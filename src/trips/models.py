from datetime import datetime
from django.conf import settings
from django.db import models


class WorkDay(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    date = models.DateField()
    mileage = models.FloatField(default=0)
    electric_bike_mileage = models.FloatField(default=0)
    bike_mileage = models.FloatField(default=0)
    foot_mileage = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    time = models.FloatField(default=0)
    electric_bike_time = models.FloatField(default=0)
    bike_time = models.FloatField(default=0)
    foot_time = models.FloatField(default=0)
    co2 = models.FloatField(default=0)

    @classmethod
    def rebuild_all(cls):
        cls.objects.all().delete()
        from data.models import DataBatch
        for db in DataBatch.objects.all().values('user', 'received_at__date').order_by('user', 'received_at__date').distinct():
            print(db)
            day = cls(user_id=db['user'], date=db['received_at__date'])
            day.build()
            day.save()

    def build(self):
        from data.models import DataBatch
        from deliveries.models import Delivery
        import geopy.distance

        batches = self.user.databatch_set.filter(received_at__date=self.date)
        deliveries = self.user.delivery_set.filter(timestamp__date=self.date)
        every = [(b.received_at, b) for b in batches] + [(d.timestamp, d) for d in deliveries]
        every.sort()

        mode = None
        last_time, last_pos = None, None
        for dt, item in every:
            if isinstance(item, DataBatch):
                for event in item.events():
                    try:
                        t = datetime.strptime(event['date'], '%Y-%m-%d %H:%M:%S.%f+0200')
                    except:
                        try:
                            t = datetime.strptime(event['date'], '%Y-%m-%d %H:%M:%S+0200')
                        except:
                            continue
                    if last_time:
                        dur = (t - last_time).seconds
                        self.time += dur
                        if mode:
                            setattr(self, mode + '_time', getattr(self, mode + '_time') + dur)
                    last_time = t

                    if 'latitude' in event:
                        pos = event['latitude'], event['longitude']
                        if last_pos:
                            distance = geopy.distance.vincenty(last_pos, pos).km
                            self.mileage += distance
                            self.co2 += .1181 * distance
                            if mode:
                                setattr(self, mode + '_mileage', getattr(self, mode + '_mileage') + distance)
                        last_pos = pos

            else:
                self.weight += item.letters_weight + item.packaged_weight
                if item.mode:
                    mode = item.mode.replace('-', '_')



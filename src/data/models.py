import json
from django.conf import settings
from django.db import models
from django.core.files.base import ContentFile


def read_uuid(data):
    return data.get('uuid', '')


class DataBatch(models.Model):
    uuid = models.CharField(max_length=255, db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)
    content = models.FileField(upload_to='data/batch')

    class Meta:
        unique_together = (('user', 'uuid'),)
        ordering = ('received_at',)

    @classmethod
    def receive(cls, user, data):
        uuid = read_uuid(data)
        print(user, uuid)
        try:
            obj = cls.objects.create(
                user=user,
                uuid=uuid
            )
        except:
            raise
            return
        else:
            obj.content.save(
                '%s/%s/%s.json' % (
                    obj.received_at.date().isoformat(),
                    user.pk,
                    uuid
                ),
                ContentFile(json.dumps(data)))
            print(obj.content.path)


    def events(self):
        import json
        with self.content.open() as f:
            d = json.load(f)
        act = d['activity'] + d['position']
        act.sort(key=lambda x: x['date'])
        return act

from django.contrib.auth.models import User
from django.test import TestCase
from oauth2_provider.models import Application
from bikes.models import ElectricBike
from trips.models import WorkDay
from data.models import DataBatch
from deliveries.models import Delivery
from push.models import PushToken
from django.conf import settings


class EndpointsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User(username='testuser',
                        first_name='Test', last_name='User')
        cls.user.set_password('testpassword')
        cls.user.save()
        cls.app = Application.objects.create(client_id='testapp', client_type='public',
                                             authorization_grant_type='password', client_secret='testsecret', skip_authorization=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.app.delete()

    def setUp(self):
        response = self.client.post('/api/1/oauth/token/', {
            'grant_type': 'password',
            'client_id': 'testapp',
            'username': 'testuser',
            'password': 'testpassword',
        })
        token = response.json()['access_token']
        self.A = {"HTTP_AUTHORIZATION": "Bearer %s" % token}

    def test_bikes_electric(self):
        ElectricBike.objects.create(id=1, label='Label')
        response = self.client.get('/api/1/bikes/electric/', **self.A)
        data = response.json()
        self.assertEqual(data[0]['id'], 1)
        self.assertEqual(data[0]['label'], 'Label')

    def test_data(self):
        self.client.post(
            '/api/1/data/',
            {"uuid": "test"},
            content_type='application/json',
            **self.A
        )
        self.assertTrue(DataBatch.objects.filter(
            uuid='test', user=self.user).exists())

    def test_days(self):
        wd = WorkDay.objects.create(
            user=self.user,
            date='2019-10-01',
            bike_time=1,
            co2=2,
            electric_bike_mileage=3.5,
            foot_time=4,
            mileage=5.5,
            time=6.5,
            weight=7.5
        )
        response = self.client.get('/api/1/days/', **self.A)
        self.assertEqual(response.json(), {"days": [{"date": "2019-10-01"}]})
        response = self.client.get('/api/1/days/2019-10-01/', **self.A)
        self.assertEqual(response.json(), {
            'bikeTime': 1,
            'co2': 2,
            'electricBikeMileage': 3.5,
            'footTime': 4,
            'mileage': 5.5,
            'time': 6.5,
            'weight': 7.5
        })

    def test_deliveries(self):
        response = self.client.post('/api/1/deliveries/test/',
                                    {
                                        # "user":1,
                                        "addresses": 1,
                                        "letters_number": 2,
                                        "letters_weight": 3,
                                        "packages_number": 4,
                                        "packaged_weight": 5,
                                    },
                                    content_type='application/json',
                                    **self.A
                                    )
        print(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Delivery.objects.all().exists())

    def test_me(self):
        response = self.client.get('/api/1/me/', **self.A)
        self.assertEquals(response.json(), {"name": "Test User"})

    def test_push(self):
        self.client.post(
            '/api/1/push/token/',
            {"token": "a-token"},
            content_type='application/json',
            **self.A
        )
        self.assertTrue(PushToken.objects.filter(
            user=self.user, token='a-token').exists())

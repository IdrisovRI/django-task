from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from data.models import Data


class DataTestCase(APITestCase):
    def setUp(self):
        Data.objects.create(a=3, b=12)
        Data.objects.create(a=1, b=4)
        Data.objects.create(a=1, b=5)
        Data.objects.create(a=1, b=5)
        Data.objects.create(a=3, b=8)
        Data.objects.create(a=5, b=3)
        Data.objects.create(a=5, b=8)

    def test_add_data(self):
        resp = self.client.post(reverse("data:add_data"), {"data": "100,100"})
        rec = Data.objects.filter(a=100, b=100).values()

        assert resp.data['result'] == 'Added 1 elements.'
        assert len(rec) == 1
        assert rec[0]['a'] == 100
        assert rec[0]['b'] == 100

    def test_add_data2(self):
        resp = self.client.post(reverse("data:add_data"), {"data": "100,100;100,200"})
        rec = Data.objects.filter(a=100).values()

        assert resp.data['result'] == 'Added 2 elements.'
        assert len(rec) == 2
        assert rec[0]['a'] == 100
        assert rec[0]['b'] == 100
        assert rec[1]['a'] == 100
        assert rec[1]['b'] == 200

    def test_get_data(self):
        resp = self.client.get(reverse("data:data_list"), {"a": 4})

        assert "5,11" == resp.data['result']

    def test_get_data2(self):
        resp = self.client.get(reverse("data:data_list"), {"b": 13})

        assert "1,14;3,20" == resp.data['result']

    def test_get_data3(self):
        resp = self.client.get(reverse("data:data_list"), {"a": 3, "b": 12})

        assert "3,20" == resp.data['result']

from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Image
# Create your tests here.



class TestImage(APITestCase):
    url = "/image_upload/"

    def setUp(self):
        Image.objects.create(image="Testimage.png", uploaded_by=2)

    def test_get_image(self):
        
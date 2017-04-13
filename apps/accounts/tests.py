from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.test_user = {'email': 'test@a.co', 'password': 'helloworld'}

    def test_can_register_user(self):
        '''
        Ensure that we can register a new user.
        '''
        resp = self.client.post(reverse('register'),
                                self.test_user,
                                format='json')

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(email='test@a.co').email,
                         'test@a.co')

    def test_can_obtain_jwt_token(self):
        '''
        Ensure that we can obtain a jwt token, given valid credentials.
        '''
        self.client.post(reverse('register'), self.test_user, format='json')
        resp = self.client.post(reverse('obtain-jwt-token'),
                                self.test_user,
                                format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(resp.data['token'])

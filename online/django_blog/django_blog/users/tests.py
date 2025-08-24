from django.test import TestCase
from django.urls import reverse
from .models import User

class UsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='9V7B0@example.com')

    def test_users_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
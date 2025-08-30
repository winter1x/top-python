from django.test import TestCase
from django.urls import reverse
from .models import User
#from django.contrib.auth import get_user_model

#User = get_user_model()

class UsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='9V7B0@example.com')

    def test_users_list(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
    
    def test_user_update_flow(self):
        update_url = reverse('update', kwargs={'pk': self.user.pk})
        list_url = reverse('index')

        self.client.post(update_url, {'username': 'newtestuser', 'email': self.user.email})

        response = self.client.get(list_url)

        self.assertContains(response, 'newtestuser')
        self.assertFalse(User.objects.filter(username='testuser').exists())
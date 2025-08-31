from django.test import TestCase
from django.urls import reverse
from django_blog.users.models import BlogUser

class UsersTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user = BlogUser.objects.get(username='testuser')
        #self.user = BlogUser.objects.create(username='testuser', email='9V7B0@example.com')

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
        self.assertFalse(BlogUser.objects.filter(username='testuser').exists())
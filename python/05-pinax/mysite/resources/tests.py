import pprint as pp
from django.test import TestCase, Client
from django.contrib.auth.models import User

class FirsTest(TestCase):
    def test_test_test(self):
        self.assertEqual(404, 404)

class UserTest(TestCase):
    def setUp(self):
        user = User.objects.create_user('test', 'test@email.com', 'test')
        self.client = Client()

    def test_login(self):
        logged_in = self.client.login(username='test', password='test')
        self.assertEqual(logged_in, True)
        #pp.pprint(logged_in)




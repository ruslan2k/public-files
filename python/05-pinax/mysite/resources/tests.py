import pprint as pp
from django.test import TestCase, Client
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Login"]').click()


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

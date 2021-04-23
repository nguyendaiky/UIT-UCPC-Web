from django.test import SimpleTestCase
from django.urls import reverse, resolve
from register.views import home, register, login, profile, edit, logout

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse('home')
        print(resolve(url))
        #self.assertEquals(resolve(url).func, home)
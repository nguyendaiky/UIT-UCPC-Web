from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


from register.models import School, Team

# 👋 TESTING HOMEPAGE

class Home(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/home.html')

class BaseTestRegister(TestCase):
    def setUp(self):
        self.register_url=reverse('register:register')
        school = School.objects.create(school='Foobar')
        self.user={
            'team': 'Team A',
            'member1': 'Nguyễn Văn Khang',
            'member2': 'Trương Minh Quân',
            'member3': 'Nhạc Phi',
            'email': 'test@gm.uit.edu.vn',
            'phone': '0983416237',
            'school': [school.id],
            'password': 'password'}
        self.user_invalid_teamname={
            'team': '🙁',
            'member1': 'Nguyễn Văn Khang',
            'member2': 'Trương Minh Quân',
            'member3': 'Nhạc Phi',
            'email': 'test@gm.uit.edu.vn',
            'phone': '0983416237',
            'school': [school.id],
            'password': 'password'}
        self.user_invalid_membername={
            'team': 'Team A',
            'member1': '🙁',
            'member2': '🙁',
            'member3': '🙁',
            'email': 'test@gm.uit.edu.vn',
            'phone': '0983416237',
            'school': [school.id],
            'password': 'password'}
        self.user_invalid_email={
            'team': 'Team A',
            'member1': 'Nguyễn Văn Khang',
            'member2': 'Trương Minh Quân',
            'member3': 'Nhạc Phi',
            'email': 'test.com',
            'phone': '0983416237',
            'school': [school.id],
            'password': 'password'}
        return super().setUp()
class TestRegister(BaseTestRegister):
    def test_can_view_page_correctly(self):
       response=self.client.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'register/register.html')
    def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
    # def test_cant_register_user_invalid_email(self):
    #     response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
    #     self.assertEqual(response.status_code,400)


# 📝 TESTING REGISTER
class Register(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        """Check able to register normaly"""
        team_count = Team.objects.count()
        school = School.objects.create(school='Foobar')
        response = self.client.post(
            reverse('register:register'), {
                'team': 'Team A',
                'member1': 'Nguyễn Văn Khang',
                'member2': 'Trương Minh Quân',
                'member3': 'Nhạc Phi',
                'email': 'test@gm.uit.edu.vn',
                'phone': '0983416237',
                'school': [school.id],
                'password': 'password'})
        self.assertEqual(response.status_code, 302)  # HttpResponseRedirect
        self.assertEqual(Team.objects.count(), team_count + 1)


# 📝 TESTING LOGIN
class BaseTestLogin(TestCase):
    def setUp(self):
        self.login_url=reverse('register:login')
        self.user={
            'username':'testuser',
            'email':'test@test.com',
            'password':'123456',}
        return super().setUp()

class Login(BaseTestLogin):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_success(self):
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)


class Profile(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class Edit(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class Logout(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
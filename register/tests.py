from django.test import TestCase
from django.urls import reverse


from register.models import School, Team

# 👋 TESTING HOMEPAGE


class Home(TestCase):
    def test_able_to_access(self):
        """Check if status is 200 👌"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/home.html')


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

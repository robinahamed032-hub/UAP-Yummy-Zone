from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CanteenSystemTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='student1',
            password='password123'
        )

    def test_student_login_page_status(self):

        response = self.client.get(reverse('student_home')) # অথবা আপনার লগইন URL name
        self.assertEqual(response.status_code, 200)

    def test_student_login_functionality(self):
        response = self.client.post(reverse('student_home'), {
            'username': 'student1',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
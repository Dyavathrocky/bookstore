from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve ,reverse
from .views import SignupPageView
from .forms import CustomUserCreationForm

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        
        _user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
                )

        self.assertEqual(_user.username,'will')
        self.assertEqual(_user.email,'will@email.com')
        self.assertTrue(_user.is_active)
        self.assertFalse(_user.is_staff)
        self.assertFalse(_user.is_superuser)

    
    def test_create_superuser(self):
        User = get_user_model()

        admin_user = User.objects.create_superuser(
            username = 'superadm',
            email = 'superadm@gmail.com',
            password = 'super123'
        )

        self.assertEqual(admin_user.username,'superadm')
        self.assertEqual(admin_user.email,'superadm@gmail.com')
        #self.assertEqual(admin_user.password,'super123')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupPageTest(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url =  reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_templates(self):
        self.assertEqual(self.response.status_code , 200)
        self.assertTemplateUsed(self.response , 'account/signup.html')
        self.assertContains(self.response , 'Signup')
        self.assertNotContains(self.response , 'hi myself rakeshhhhh')

    def test_signup_form(self):
        #form = self.response.context.get('form')
        #self.assertIsInstance(form , CustomUserCreationForm)
        #self.assertContains(self.response,'csrfmiddlewaretoken')
        _new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)

    '''def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )'''







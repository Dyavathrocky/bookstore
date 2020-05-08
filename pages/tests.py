from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse , resolve
from .views import HomePageView , AboutPageView

# Create your tests here.

'''class HomePageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code ,200)

    def test_homepage_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response , 'home.html')

    def test_hompage_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response , 'Home Page')

    def test_homepage_does_not_contains_incorrecet_html(self):
        response = self.client.get('/')
        self.assertNotContains(response , 'hi i am here hisiihsihihs')'''


# ifdont want repeat everytime the response element , need to setup reverse url any way test run from top to bottom.


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_templates(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_hompage_contains_correct_html(self):
        self.assertContains(self.response, 'Home Page')

    def test_homepage_does_not_contains_incorrecet_html(self):
        self.assertNotContains(self.response, 'hi i am here hisiihsihihs')
    
    def test_homepage_url_resolves_homepageview(self):
        _view = resolve('/')
        self.assertEqual(_view.func.__name__,HomePageView.as_view().__name__)


class AboutPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code , 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response , 'about.html')
    
    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response , 'About Page')

    def test_aboutpage_doesnot_contains_html(self):
        self.assertNotContains(self.response , 'Hi there i am rakesh')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
    





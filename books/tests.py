from django.test import TestCase , Client
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Book , Review

# Create your tests here.

class BookTest(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'reviewuser' ,
            email = 'revieuser@gmail.com' ,
            password = 'testpass123',
        )
        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title = 'harry potter',
            author = 'jk rowling',
            price = '29.00'
        )

        self.review = Review.objects.create(
            book = self.book ,
            author = self.user ,
            review = 'ok ok '
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'harry potter')
        self.assertEquals(f'{self.book.author}', 'jk rowling')
        self.assertEquals(f'{self.book.price}' , '29.00')

    def test_book_detail_view(self):
        _response = self.client.get(self.book.get_absolute_url())
        _no_response = self.client.get('/books/12345')
        self.assertEqual(_response.status_code , 200)
        self.assertEqual(_no_response.status_code , 404)
        self.assertContains(_response , 'harry potter')
        self.assertContains(_response , 'ok ok ')
        self.assertTemplateUsed(_response , 'books/book_detail.html')

    def test_book_list_view(self):
        _response = self.client.get(reverse('book_list'))
        self.assertEqual(_response.status_code, 200)
        self.assertContains(_response , 'harry potter')
        self.assertTemplateUsed(_response , 'books/book_list.html')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@gmail.com' , password='testpass123')
        _response = self.client.get(reverse('book_list'))
        self.assertEqual(_response.status_code , 200)
        self.assertContains(_response , 'harry potter')
        self.assertTemplateUsed(_response ,'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        _response = self.client.get(reverse('book_list'))
        self.assertEqual(_response.status_code , 302)
        self.assertRedirects(
            _response , '%s?next=/books/' % (reverse('account_login')))
        _response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(_response,'Log In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='revieuser@gmail.com',password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        _response = self.client.get(self.book.get_absolute_url())
        _no_response = self.client.get('/books/12345')
        self.assertEqual(_response.status_code , 200)
        self.assertEqual(_no_response.status_code , 404)
        self.assertContains(_response , 'harry potter')
        self.assertContains(_response , 'ok ok')
        self.assertTemplateUsed(_response , 'books/book_detail.html')



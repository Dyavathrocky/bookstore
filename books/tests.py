from django.test import TestCase , client

from django.urls import reverse

from .models import Book

# Create your tests here.

class BookTest(TestCase):


    def setUp(self):
        self.book = Book.objects.create(
            title = 'harry potter',
            author = 'jk rowling',
            price = '29.00')

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
        self.assertTemplateUsed(_response , 'books/book_detail.html')

    def test_book_list_view(self):
        _response = self.client.get(reverse('book_list'))
        self.assertEqual(_response.status_code, 200)
        self.assertContains(_response , 'harry potter')
        self.assertTemplateUsed(_response , 'books/book_list.html')
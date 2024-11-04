from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from books.models import Book, Review


User = get_user_model()


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="pass123"
        )
        cls.special_permission = Permission.objects.get(codename="special_status")
        cls.book = Book.objects.create(
            title="Python Kicks Ass",
            author="John Wayne",
            price="29.00"
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review"
        )


    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Python Kicks Ass")
        self.assertEqual(f"{self.book.author}", "John Wayne")
        self.assertEqual(f"{self.book.price}", "29.00")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="pass123")
        response = self.client.get(reverse("books:book-list"))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Python Kicks Ass")
        self.assertTemplateUsed(response, "books/book_list.html")


    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("books:book-list"))

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(
            response,
            "%s?next=/books/" % (reverse("account_login"))
        )
        self.assertContains(response, "Log In")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="pass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(no_response.status_code, HTTPStatus.NOT_FOUND)
        self.assertContains(response, "John Wayne")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")

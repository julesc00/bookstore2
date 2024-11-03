from http import HTTPStatus

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:home")
        self.res = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_url_name(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.res, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, "This is the Home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, "Hi there!")

    def test_homepage_url_resolve_home_page_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:about")
        self.res = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.res, "pages/about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.res, "About Page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.res, "Hi there! I should not be on the page.")

    def test_about_page_url_resolves_about_page_view(self):
        view = resolve("/about/")

        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
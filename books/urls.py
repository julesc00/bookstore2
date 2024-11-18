from django.urls import path

from books.views import BookListView, BookDetailView, SearchResultsListView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="book-list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("search/", SearchResultsListView.as_view(), name="search-results"),
]
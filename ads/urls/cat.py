from django.urls import path

from ads.views.cat import CatDetailView, CatCreateView, CatListView, CatUpdateView, \
    CatDeleteView

urlpatterns = [
    path("create/", CatCreateView.as_view()),
    path("<int:pk>/", CatDetailView.as_view()),
    path("", CatListView.as_view()),
    path("<int:pk>/update/", CatUpdateView.as_view()),
    path("<int:pk>/delete/", CatDeleteView.as_view()),
]
from django.urls import path
from rest_framework import routers
from ads.views.cat import CatListView, CatDetailView, CatCreateView, CatUpdateView, CatDeleteView


from ads.views.cat import CatViewSet

# urlpatterns = [
#     path('', CatListView.as_view()),
#     path('<int:pk>/', CatDetailView.as_view()),
#     path('create/', CatCreateView.as_view()),
#     path('update/<int:pk>/', CatUpdateView.as_view()),
#     path('delete/<int:pk>/', CatDeleteView.as_view()),
# ]

router = routers.SimpleRouter()
router.register('', CatViewSet)
urlpatterns = router.urls
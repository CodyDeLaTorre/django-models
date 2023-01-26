from django.urls import path

from .views import AboutPageView, SnackCreateView, SnackDeleteView, SnackListView, SnackDetailView, SnackUpdateView

urlpatterns = [
  # path('', HomePageView.as_view(), name='home'),
  path('about', AboutPageView.as_view(), name='about'),
  path('', SnackListView.as_view(), name="snacks_list"),
  path('snacks/<int:pk>/', SnackDetailView.as_view(), name="snacks_detail"),
  path('snacks/create/', SnackCreateView.as_view(), name="snacks_create"),
  path('snacks/<int:pk>/update/', SnackUpdateView.as_view(), name="snacks_update"),
  path('snacks/<int:pk>/delete/', SnackDeleteView.as_view(), name="snacks_delete"),
]

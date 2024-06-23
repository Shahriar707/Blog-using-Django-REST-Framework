from django.urls import path
from .views import BlogView, PublicBlogView

urlpatterns = [
    path('', PublicBlogView.as_view()),
    path('blog/', BlogView.as_view()),
]

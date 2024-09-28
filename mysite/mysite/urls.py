from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

# Optional: Define a view for the home page
def home(request):
    return HttpResponse("Welcome to the home page!")

urlpatterns = [
    path("", home, name="home"),  # Handle root URL
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]


from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("projects/", views.projects,name="projects"),
    path("eda", views.eda,name="eda"),
    path("testimonials/", views.testimonials,name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume,name="resume")
]
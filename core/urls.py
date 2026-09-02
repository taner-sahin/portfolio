from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    
    path("projects/careertrack/case-study/",
        views.careertrack_case_study,
        name="careertrack_case_study",
    ),
]
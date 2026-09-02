from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def careertrack_case_study(request):
    return render(request, "careertrack_case_study.html")
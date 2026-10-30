"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API.views import AboutView,EducationView,StudentView,ProjectsView,SkillsView,ExperianceView,CertificateView
from API.views import ServicesView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',AboutView.as_view()),
    path('education/',EducationView.as_view()),
    path('student/',StudentView.as_view()),
    path('projects/',ProjectsView.as_view()),
    path('skills/',SkillsView.as_view()),
    path('experiance/',ExperianceView.as_view()),
    path('certificates/',CertificateView.as_view()),
    path('services/',ServicesView.as_view()),
]

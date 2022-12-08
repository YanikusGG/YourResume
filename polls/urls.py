from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('create_resume/', views.resume_create, name='create_resume_url'),
    path('resumes/', views.resume_list, name='resume_list_url'),
    path('resume/<str:resume_name>/download', views.resume_download, name='download_resume_url'),
    path('resume/<str:resume_name>/', views.resume_view, name='view_resume_url'),
]

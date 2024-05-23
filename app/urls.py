
from django.urls import path
# from app.views import hello, job_detail
from app import views

urlpatterns = [
    path('', views.jobs, name="jobs_home"),
    path('job_detail/<int:id>', views.job_detail, name="job_details"),
]
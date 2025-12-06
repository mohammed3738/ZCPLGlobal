from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_study_list, name="case_study_list"),
    path("create/", views.create_case_study, name="create_case_study"),
    path('<slug:slug>/', views.case_study_detail, name="case_study_detail"),

]

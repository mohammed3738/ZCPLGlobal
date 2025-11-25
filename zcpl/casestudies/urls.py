from django.urls import path
from . import views

urlpatterns = [
    path('', views.case_study_list, name="case_study_list"),
    path('<slug:slug>/', views.case_study_detail, name="case_study_detail"),
    path('category/<slug:slug>/', views.case_studies_by_category, name='case_studies_by_category'),

]


from django.urls import path
from .views import* 

urlpatterns = [
    path('',EmployeeCreateApi.as_view()),
    path("api/",EmployeeApi.as_view()),
    path("view/<int:pk>/",EmployeeUpdateApi.as_view()),
    path("delete/<int:pk>/",EmployeeDeleteApi.as_view()),
]

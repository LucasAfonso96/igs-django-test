from .views import home, collaborator_add, collaborator_list, collaborator_remove, department_list, department_add, department_remove
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('collaborators/', collaborator_list, name='collaborator_list'),
    path('collaborators/add/', collaborator_add, name='collaborator_add'),
    path('collaborators/<int:pk>/remove/', collaborator_remove, name='collaborator_remove'),
    path('departments/', department_list, name='department_list'),
    path('departments/add/', department_add, name='department_add'),
    path('departments/<int:pk>/remove/', department_remove, name='department_remove'),
]
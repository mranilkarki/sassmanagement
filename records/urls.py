from django.urls import path
from records import views
from django.contrib.auth import views as auth_views


app_name= 'records'
urlpatterns = [
    path('list/', views.students_list, name="NameOfStudents"),
    path('register/', views.register, name="registerstudents"),
    path('editmode/',views.editmode, name="editmode"),
    path('editmode1/',views.editmode1, name="editmode1"),
    path('upload/', views.upload, name="uploads"),
    path('search/', views.search, name="search"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    
]


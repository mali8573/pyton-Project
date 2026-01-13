from django.http import HttpResponseNotFound
from django.urls import path, re_path
from task_managment_app1 import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('all_tasks/', views.all_tasks_view, name='all_tasks'),
    path('add_task/', views.add_task_view, name='add_task'),
    path('update_task/<int:taskid>', views.update_task_view, name='update_task'),
    path('update_status_task/<int:taskid>', views.update_status_task_view, name='update_status_task'),
    path('delete_task/<int:taskid>', views.delete_task_view, name='delete_task'),
    path('add_team/', views.add_team_view, name='add_team'),
    path('personal_details/', views.personal_datails_view, name='personal_details'),
    path('error', views.error_view, name='error'),
    re_path(r'^.*$', views.custom_404_view, name='custom_404'),
]
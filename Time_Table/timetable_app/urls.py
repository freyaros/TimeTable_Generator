from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('timetable/create/', views.timetable_create, name='timetable_create'),
    path('timetable/classgroup/<int:group_id>/', views.classgroup_timetable, name='classgroup_timetable'),
    path('timetable/classgroup/<int:group_id>/delete/', views.delete_classgroup_timetable, name='delete_classgroup_timetable'),
    path('add/classgroup/', views.add_class_group, name='add_class_group'),
    path('add/subject/', views.add_subject, name='add_subject'),
    path('add/teacher/', views.add_teacher, name='add_teacher'),
]
from django.urls import path
from student_app.api import studenttableCreateApi,studenttableApi,DeleteApi
urlpatterns = [
    path('api/create',studenttableCreateApi.as_view()),
    path('api',studenttableApi.as_view()),
    path('api/delete',DeleteApi.as_view()),
    
]

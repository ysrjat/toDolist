from django.urls import path
from .views import TaskList
from .views import TaskDetail


urlpatterns = [
    path('',TaskList.as_view(), name='task'),
    path('task/<int:pk>' , TaskDetail.as_view(), name="task_Detail" ),
]
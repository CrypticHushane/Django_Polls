from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate

urlpatterns = [
    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='createTask'),
    path('task-update/<str:pk>', TaskUpdate.as_view(), name='updateTask'),
]
from django.urls import path
from .views import Register, TaskList,TaskDetail,TaskCreate,TaskUpdate, TaskDelete,CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

    path('register', Register.as_view(), name='register'),

    path('tasks', TaskList.as_view(), name='tasks'),
    path('task/<str:pk>', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='createTask'),
    path('task-update/<str:pk>', TaskUpdate.as_view(), name='updateTask'),
    path('task-delete/<str:pk>', TaskDelete.as_view(), name='deleteTask'),
]
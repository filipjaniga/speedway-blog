from django.urls import path
from .views import HomeView, TaskDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='calendar_home'),
    path('task/<int:pk>', TaskDetailsView.as_view(), name='calendar_details')
]
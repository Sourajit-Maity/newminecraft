from django.urls import path
from . import views

urlpatterns = [
    # Login view
    path('home/', views.home_view, name='dashboard'),
    path('upload/Masterproduct/', views.upload_master_file, name='upload_master_file'),
    path('get/Masterproduct/', views.get_feedback_data, name='get_feedback_data'),
]

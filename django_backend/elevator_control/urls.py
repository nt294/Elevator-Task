from django.urls import path
from .views import get_all_floors, control_panels_by_floor, request_elevator, get_all_elevator_info

urlpatterns = [
    path('get-all-floors/', get_all_floors, name='get_all_floors'),
    path('floor/<int:floor_id>/control-panels/', control_panels_by_floor, name='control_panels_by_floor'),
    path('request-elevator/', request_elevator, name='request_elevator'),
    path('get-all-elevator-info/', get_all_elevator_info, name='get_all_elevator_info'),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='http://localhost:3000'), name='redirect-to-frontend'),
    path('admin/', admin.site.urls),
    path('elevator-control/', include('elevator_control.urls')),
]

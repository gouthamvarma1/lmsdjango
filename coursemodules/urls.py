
from django.urls import path
from .views import ModuleView


urlpatterns = [
    path('modules', ModuleView.as_view())
            ]

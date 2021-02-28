
from django.urls import include,path

from rest_framework import routers
from . import views
# from .views import ModuleView

router = routers.DefaultRouter()
router.register(r'assignment', views.AssignmentViewSet)

# urlpatterns = [
#     path('modules', ModuleView.as_view())
#             ]

urlpatterns = [
    path('', include(router.urls))
]

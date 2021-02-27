
from django.urls import include,path
# from .views import ModuleView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'modules', views.ModuleViewSet)
router.register(r'courses', views.CourseViewSet)

# urlpatterns = [
#     path('modules', ModuleView.as_view())
#             ]

urlpatterns = [
    path('', include(router.urls))
]

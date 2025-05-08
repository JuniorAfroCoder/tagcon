from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

router = routers.DefaultRouter()

router.register(r'attendees', AttendeeViewSet)
router.register(r'exhibitors', ExhibitorViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

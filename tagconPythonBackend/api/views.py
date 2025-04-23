from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action, permission_classes
from .permissions import ReadOnlyRequiresAuth
from .mixins import ExportMixin

class ExhibitorViewSet(ExportMixin,viewsets.ModelViewSet):
    queryset = Exhibitor.objects.all()
    serializer_class = ExhibitorSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['companyName', 'spaceNeeded']
    search_fields = ['name', 'email', 'companyName', 'phoneNumber']
    export_fields = ['name', 'email', 'phone_number', 'company_name', 'company_description', 'space_needed', 'created_at']
    export_filename = 'exhibitors'


class AttendeeViewSet(ExportMixin,viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['sex', 'age']
    search_fields = ['name', 'email', 'phone_number']
    export_fields = ['name', 'email', 'phone_number', 'age', 'sex', 'created_at']
    export_filename = 'attendees'

class VolunteerViewSet(ExportMixin,viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['sex', 'age']
    search_fields = ['name', 'email', 'phone_number']
    export_fields = ['name', 'email', 'phone_number', 'age', 'sex', 'created_at']
    export_filename = 'volunteers'

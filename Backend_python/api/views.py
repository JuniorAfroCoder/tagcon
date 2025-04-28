from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action, permission_classes
from .permissions import ReadOnlyRequiresAuth
from .mixins import *
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ExhibitorViewSet(ExportMixin,SimplePostResponseMixin,viewsets.ModelViewSet):
    queryset = Exhibitor.objects.all()
    serializer_class = ExhibitorSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['companyName', 'spaceNeeded']
    search_fields = ['name', 'email', 'companyName', 'phoneNumber']
    export_fields = ['name', 'email', 'phone_number', 'company_name', 'company_description', 'space_needed', 'created_at']
    export_filename = 'exhibitors'


class AttendeeViewSet(ExportMixin,SimplePostResponseMixin,viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['sex', 'age']
    search_fields = ['name', 'email', 'phone_number']
    export_fields = ['name', 'email', 'phone_number', 'age', 'sex', 'created_at']
    export_filename = 'attendees'

class VolunteerViewSet(ExportMixin,SimplePostResponseMixin,viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [ReadOnlyRequiresAuth]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['sex', 'age']
    search_fields = ['name', 'email', 'phone_number']
    export_fields = ['name', 'email', 'phone_number', 'age', 'sex', 'created_at']
    export_filename = 'volunteers'


class ContactView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        subject = request.data.get('subject', 'TAGCON Get In Touch')
        message = request.data.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(subject, full_message, email, ['tagcon@ksquad.dev'])
        send_mail(
            subject=f"[TAGCON : 2025] ",
            message=f"Vôtre message a été envoyé avec succès. Nous vous contacterons dès que possible.",
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
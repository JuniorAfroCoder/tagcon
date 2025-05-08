from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        data['groups'] = groups
        data['is_admin'] = self.user.is_superuser
        data['id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name

        return data


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = '__all__'

class ExhibitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__' 
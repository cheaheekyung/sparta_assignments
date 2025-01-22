from rest_framework import serializers
from .models import User
from django.contrib.auth.models import User


class UserRegisterSerialize(serializers.ModelSerializer):
    pass

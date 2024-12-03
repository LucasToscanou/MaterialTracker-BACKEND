from rest_framework import serializers
from MaterialTrackerApp.models import *
from django.utils import timezone

class MTMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class MTMaterialSerializerCreateItem(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            'id',
            'ref',
            'description',
            'project',
            'main_img',
            'current_location',
            'cost',
            'currency',
            'quality_exp_date',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class MaterialImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialImg
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
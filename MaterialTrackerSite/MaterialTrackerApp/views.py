import csv

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views import View
from django.contrib import messages 

from MaterialTrackerApp.models import *
from django.urls import reverse
from random import *
import json
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from MaterialTrackerApp.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class MaterialView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all materials",
        operation_description="Get all materials",
        responses={200: MTMaterialSerializer(many=True)}
    )
    def get(self, request):
        queryset = Material.objects.all()
        serializer = MTMaterialSerializer(queryset, many=True)
        print("serializer.data = " + str(serializer.data))
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete selected materials",
        operation_description="Delete materials based on selected IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'selectedItems': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of material IDs to delete'
                )
            }
        ),
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request):
        id_erro = ""
        erro = False

        selected_items = request.data.get("selectedItems", [])
        print("Selected items:", selected_items)

        for id in selected_items:
            mat = Material.objects.filter(id=id).first()
            if mat:
                mat.delete()
            else:
                id_erro += str(id) + " "
                erro = True

        if erro:
            return Response({'error': f'item(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class MaterialDetailView(APIView):
    @swagger_auto_schema(
        operation_summary="Get a specific material",
        operation_description="Get a specific material based on ID",
        responses={200: MTMaterialSerializer}
    )
    def get(self, request, pk):
        material = Material.objects.filter(id=pk).first()
        if material:
            serializer = MTMaterialSerializer(material)
            return Response(serializer.data)
        else:
            return Response({'error': f'Material with ID {pk} not found'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Update a specific material",
        operation_description="Update a specific material based on ID",
        request_body=MTMaterialSerializerCreateItem,
        responses={
            200: MTMaterialSerializer,
            400: 'Bad Request',
            404: 'Not Found'
        }
    )
    def put(self, request, pk):
        print("request.data = " + str(request.data))
        material = Material.objects.filter(id=pk).first()
        if material:
            serializer = MTMaterialSerializerCreateItem(material, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': f'Material with ID {pk} not found'}, status=status.HTTP_404_NOT_FOUND)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProjectView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all projects",
        operation_description="Retrieve a list of all projects",
        responses={200: ProjectSerializer(many=True)}
    )
    def get(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete selected projects",
        operation_description="Delete projects based on selected IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'selectedItems': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of project IDs to delete'
                )
            }
        ),
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request):
        id_erro = ""
        erro = False

        selected_items = request.data.get("selectedItems", [])
        for id in selected_items:
            project = Project.objects.filter(id=id).first()
            if project:
                project.delete()
            else:
                id_erro += str(id) + " "
                erro = True

        if erro:
            return Response({'error': f'Project(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)




@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class LocationView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all locations",
        operation_description="Retrieve a list of all locations",
        responses={200: LocationSerializer(many=True)}
    )
    def get(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete selected locations",
        operation_description="Delete locations based on selected IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'selectedItems': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of location IDs to delete'
                )
            }
        ),
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request):
        id_erro = ""
        erro = False

        selected_items = request.data.get("selectedItems", [])
        for id in selected_items:
            location = Location.objects.filter(id=id).first()
            if location:
                location.delete()
            else:
                id_erro += str(id) + " "
                erro = True

        if erro:
            return Response({'error': f'Location(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# class UserProfileView(APIView):
#     @swagger_auto_schema(
#         operation_summary="Get all user profiles",
#         operation_description="Retrieve a list of all user profiles",
#         responses={200: UserProfileSerializer(many=True)}
#     )
#     def get(self, request):
#         queryset = UserProfile.objects.all()
#         serializer = UserProfileSerializer(queryset, many=True)
#         return Response(serializer.data)

#     @swagger_auto_schema(
#         operation_summary="Delete selected user profiles",
#         operation_description="Delete user profiles based on selected IDs",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'selectedItems': openapi.Schema(
#                     type=openapi.TYPE_ARRAY,
#                     items=openapi.Items(type=openapi.TYPE_INTEGER),
#                     description='List of user profile IDs to delete'
#                 )
#             }
#         ),
#         responses={
#             204: 'No Content',
#             404: 'Not Found'
#         }
#     )
#     def delete(self, request):
#         id_erro = ""
#         erro = False

#         selected_items = request.data.get("selectedItems", [])
#         for id in selected_items:
#             user_profile = UserProfile.objects.filter(id=id).first()
#             if user_profile:
#                 user_profile.delete()
#             else:
#                 id_erro += str(id) + " "
#                 erro = True

#         if erro:
#             return Response({'error': f'User profile(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
    
#     @swagger_auto_schema(
#         operation_summary="Create a new user profile",
#         operation_description="Create a new user profile",
#         request_body=UserProfileSerializer,
#         responses={
#             201: UserProfileSerializer,
#             400: 'Bad Request'
#         }
#     )
#     def post(self, request):
#         serializer = UserProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             user_profile = serializer.save()
#             return Response(UserProfileSerializer(user_profile).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class MaterialImgView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all material images",
        operation_description="Retrieve a list of all material images",
        responses={200: MaterialImgSerializer(many=True)}
    )
    def get(self, request):
        queryset = MaterialImg.objects.all()
        serializer = MaterialImgSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete selected material images",
        operation_description="Delete material images based on selected IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'selectedItems': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of material image IDs to delete'
                )
            }
        ),
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request):
        id_erro = ""
        erro = False

        selected_items = request.data.get("selectedItems", [])
        for id in selected_items:
            material_img = MaterialImg.objects.filter(id=id).first()
            if material_img:
                material_img.delete()
            else:
                id_erro += str(id) + " "
                erro = True

        if erro:
            return Response({'error': f'Material image(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CurrencyView(APIView):
    @swagger_auto_schema(
        operation_summary="Get all currencies",
        operation_description="Retrieve a list of all currencies",
        responses={200: CurrencySerializer(many=True)}
    )
    def get(self, request):
        queryset = Currency.objects.all()
        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete selected currencies",
        operation_description="Delete currencies based on selected IDs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'selectedItems': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_INTEGER),
                    description='List of currency IDs to delete'
                )
            }
        ),
        responses={
            204: 'No Content',
            404: 'Not Found'
        }
    )
    def delete(self, request):
        id_erro = ""
        erro = False

        selected_items = request.data.get("selectedItems", [])
        for id in selected_items:
            currency = Currency.objects.filter(id=id).first()
            if currency:
                currency.delete()
            else:
                id_erro += str(id) + " "
                erro = True

        if erro:
            return Response({'error': f'Currency(s) [{id_erro.strip()}] not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class MaterialCreateView(APIView):
    @swagger_auto_schema(
        operation_summary="Create a new material",
        operation_description="Create a new material",
        request_body=MTMaterialSerializer,
        responses={
            201: MTMaterialSerializer,
            400: 'Bad Request'
        }
    )
    def post(self, request):
        print("request.data = " + str(request.data))  # Log incoming data for debugging
        
        serializer = MTMaterialSerializerCreateItem(data=request.data)
        if serializer.is_valid():
            material = serializer.save()  # Automatically fills in id, created_at, updated_at
            return Response(MTMaterialSerializerCreateItem(material).data, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)  # Log errors for debugging
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

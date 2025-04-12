from django.shortcuts import get_object_or_404
from rest_framework import status , generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import * 
from .serializers import * 
from .permissions import IsInGroup , IsInMultipleGroups 
# Create your views here.


class ListCreateCity( generics.ListCreateAPIView ) :
    permission_classes = [ IsInGroup( 'Admin' ) ]
    serializer_class = CitySerializer 
    queryset = City.objects.all() 

class CityDetailDelete( generics.RetrieveDestroyAPIView ) : 
    permission_classes = [ IsInGroup( 'Admin' ) ]
    serializer_class = CitySerializer 
    queryset = City.objects.all() 

class ListCreateLab( generics.ListCreateAPIView ) :
    permission_classes = [ IsInGroup( 'Admin' ) ]     
    serializer_class = LabSerializer 
    queryset = Lab.objects.all()

class LabDetailUpdateDelete( generics.RetrieveUpdateDestroyAPIView ) :
    permission_classes = [ IsInGroup( 'Admin' ) ]    
    serializer_class = LabSerializer 
    queryset = Lab.objects.all() 

class ListCreatePharmacy( generics.ListCreateAPIView ) :     
    serializer_class = PharmacySerializer 
    queryset = Pharmacy.objects.all() 

class PharmacyDetailUpdateDelete( generics.RetrieveUpdateDestroyAPIView ) : 
    serializer_class = PharmacySerializer 
    queryset = Pharmacy.objects.all() 

class ListCreateProduct( generics.ListCreateAPIView ) :
    serializer_class = ProductSerializer 
    queryset = Product.objects.all() 

class ProductDetailUpdateDelete( generics.RetrieveUpdateDestroyAPIView ) :
    serializer_class = ProductSerializer 
    queryset = Product.objects.all() 



 

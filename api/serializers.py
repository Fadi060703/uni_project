from rest_framework import serializers 
from .models import * 

class CitySerializer( serializers.ModelSerializer ) :
    class Meta : 
        model = City 
        fields = [ 'name' ] 

class LabSerializer( serializers.ModelSerializer ) : 
    CitySerializer() 
    class Meta : 
        model = Lab 
        fields = [ 'name' , 'city' ]

class PharmacySerializer( serializers.ModelSerializer ) :
    CitySerializer()
    class Meta :
        model = Pharmacy 
        fields = [ 'name' , 'city' , 'address' , 'phone_number' ] 

class ProductSerializer( serializers.ModelSerializer ) :
    LabSerializer() 
    class Meta :
        model = Product 
        fields = [ 'name' , 'manufacturing_lab' , 'type' , 'man_price' ,
                   'sell_price' , 'code' ] 
        
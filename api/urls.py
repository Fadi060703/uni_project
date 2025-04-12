from django.urls import path 
from .views import * 

urlpatterns = [
    # API Endpoints
        # Admin , Manager , Site Settings and Models 
    path( 'cities' , ListCreateCity.as_view() , name = 'cities-list' ) ,
    path( 'cities/<int:pk>' , CityDetailDelete.as_view() , name = 'cities-detail' ) ,
    path( 'labs' , ListCreateLab.as_view() , name = 'labs-list' ) ,
    path( 'labs/<int:pk>' , LabDetailUpdateDelete.as_view() , name = 'labs-detail' ) , 
    path( 'pharmacies' , ListCreatePharmacy.as_view() , name = 'pharmacies-list' ) ,
    path( 'pharmacies/<int:pk>' , PharmacyDetailUpdateDelete.as_view() , name = 'pharmacies-detail' ) ,

]
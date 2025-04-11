from django.db import models
from django.utils import timezone

# Create your models here.
class City( models.Model ) :
    name = models.CharField( max_length = 30 ) 

    def __str__( self ) :
        return f'{ self.name }' 
    

class Lab( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'labLocation' ) 

    def __str__( self ) : 
        return f'{ self.name } + ( { self.city } )'
    
class Pharmacy( models.Model ) :
    name = models.CharField( max_length = 255 )
    city = models.ForeignKey( City , on_delete = models.CASCADE , related_name = 'pharmLocation' )  
    address = models.TextField() 
    phone_number = models.CharField( max_length = 20 ) 

    def __str__( self ) : 
        return f'{ self.name } + ( { self.city } )' 
    

class Product( models.Model ) :
    name = models.CharField( max_length = 255 ) 
    manufacturing_lab = models.ForeignKey( Lab , on_delete = models.CASCADE , related_name = 'product-lab' ) 
    
    class Type( models.TextChoices ) :
        TABLET = 'Tablet' , 'TABLET' 
        SYRUP = 'Syrup' , 'SYRUP' 
        CREAM = 'Cream' , 'CREAM' 
        SANITIZER = 'Sanitizer' , 'SANITIZER' 
        OTHER = 'Other' , 'OTHER' 

    type = models.CharField( choices = Type.choices , max_length = 20 ) 
    man_price = models.DecimalField( decimal_places = 3 ) 
    sell_price = models.DecimalField( decimal_places = 3 ) 
    code = models.CharField( max_length = 30 )
    
    def save( self , *args , **kwargs ) :
        if not self.code :
            time_part = timezone.now().strftime( "%H%M%S" ) 
            date_part = timezone.now().strftime( "%d%m%Y" )
            self.code = f'{ time_part }{ date_part }' 
        super.save( *args , **kwargs ) 

    def __str__( self ) :  
        return f'{ self.name } + ( { self.manufacturing_lab } )'


    
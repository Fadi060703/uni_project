from django.db import models

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
    


      
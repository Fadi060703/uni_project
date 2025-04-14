from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import AbstractUser , Group
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseUser( AbstractUser ) : # ThE Base User : 4 Different users will inherit
    username = None 
    email = models.EmailField( _( 'Email') , unique = True )
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    class Meta :
        verbose_name = 'Base User'
        verbose_name_plural = 'Base Users'

    def __str__( self ) :
        return f'{ self.email }' 

class Admin( BaseUser ) :
    class Meta :
        proxy = True 
        verbose_name = 'Admin' 
        verbose_name_plural = 'Admins' 
    
    def save( self , *args , **kwargs ) :
        self.is_staff = True 
        self.is_superuser = True 
        super().save( *args , **kwargs ) 
        admin_group , _ = Group.objects.get_or_create( 'Admin' ) 
        self.groups.add( admin_group ) 

class Manager( BaseUser ) :
    class Meta : 
        verbose_name = 'Manager' 
        verbose_name_plural = 'Managers' 
    
    def save( self , *args , **kwargs ) :
        super().save( *args , **kwargs ) 
        manager_group , _ = Group.objects.get_or_create( 'Manager' ) 
        self.groups.add( manager_group ) 

class Accountant( BaseUser ) :
    class Meta : 
        verbose_name = 'Accountant' 
        verbose_name_plural = 'Accountants' 

    def save( self , *args , **kwargs ) :
        super().save( *args , **kwargs ) 
        acc_group , _ = Group.objects.get_or_create( 'Accountant' ) 
        self.groups.add( acc_group ) 

class Salesman( BaseUser ) :
    class Meta :
        verbose_name = 'Salesman' 
        verbose_name_plural = 'Salesmen' 
    
    def save( self , *args , **kwargs ) :
        super().save( *args , **kwargs ) 
        sales_group , _ = Group.objects.get_or_create( 'Sales' ) 
        self.groups.add( sales_group ) 

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
    manufacturing_lab = models.ForeignKey( Lab , on_delete = models.CASCADE , related_name = 'product_lab' ) 
    
    class Type( models.TextChoices ) :
        TABLET = 'Tablet' , 'TABLET' 
        SYRUP = 'Syrup' , 'SYRUP' 
        CREAM = 'Cream' , 'CREAM' 
        SANITIZER = 'Sanitizer' , 'SANITIZER' 
        OTHER = 'Other' , 'OTHER' 

    type = models.CharField( choices = Type.choices , max_length = 20 ) 
    man_price = models.DecimalField( decimal_places = 3 , max_digits = 7 ) 
    sell_price = models.DecimalField( decimal_places = 3 , max_digits = 7 )  
    code = models.CharField( max_length = 30 , blank = True )
    
    def save( self , *args , **kwargs ) :
        if not self.code :
            letter = self.manufacturing_lab.name[ 0 ] 
            time_part = timezone.now().strftime( "%H%M%S" ) 
            date_part = timezone.now().strftime( "%d%m%Y" )
            self.code = f'{ letter }-{ time_part }{ date_part }' 
        super().save( *args , **kwargs )

    def __str__( self ) :  
        return f'{ self.name } + ( { self.manufacturing_lab } )'
    

from rest_framework.permissions import BasePermission 

class IsInGroup( BasePermission ) :
    def __init__( self , group_name ) :
        self.group_name = group_name 

    def has_permission( self , request , view ) :
        return request.user.groups.filter( name = self.group_name ).exists() 
    
class IsInMultipleGroups( BasePermission ) :
    def __init__( self , group_names ) :
        self.group_names = group_names 

    def has_permission( self , request , view ) :
        return request.user.groups.filter( name__in = self.group_names ).exists()  
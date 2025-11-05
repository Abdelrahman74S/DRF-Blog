from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from rest_framework import permissions
from accounts.models import Profile

User = get_user_model()

class IsOwner(BasePermission):
 
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'author'):

            try:
                return obj.author == request.user.profile
            except Profile.DoesNotExist:
                return False
        
        return False
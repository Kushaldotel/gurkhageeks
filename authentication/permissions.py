from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsDeveloper(BasePermission):

    def has_permission(self,request,view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.user_type != 'developer':
            raise PermissionDenied('User is not a developer')


class IsOrganization(BasePermission):

    def has_permission(self,request,view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.user_type != 'organization':
            raise PermissionDenied('User is not an organization')


class IsStaff(BasePermission):

    def has_permission(self,request,view):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.user_type != 'staff':
            raise PermissionDenied('User is not a staff')
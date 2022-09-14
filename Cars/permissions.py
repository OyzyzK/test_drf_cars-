from rest_framework import permissions
admin_token = 'd2312ihfojh12307y07yfh1234fadw2t'

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method =='GET':
            return True
        token = request.META.get('HTTP_AUTHORIZATION', b'')
        return token == admin_token

class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.method =='GET':
            return True
        token = request.META.get('HTTP_AUTHORIZATION', b'')
        return token == admin_token
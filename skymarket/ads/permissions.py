from rest_framework import permissions
from django.http import Http404
from skymarket.ads.models import Comment, Ad
from skymarket.users.models import User


class CommentUpdatePermission(permissions.BasePermission):
    message = 'Managing other selection not permitted'

    def has_permission(self, request, view):
        try:
            entity = Comment.objects.get(pk=view.kwarks["pk"])
        except Comment.DoesNotExist:
            raise Http404

        if entity.author_id == request.user.id:
            return True
        return False


class AdUpdatePermission(permissions.BasePermission):
    message = 'Managing other ads not permitted'

    def has_permission(self, request, view):
        if request.user.role in [User.ADMIN, User.USER]:
            return True

        try:
            entity = Ad.objects.get(pk=view.kwarks["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if entity.author_id == request.user.id:
            return True
        return False
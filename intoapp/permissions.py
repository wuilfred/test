from rest_framework import permissions
from rest_framework import serializers
from .models import SaveTicketEvent


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveTicketEvent
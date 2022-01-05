from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from ..serializers.idea import IdeaSerializer
from ..models.idea import Idea

class IdeasView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        idea = IdeaSerializer(data=request.data)
        if idea.is_valid():
            idea.save()
            return Response(idea.data, status=status.HTTP_201_CREATED)
        else:
            return Response(idea.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        # filter for ideas with our user id
        ideas = Idea.objects.filter(owner=request.user.id)
        data = IdeaSerializer(ideas, many=True).data
        return Response(data)


class IdeaView(APIView):
    def delete(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)
        # Check the idea's owner against the user making this request
        if request.user != idea.owner:
            raise PermissionDenied('Unauthorized, you do not own this idea')
        idea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)
        if request.user != idea.owner:
            raise PermissionDenied('Unauthorized, you do not own this idea')
        data = IdeaSerializer(idea).data
        return Response(data)
    
    def patch(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)
        # Check the idea's owner against the user making this request
        if request.user != idea.owner:
            raise PermissionDenied('Unauthorized, you do not own this idea')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_idea = IdeaSerializer(idea, data=request.data)
        if updated_idea.is_valid():
            updated_idea.save()
            return Response(updated_idea.data)
        return Response(updated_idea.errors, status=status.HTTP_400_BAD_REQUEST)    
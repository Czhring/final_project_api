from rest_framework import serializers
from ..models.idea import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'title','content', 'owner')
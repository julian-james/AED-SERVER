from rest_framework import serializers
from .models import Defib

class DefibSerializer(serializers.ModelSerializer):

    class Meta:
        model = Defib
        fields = ('id', 'address', 'post_code',   'long', 'lat', 'what3words_link', 'photo_url', 'time_taken', 'access', 'approved', 'comments', 'user_id')
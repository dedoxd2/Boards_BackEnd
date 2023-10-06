from rest_framework import serializers
from .models import *


class BoardSerializer (serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'


class TopicSerializer (serializers.ModelSerializer):
    boards = BoardSerializer(many=True, read_only=True)
    board_name = serializers.CharField(source='board.name', required=False)
    creater_name = serializers.CharField(
        source='created_by.username', required=False)

    class Meta:
        model = Topic
        fields = '__all__'


class PostSerializer (serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

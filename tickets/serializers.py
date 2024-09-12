from rest_framework import serializers
from .models import Ticket, Comment

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'asunto', 'descripcion', 'estado', 'fecha_creacion', 'cliente', 'soporte']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'ticket', 'usuario', 'contenido']
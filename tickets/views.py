from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket, Comment
from .serializers import TicketSerializer, CommentSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Bienvenido a Ticket System</h1>')


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket, Comment
from .serializers import TicketSerializer, CommentSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

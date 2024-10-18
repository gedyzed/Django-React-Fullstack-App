from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerialezer,NotesSerializers
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Notes


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerialezer
    permission_classes=[AllowAny]
    
class CreateNoteList(generics.ListCreateAPIView):
    serializer_class=NotesSerializers
    permission_classes=[IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)        
        return 
class DeleteNote(generics.CreateAPIView):
        serializer_class=NotesSerializers  
        permission_classes=[IsAuthenticated]  
        
        def get_queryset(self):
            user = self.request.user
            return Notes.objects.filter(author=user)
     

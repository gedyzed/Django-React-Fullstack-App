from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.CreateNoteList.as_view(),name='note_list'),
    path('notes/delete/<str:pk>/',views.DeleteNote.as_view(),name='delete_note'),
] 
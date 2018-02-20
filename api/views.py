from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import NoteSerializer,FBUserSerializer,FBUserDetailsSerializer,NoteDetailSerializer,FBUserNoteDetailsSerializer
from note.models import Note
from fbuser.models import FBUser

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'fbusers': reverse('fbuser_list', request=request, format=format),
        'notes': reverse('note_list', request=request, format=format),

    })

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save()

class FBUserList(generics.ListCreateAPIView):
    queryset = FBUser.objects.all()
    serializer_class = FBUserSerializer

    def perform_create(self, serializer):
        serializer.save()

class FBUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FBUser.objects.all()
    serializer_class = FBUserDetailsSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteDetailSerializer

class FBUserNoteDetail(generics.RetrieveAPIView):
    queryset = FBUser.objects.all()
    serializer_class = FBUserNoteDetailsSerializer


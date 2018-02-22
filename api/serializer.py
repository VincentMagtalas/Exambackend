from rest_framework import serializers

from note.models import Note
from fbuser.models import FBUser

class NoteSerializer(serializers.ModelSerializer):
    URL = serializers.HyperlinkedIdentityField(view_name='note_detail', format='html')
    class Meta:
        model = Note
        fields = ('URL','FBID','NoteTitle','NoteContent','DateCreated','Status')

class NoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('FBID','NoteTitle','NoteContent','DateCreated','Status')

class FBUserSerializer(serializers.ModelSerializer):
    DetailURL = serializers.HyperlinkedIdentityField(view_name='fbuser_detail', format='html')
    NotesURL = serializers.HyperlinkedIdentityField(view_name='fbuser_note', format='html')
    class Meta:
        model = FBUser
        fields = ('DetailURL','NotesURL','id','FBID','Name','Email','DateRegistered')

class FBUserDetailsSerializer(serializers.ModelSerializer):
    NotesURL = serializers.HyperlinkedIdentityField(view_name='fbuser_note', format='html')
    class Meta:
        model = FBUser
        fields = ('NotesURL','id','FBID','Name','Email','DateRegistered')

class FBUserNoteDetailsSerializer(serializers.ModelSerializer):
    Notes = NoteSerializer(many=True, read_only=True)
    class Meta:
        model = FBUser
        fields = ('id','FBID','Name','Notes')


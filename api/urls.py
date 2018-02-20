from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/$', views.api_root),
    url(r'^api/notes/$', views.NoteList.as_view(), name='note_list'),
    url(r'^api/fbusers/$', views.FBUserList.as_view(), name='fbuser_list'),
    url(r'^api/fbuser/(?P<pk>[0-9]+)/$', views.FBUserDetail.as_view(), name='fbuser_detail'),
    url(r'^api/note/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view(), name='note_detail'),
    url(r'^api/fbusernotes/(?P<pk>[0-9]+)/$', views.FBUserNoteDetail.as_view(), name='fbuser_note'),
]
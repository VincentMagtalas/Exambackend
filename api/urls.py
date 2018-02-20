from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^notes/$', views.NoteList.as_view(), name='note_list'),
    url(r'^fbusers/$', views.FBUserList.as_view(), name='fbuser_list'),
    url(r'^fbuser/(?P<pk>[0-9]+)/$', views.FBUserDetail.as_view(), name='fbuser_detail'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view(), name='note_detail'),
    url(r'^fbusernotes/(?P<pk>[0-9]+)/$', views.FBUserNoteDetail.as_view(), name='fbuser_note'),
]
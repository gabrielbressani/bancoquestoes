from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from questoes.api import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),

    url(r'^objetivas/$', views.QuestaoObjetivaList.as_view(), name='objetivas-list'),
    url(r'^objetivas/(?P<pk>[0-9]+)/$', views.QuestaoObjetivaDetailView.as_view(), name='objetivas-detail'),
    url(r'^discursivas/$', views.QuestaoDiscursivaList.as_view(), name='discursivas-list'),
    url(r'^discursivas/(?P<pk>[0-9]+)/$', views.QuestaoDiscursivaDetailView.as_view(), name='discursivas-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

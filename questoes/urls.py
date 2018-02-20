from django.conf.urls import url

from questoes import views

urlpatterns = [
    url(r'^$', views.ListQuestoes.as_view(), name='questoes-list'),

    url(r'objetiva/add/$', views.CreateResposta.as_view(), name='add-objetiva'),
    url(r'objetiva/(?P<pk>[0-9]+)/$', views.UpdateResposta.as_view(), name='update-objetiva'),
    url(r'objetiva/(?P<pk>[0-9]+)/delete/$', views.DeleteQuestaoObjetiva.as_view(), name='delete-objetiva'),

    url(r'discursiva/add/$', views.CreateRespostaDiscursiva.as_view(), name='add-discursiva'),
    url(r'discursiva/(?P<pk>[0-9]+)/$', views.UpdateRespostaDiscursiva.as_view(), name='update-discursiva'),
    url(r'discursiva/(?P<pk>[0-9]+)/delete/$', views.DeleteQuestaoDiscursiva.as_view(), name='delete-discursiva'),
]

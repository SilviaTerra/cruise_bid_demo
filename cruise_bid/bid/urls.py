from django.conf.urls import url

from . import views
app_name = 'bid'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /bids/1/
    url(r'^(?P<cruise_id>[0-9]+)/$', views.placeBid, name='placeBid'),
    url(r'^submit/$', views.submitCruise, name='submitCruise')
]
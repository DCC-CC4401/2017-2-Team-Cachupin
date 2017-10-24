from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.landing_page, name='landing'),
    # ex: /animals/5/
    url(r'^animals/(?P<animal_id>[0-9]+)/$', views.animal_record, name='animal_record'),
    # ex: /complaints
    url(r'^complaints$', views.complaint_record, name='complaint_record_no_param'),
    # ex: /complaints/5/
    url(r'^complaints/(?P<complaint_id>[0-9]+)/$', views.complaint_record, name='complaint_record'),
    # ex: /municipality/5/
    url(r'^municipalities/(?P<municipality_id>[0-9]+)/$', views.municipality_record, name='municipality_record'),
    # login
    url(r'^login/$', views.login, name='login'),
    # register
    url(r'^register/$', views.register, name='register'),
]
# image/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views_admin

urlpatterns = [
    url(r'^cache_images_locally_for_all_voters/$', views_admin.cache_images_locally_for_all_voters_view,
        name='cache_images_locally_for_all_voters'),
    url(r'^(?P<voter_id>[0-9]+)/create_resized_images_for_all_voters/$',
        views_admin.create_resized_images_for_all_voters_view, name='create_resized_images_for_all_voters')

]

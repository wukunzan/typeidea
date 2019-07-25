
from django.conf.urls import url
from django.contrib import admin

from typeidea.custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView,
)
from config.views import links





urlpatterns = [
	url(r'^$',IndexView.as_view(),name='index'),
	url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category-list'),
	url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag-list'),
	url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post-detail'),
	url(r'^links/$',links,name='links'),

    # url(r'^super_admin/',admin.site.urls),
    url(r'^admin/',admin.site.urls),
]

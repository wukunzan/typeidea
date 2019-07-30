import xadmin

from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from typeidea.custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView,SearchView,AuthorView,
)
from config.views import LinkListView
from comment.views import CommentView
from .autocomplete import CategoryAutocomplete, TagAutocomplete





urlpatterns = [
	url(r'^$',IndexView.as_view(),name='index'),
	url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(),name='category-list'),
	url(r'^tag/(?P<tag_id>\d+)/$',TagView.as_view(),name='tag-list'),
	url(r'^post/(?P<post_id>\d+).html$',PostDetailView.as_view(),name='post-detail'),
	url(r'^links/$', LinkListView.as_view(), name='links'),
	url(r'^search/$',SearchView.as_view(),name='search'),
	url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
	url(r'^comment/$', CommentView.as_view(), name='comment'),
	url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^super_admin/',admin.site.urls),
    url(r'^admin/',xadmin.site.urls,name='xadmin'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

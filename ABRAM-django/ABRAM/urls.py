from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ABRAM.views.home', name='home'),
    # url(r'^ABRAM/', include('ABRAM.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^posts/post$', 'posts.views.create_thread'),
	url(r'^posts/$', 'posts.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
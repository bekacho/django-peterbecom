from django import http
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'peterbecom.views.home', name='home'),
    # url(r'^peterbecom/', include('peterbecom.foo.urls')),
    url(r'^plog/', include('apps.plog.urls')),
    url(r'^plog$', lambda x: http.HttpResponseRedirect('/plog/')),
    url(r'', include('apps.homepage.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += staticfiles_urlpatterns()


import djcelery
djcelery.setup_loader()

#import logging
#from django.conf import settings
#from django.contrib.sites.models import Site
#site = Site.objects.get(pk=settings.SITE_ID)
#if site.domain == 'example.com':
#    logging.critical("Using unconfigured Site domain: %s" % site.domain)
#else:
#    logging.info("Using Site domain: %s" % site.domain)


import jingo
from compressor.contrib.jinja2ext import CompressorExtension
jingo.env.add_extension(CompressorExtension)

from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'IoTSSG.views.landing', name='landing'),
    url(r'^$', 'IoTSSG.views.home', name='home'),

    url(r'^login/$', 'IoTSSG.views.the_gate', name='login'),

    url(r'^programs/$', 'IoTSSG.views.program_list',name='program_list'),
    url(r'^programs/retrieve/$','IoTSSG.views.retrieve_programs',name='retrieve_programs'),
    url(r'^programs/(?P<program_name>\w+)/$', 'IoTSSG.views.program', name='program'),
    url(r'^meeting/$', 'IoTSSG.views.meeting', name='meeting'),
    url(r'^roster/$', 'IoTSSG.views.roster', name='roster'),
    url(r'^community/', 'IoTSSG.views.community', name='community'),
    url(r'^analytics/', 'IoTSSG.views.analytics', name='analytics'),
    url(r'^about/', 'IoTSSG.views.about', name='about'),
    url(r'^log_out/', 'IoTSSG.views.log_out', name='log_out'),
    # url(r'^IoTSSG/', include('IoTSSG.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root':settings.STATIC_ROOT}),
		)
"""
Definition of urls for Mcloud4.
"""

from datetime import datetime
from django.conf.urls import patterns, url,include
from app.forms import BootstrapAuthenticationForm
from django.contrib import admin

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name='home'),
    #url(r'^contact$', 'app.views.contact', name='contact'),
    #url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }

        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^T1_input/$', 'app.views.T1_input', name='T1_input'),
    url(r'^T1_result/$', 'app.views.T1_result', name='T1_result'),
    url(r'^T1LL_input/$', 'app.views.T1LL_input', name='T1LL_input'),
    url(r'^T1LL_result/$', 'app.views.T1LL_result', name='T1LL_result'),
    url(r'^AHA17_input/$', 'app.views.AHA17_input' ,name='AHA17_input'),
    url(r'^AHA17_result/', 'app.views.AHA17_result',name='AHA17_result'),
    url(r'^T2_input/$', 'app.views.T2_input' ,name='T2_input'),
    url(r'^T2_result/$', 'app.views.T2_result' ,name='T2_result'),
	url(r'^perfusion_input/$', 'app.views.perfusion_input' ,name='perfusion_input'),
    url(r'^perfusion_result/$', 'app.views.perfusion_result' ,name='perfusion_result'),
    url(r'^fcmat_result/$', 'app.views.fcmat_result' ,name='fcmat_result'),
    url(r'^fcmat_input/$', 'app.views.fcmat_input' ,name='fcmat_input'),
    url(r'^list_MRAPP/$', 'app.views.list_MRAPP' ,name='list_MRAPP'),
    #url(r'^MRAPP/(\d)/$', 'app.views.MRAPP' ,name='MRAPP'),
    url(r'^MRAPP/', include('fileupload.urls')),
    #url(r'^MRAPP/', 'app.views.list_MRAPP'),
    #url(r'^MRAPP/(\d)/$', 'fileupload.views.PictureCreateView.as_view()', name='upload-new'),





    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)


from os.path import join, abspath, dirname
urlpatterns += patterns('',
    (r'^result/(.*)$', 'django.views.static.serve', {'document_root': join(abspath(dirname(__file__)), 'result')}),
)
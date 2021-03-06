"""
Definition of urls for lab2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^products', app.views.products, name='products'),
    url(r'^product/([0-9]+)$', app.views.product),
    url(r'^users', app.views.users, name='users'), 
    url(r'^product/$', app.views.addProduct, name='addProduct'),
    url(r'^product/get/([0-9]+)$', app.views.getProduct, name='getProduct'),
    url(r'^product/edit/([0-9]+)$', app.views.editProduct, name='editProduct'),
    url(r'^product/delete/([0-9]+)$', app.views.deleteProduct, name='deleteProduct'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

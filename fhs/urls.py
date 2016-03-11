from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
        url(r'^$', views.index, name="index"),
        url(r'^register/$', views.register, name="register"),
        url(r'^login/$', views.user_login, name="login"),
        url(r'^logout/$', views.user_logout, name="logout"),
        url(r'^about/$', views.about, name="about"),
        url(r'^privacy-policy/$', views.privacy, name="privacy"),
        url(r'^terms-of-use/$', views.terms, name="terms"),
        url(r'^search/', views.search, name='search'),
        )
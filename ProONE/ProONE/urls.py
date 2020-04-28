from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from proapp import views
from django.views.static import serve
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$', views.success_view),
    url(r'^reg/',views.registration_view),
    url(r'^login/', views.login_view),
    url(r'^user/', views.success_view),
    url(r'^member/',views.member),
    url(r'^story/',views.storypad),
    url(r'^feed/',views.feedback),
    url(r'^cmt/',views.cmt),
    url(r'^logout/', views.link),
    url(r'^home/', views.home),
    url(r'^rst/', views.reset),
    url(r'^update/', views.update),
    url(r'^fgt/', views.forget),
]

if settings.DEBUG:
    urlpatterns+=[
        url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),

    ]

from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('signup',views.signupuser, name='signup'),
    path('login1', views.loginuser, name='login1'),
    path('mira-bhy',views.bhyhosp, name="hospitalpage1"),
    path('vasai', views.vasaihosp, name="hospitalpage2"),
    path('logout',views.logoutuser,name="logoutuser"),
    path('sortnamebhy', views.sortbynamebhy, name='sortnamebhy'),
    path('sortnamevasi',views.sortbynamevasai,name='sortnamevasi'),
    path('sortdisbhy',views.sortbydisbhy,name='sortdisbhy'),
    path('sortdisvasi',views.sortbydisvasai,name='sortdisvasi'),
    path('appoint', views.appoint, name='appoint'),
    path('vaccinelist', views.vaccinelist, name='vaccinelist'),
    path('vaccinemain', views.vaccinemain, name='vaccinemain'),
    path('success', views.success, name='success'),
    path('sortbyprice', views.sortbyprice, name='sortbyprice'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('urapp', views.urapp, name='urapp')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

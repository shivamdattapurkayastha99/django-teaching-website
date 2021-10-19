
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from teachproj.settings import MEDIA_ROOT,MEDIA_URL

urlpatterns = [
    
    path('',views.home,name='home' ),
    path('course/<str:slug>',views.coursepage,name='coursepage' ),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
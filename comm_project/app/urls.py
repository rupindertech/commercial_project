from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index")
    #path("<str:link_slug>",views.default),
    #path("<str:mycategory>",views.cate),

]

#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) 
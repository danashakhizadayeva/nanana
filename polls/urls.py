from django.urls import path

from . import views
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include



urlpatterns = [
    path('', views.index, name='polls-index'),
    path('about/', views.about, name='polls-about'),
    path('index/byhand/', views.byhand, name='polls-byhand'),
    path('index/bytyping/', views.bytyping, name='polls-bytyping'),
    path('database/', views.database, name='polls-database'),
#    path('videos/', views.showvideo, name='polls-videos'),
#    path('index/recordVideo/', views.recordVideo, name='polls-recordVideo'),
#    path('add_movie_form_submission/', views.add_movie_form_submission, name='polls-add_movie_form_submission'),
    path('i/', views.i, name='polls-i'),
    path('mymytext/', views.mymytext, name='polls-mymytext'),
    path('video_access/', views.video_access, name='polls-video_access'),
    path('image_access/', views.image_access, name='polls-image_access'),
    path('checkresults/', views.checkresults, name='polls-checkresults'),
    path('accounts/', include('django.contrib.auth.urls')),
]  

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
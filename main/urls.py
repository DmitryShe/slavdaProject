from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about, name='about'),
    path('hotels', views.about, name='hotels'),
    path('test', views.test, name='test'),
    path('hotels/<int:hotel_id>/', views.hotelPage),
    path('hotel_card', views.hotelPage, name='hotels'),
    path('news', views.news, name='news'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
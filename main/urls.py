from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news),
    path('news/<int:news_id>', views.newsPage, name='news-page'),
    path('hotels', views.hotels),
    path('hotels/<int:hotel_id>/', views.hotelPage, name='hotel-page'),
    #path('about-us', views.about, name='about'),
    #path('hotels', views.about, name='hotels'),
    path('test', views.AjaxHandler.as_view()),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
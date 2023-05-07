from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('hotels', views.hotels),
    path('hotels/<int:hotel_id>/', views.hotelPage, name='hotel_page'),
    #path('about-us', views.about, name='about'),
    #path('hotels', views.about, name='hotels'),
    path('test', views.AjaxHandler.as_view()),
    #path('404/', views.page_not_found_view),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
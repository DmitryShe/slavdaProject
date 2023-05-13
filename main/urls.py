from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('hotels', views.HotelsView.as_view(), name='hotels'),
    path('hotels/<int:pk>/', views.HotelPageView.as_view(), name='hotel_page'),
    path('foods', views.FoodView.as_view(), name='foods'),
    path('foods/<int:pk>/', views.HotelPageView.as_view(), name='food'),
    path('contacts/', views.CotactsView.as_view(), name='contacts'),
    path('test', views.AjaxHandler.as_view()),
    
    re_path(r'^froala_editor/', include('froala_editor.urls'))
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
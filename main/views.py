from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Q
from django.views.generic import View
from django.views import generic

from .models import Hotels
from .models import News
from .models import HotelsGallery
from .models import PlacementType
from .models import CiteInformations

from .forms import HotelsFilterForm

from random import randint


def index(request):
    news = News.objects.all()
    hotels = Hotels.objects.all()
    context = {
        'news': news,
        'hotels': hotels,
    }
    return render(request, 'main/index.html', context)

# hotels pages



class HotelsView(generic.ListView):
    model = Hotels
    template_name = 'main/hotels.html'
    context_object_name = 'hotels'
    paginate_by = 12

    @staticmethod
    def filter_options():
        return PlacementType.objects.all()
    


class HotelPageView(generic.DetailView):
    model = Hotels
    template_name = 'main/_hotel_card.html'

# news pages
class NewsListView(generic.ListView):
    model = News
    template_name = "main/news.html"
    paginate_by = 2

class NewsDetailView(generic.DetailView):
    model = News
    template_name = "main/_news_card.html"
    context_object_name = 'news_detail'

class CotactsView(generic.ListView):
    model = CiteInformations
    template_name = "main/contacts.html"
    context_object_name = 'contacts'


# hotels function
'''
def hotels(request):
    hotels = Hotels.objects.all()
    
    context = {
        'hotels': hotels
    }
    return render(request, 'main/hotels.html', context)

def hotelPage(request, hotel_id):
    try:
        hotel = Hotels.objects.get(id = hotel_id)
        context = {
            'hotel': hotel,
        }
    except Hotels.DoesNotExist:
        raise Http404('does not exist')
    return render(request, 'main/_hotel_card.html', context)

'''
def test(request):
    return render(request, 'main/__test.html')

def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)

'''
def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'main/news.html', context)

def newsPage(request, news_id):
    news = News.objects.get(id = news_id)
    #news = get_object_or_404(News, id=id)
    context = {
        'news': news
    }
    return render(request, 'main/_news_card.html', context)
'''

class AjaxHandler(View):

    def get(self, request):
        
        news = News.objects.all()
        d = dict()
        for e in news:
           
            d[e.id] = e.description
            print(d)

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            number = randint(1, 10)
            return JsonResponse(d)
        return render(request, 'main/__test.html')
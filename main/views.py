from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import View
from django.views import generic

from .models import Hotels
from .models import News
from .models import HotelsGallery

from random import randint


def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)

def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'main/index.html', context)

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




def test(request):
    return render(request, 'main/__test.html')



# news functions
class NewsListView(generic.ListView):
    model = News
    template_name = "main/news.html"

class NewsDetailView(generic.DetailView):
    model = News
    template_name = "main/_news_card.html"


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
# hotels function
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

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View

from .models import Hotels
from .models import News

from random import randint


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

def footer(request):
    return render(request, 'main/_footer.html')

def hotelPage(request, hotel_id):
    hotel = Hotels.objects.get(id = hotel_id)
    context = {
        'hotel': hotel,
    }
    return render(request, 'main/_hotel_card.html', context)



def about(request):
    hotels = Hotels.objects.all()
    return render(request, 'main/hotels.html', 
                  {'title': 'maintitle',
                   'hotels': hotels,
                   })


# news functions
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

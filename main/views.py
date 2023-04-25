from django.shortcuts import render
from .models import Hotels
from .models import News


def test(request):
    return render(request, 'main/__test.html')

def index(request):
    return render(request, 'main/index.html')

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
    item = News.objects.all()
    context = {
        'news': item
    }
    return render(request, 'main/news.html', context)

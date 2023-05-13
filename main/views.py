from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Q
from django.views.generic import View
from django.views import generic

from .models import Hotels
from .models import News
from .models import FoodBusiness
from .models import PlacementType
from .models import KitchenType
from .models import FoodType
from .models import CiteInformations



def index(request):
    news = News.objects.all()
    hotels = Hotels.objects.all()
    foods = FoodBusiness.objects.all()
    context = {
        'news': news,
        'hotels': hotels,
        'foods': foods,
    }
    return render(request, 'main/index.html', context)

# hotels pages



class HotelsView(generic.ListView):
    model = Hotels
    template_name = 'main/hotels.html'
    context_object_name = 'hotels'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        k = 2000

        if (filter_a == None and filter_b == None) or (filter_a == 0 and filter_b == 0):
            return queryset
        
        if filter_a != None and filter_b == None:
            queryset = queryset.filter(placementType__typeOfPlacment=filter_a)
            return queryset
        
        if filter_a == '0' and filter_b:
            
            x = int(filter_b) - k
            if x < 0:
                queryset = queryset
            elif 0 <= int(filter_b) < 10001:
                queryset = queryset.filter(price__range=(x, filter_b))
            else:
                queryset = queryset.filter(price__range=(10001, 1000000))
            return queryset

        if filter_a and filter_b:
            x = int(filter_b) - k


            if x <= 0:
                queryset = queryset.filter(placementType__typeOfPlacment=filter_a)
            elif 1 <= x < 12000:
                queryset = queryset.filter(placementType__typeOfPlacment=filter_a, price__range=(x, filter_b))
            else:
                queryset = queryset.filter(placementType__typeOfPlacment=filter_a, price__range=(12000, 1000000))
            return queryset
        

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == 'GET':
            selected_value = self.request.GET.get('type')
            self.request.session['selected_type'] = selected_value
        else:
            selected_value = self.request.session.get('selected_type', None)

        context['selected_type'] = selected_value
        
        return context

    @staticmethod
    def filter_options():
        
        return PlacementType.objects.all()

class HotelPageView(generic.DetailView):
    model = Hotels
    context_object_name = 'hotel_page'
    template_name = 'main/_hotel_card.html'

# foods pages
class FoodView(generic.ListView):
    model = FoodBusiness
    template_name = "main/foods.html"
    context_object_name = "foods"
    paginate_by = 12

    @staticmethod
    def filter_options():
        return KitchenType.objects.all()
    
    @staticmethod
    def filter_food_options():
        return FoodType.objects.all()

# news pages
class NewsListView(generic.ListView):
    model = News
    template_name = "main/news.html"
    paginate_by = 6

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
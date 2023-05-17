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
from .models import Showplaces
from .models import PlacementType
from .models import KitchenType
from .models import FoodType
from .models import ShowplacesType
from .models import CiteInformations
from .models import Excursion
from .models import ExcursionType



def index(request):
    news = News.objects.all()
    hotels = Hotels.objects.all()
    foods = FoodBusiness.objects.all()
    looks = Showplaces.objects.all()
    context = {
        'news': news,
        'hotels': hotels,
        'foods': foods,
        'looks': looks,
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
        
        if filter_a is None or filter_a.strip() == '0':
            filter_a = False
        if filter_b is None or filter_b.strip() == '0':
            filter_b = False

        if (filter_a is True or filter_a) and (filter_b is True or filter_b):
            queryset = queryset.filter(placementType__typeOfPlacment=filter_a, price__range=(0, filter_b))
        elif (filter_a is True or filter_a) and filter_b is False:
            queryset = queryset.filter(placementType__typeOfPlacment=filter_a)
        elif filter_a is False and (filter_b is True or filter_b):
            queryset = queryset.filter(price__range=(0, filter_b))
        else:
            queryset = queryset
            
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

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        filter_c = self.request.GET.get('kitchen')

        if filter_a is None or filter_a.strip() == '0':
            filter_a = False
        if filter_b is None or filter_b.strip() == '0':
            filter_b = False
        if filter_c is None or filter_c.strip() == '0':
            filter_c = False


        if filter_a is False and filter_b is False and filter_c is False:
            queryset = queryset
            
        elif (filter_a is True or filter_a) and filter_b is False and filter_c is False:
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a)
            print(queryset)
            print('1')
        elif filter_a is False and (filter_b is True or filter_b) and filter_c is False:
            queryset = queryset.filter(price__range=(0, filter_b))
            print('2')
        elif filter_a is False and filter_b is False and (filter_c is True or filter_c):
            queryset = queryset.filter(foodType__typeOfFood=filter_c)
            print('3')
        elif (filter_a is True or filter_a) and (filter_b is True or filter_b) and filter_c is False:
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, price__range=(0, filter_b))
            print('4')
        elif (filter_a is True or filter_a) and filter_b is False and (filter_c is True or filter_c):
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, foodType__typeOfFood=filter_c)
            print('5')
        elif filter_a is False and (filter_b is True or filter_b) and (filter_c is True or filter_c):
            queryset = queryset.filter(price__range=(0, filter_b), foodType__typeOfFood=filter_c)
            print('6')
        elif (filter_a is True or filter_a) and (filter_b is True or filter_b) and (filter_c is True or filter_c):
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, price__range=(0, filter_b), foodType__typeOfFood=filter_c)
            print('7')
        else:
            print('8')
            queryset = queryset
        
        return queryset


    @staticmethod
    def filter_options():
        return KitchenType.objects.all()
    
    @staticmethod
    def filter_food_options():
        return FoodType.objects.all()

class FoodPageView(generic.DetailView):
    model = FoodBusiness
    context_object_name = 'food'
    template_name = 'main/_food_card.html'

# looks pages
class LookView(generic.ListView):
    model = Showplaces
    template_name = 'main/looks.html'
    context_object_name = 'looks'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        
        if filter_a is None or filter_a.strip() == '0':
            filter_a = False
        if filter_b is None or filter_b.strip() == '0':
            filter_b = False

        if (filter_a is True or filter_a) and (filter_b is True or filter_b):
            queryset = queryset.filter(showplacesType__typeOfLooks=filter_a, price__range=(0, filter_b))
        elif (filter_a is True or filter_a) and filter_b is False:
            queryset = queryset.filter(showplacesType__typeOfLooks=filter_a)
        elif filter_a is False and (filter_b is True or filter_b):
            queryset = queryset.filter(price__range=(0, filter_b))
        else:
            queryset = queryset

        return queryset


    @staticmethod
    def filter_options():
        return ShowplacesType.objects.all()
    
class LookPageView(generic.DetailView):
    model = Showplaces
    context_object_name = 'look'
    template_name = 'main/_look_card.html'

class ExcursionView(generic.ListView):
    model = Excursion
    context_object_name = 'excursions'
    template_name = 'main/excursion.html'
    paginate_by = 9

    @staticmethod
    def filter_options():
        return ExcursionType.objects.all()

class ExcursionPageView(generic.DetailView):
    model = Excursion
    template_name = 'main/_excursion_card.html'
    context_object_name = 'excursion'

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


class MyViewClass(generic.ListView):
    model = Hotels
    template_name = 'main/__test.html'
    context_object_name = 'test'

    '''
    def get(self, request):
        d = {
            'name': 'mark',
            'age': 52
        }
        return JsonResponse(d)
        return render(request, 'main/__test.html')
    '''

    def create_response(self, request, data):
        d = {
            'name': 'mark',
            'age': 52
        }
        return JsonResponse(d)



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
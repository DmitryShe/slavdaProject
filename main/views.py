from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponseBadRequest
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Q
from django.views.generic import View
from django.views import generic
from django.core import serializers
from django.utils.encoding import filepath_to_uri

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

    @staticmethod
    def filter_options():
        return PlacementType.objects.all()

    def get(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'GET':
                hotels = self.get_queryset().values("id", "title", "price", "placementType")
                hotelsDict = {}
                i = 0
                for hotel in hotels:
                    hotelsDict[i] = hotel
                    hotelsDict[i]["coordinates"] = {
                        'title': (Hotels.objects.get(id=hotelsDict[i]['id'])).coordinates.title,
                        'x': (Hotels.objects.get(id=hotelsDict[i]['id'])).coordinates.pointX,
                        'y': (Hotels.objects.get(id=hotelsDict[i]['id'])).coordinates.pointY,
                    }
                    hotelsDict[i]["placementType"] = (Hotels.objects.get(id=hotelsDict[i]['id'])).placementType.typeOfPlacment
                    hotelsDict[i]["imageUrl"] = '/media/' + filepath_to_uri((Hotels.objects.get(id=hotelsDict[i]['id'])).hotel_images.first().image)
                    hotelsDict[i]["pageLink"] = '/hotels/' + str(hotelsDict[i]['id'])
                    hotelsDict[i]["tags"] = list(Hotels.objects.get(id=hotelsDict[i]['id']).tags.values('title'))
                    i += 1

                print(hotelsDict)
                return JsonResponse(hotelsDict, safe=False)
            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            filter_options = PlacementType.objects.all()
            hotels = Hotels.objects.all()
            context = {
                'filter_options': filter_options,
                'hotels': hotels,
            }

            return render(request, 'main/hotels.html', context)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        
        if filter_a is None or filter_a.strip() == '0':
            filter_a = False

        if filter_b is None or filter_b.strip() == '0':
            filter_b = False
        else:
            a, b = [int(i) for i in filter_b.split('_')]
            #print('a', a, 'b', b)

        if (filter_a is True or filter_a) and (filter_b is True or filter_b):
            queryset = queryset.filter(placementType__typeOfPlacment=filter_a, price__range=(a, b))
        elif (filter_a is True or filter_a) and filter_b is False:
            queryset = queryset.filter(placementType__typeOfPlacment=filter_a)
        elif filter_a is False and (filter_b is True or filter_b):
            queryset = queryset.filter(price__range=(a, b))
        else:
            queryset = queryset
            
        return queryset
    
    

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

    def get(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'GET':
                foods = self.get_queryset().values("id", "title", "price", "kitchenType", "foodType")
                foodsDict = {}
                i = 0
                for food in foods:
                    foodsDict[i] = food
                    foodsDict[i]["coordinates"] = {
                        'title': (FoodBusiness.objects.get(id=foodsDict[i]['id'])).orgFoodCoord.title,
                        'x': (FoodBusiness.objects.get(id=foodsDict[i]['id'])).orgFoodCoord.pointX,
                        'y': (FoodBusiness.objects.get(id=foodsDict[i]['id'])).orgFoodCoord.pointY,
                    }
                    foodsDict[i]["kitchenType"] = (FoodBusiness.objects.get(id=foodsDict[i]['id'])).kitchenType.typeOfKitchen
                    foodsDict[i]["foodType"] = (FoodBusiness.objects.get(id=foodsDict[i]['id'])).foodType.typeOfFood
                    foodsDict[i]["imageUrl"] = '/media/' + filepath_to_uri((FoodBusiness.objects.get(id=foodsDict[i]['id'])).FoodBusiness_images.first().image)
                    foodsDict[i]["pageLink"] = '/foods/' + str(foodsDict[i]['id'])
                    foodsDict[i]["tags"] = list(FoodBusiness.objects.get(id=foodsDict[i]['id']).tags.values('title'))
                    i += 1

                print(foodsDict)
                return JsonResponse(foodsDict, safe=False)
            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            filter_options = KitchenType.objects.all()
            filter_food_options = FoodType.objects.all()
            foods = FoodBusiness.objects.all()
            context = {
                'filter_options': filter_options,
                'filter_food_options': filter_food_options,
                'foods': foods,
            }

            return render(request, 'main/foods.html', context)
    

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        filter_c = self.request.GET.get('kitchen')

        if filter_a is None or filter_a.strip() == '0':
            filter_a = False

        if filter_b is None or filter_b.strip() == '0':
            filter_b = False
        else:
            a, b = [int(i) for i in filter_b.split('_')]
            print('a', a, 'b', b)

        if filter_c is None or filter_c.strip() == '0':
            filter_c = False
        

        if filter_a is False and filter_b is False and filter_c is False:
            queryset = queryset
            
        elif (filter_a is True or filter_a) and filter_b is False and filter_c is False:
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a)
            print(queryset)
            print('1')
        elif filter_a is False and (filter_b is True or filter_b) and filter_c is False:
            queryset = queryset.filter(price__range=(a, b))
            print('2')
        elif filter_a is False and filter_b is False and (filter_c is True or filter_c):
            queryset = queryset.filter(foodType__typeOfFood=filter_c)
            print('3')
        elif (filter_a is True or filter_a) and (filter_b is True or filter_b) and filter_c is False:
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, price__range=(a, b))
            print('4')
        elif (filter_a is True or filter_a) and filter_b is False and (filter_c is True or filter_c):
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, foodType__typeOfFood=filter_c)
            print('5')
        elif filter_a is False and (filter_b is True or filter_b) and (filter_c is True or filter_c):
            queryset = queryset.filter(price__range=(a, b), foodType__typeOfFood=filter_c)
            print('6')
        elif (filter_a is True or filter_a) and (filter_b is True or filter_b) and (filter_c is True or filter_c):
            queryset = queryset.filter(kitchenType__typeOfKitchen=filter_a, price__range=(a, b), foodType__typeOfFood=filter_c)
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

    def get(self, request):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        if is_ajax:
            if request.method == 'GET':
                looks = self.get_queryset().values("id", "title", "price", "showplacesType")
                looksDict = {}
                i = 0
                for look in looks:
                    looksDict[i] = look
                    looksDict[i]["coordinates"] = {
                        'title': (Showplaces.objects.get(id=looksDict[i]['id'])).showPlacesCoord.title,
                        'x': (Showplaces.objects.get(id=looksDict[i]['id'])).showPlacesCoord.pointX,
                        'y': (Showplaces.objects.get(id=looksDict[i]['id'])).showPlacesCoord.pointY,
                    }
                    looksDict[i]["showplacesType"] = (Showplaces.objects.get(id=looksDict[i]['id'])).showplacesType.typeOfLooks
                    looksDict[i]["imageUrl"] = '/media/' + filepath_to_uri((Showplaces.objects.get(id=looksDict[i]['id'])).Showplaces_images.first().image)
                    looksDict[i]["pageLink"] = '/looks/' + str(looksDict[i]['id'])
                    looksDict[i]["tags"] = list(Showplaces.objects.get(id=looksDict[i]['id']).tags.values('title'))
                    i += 1

                print(looksDict)
                return JsonResponse(looksDict, safe=False)
            return JsonResponse({'status': 'Invalid request'}, status=400)
        else:
            filter_options = ShowplacesType.objects.all()
            looks = Showplaces.objects.all()
            context = {
                'filter_options': filter_options,
                'looks': looks,
            }

            return render(request, 'main/looks.html', context)


    def get_queryset(self):
        queryset = super().get_queryset()
        filter_a = self.request.GET.get('type') 
        filter_b = self.request.GET.get('price')
        
        if filter_a is None or filter_a.strip() == '0':
            filter_a = False

        if filter_b is None or filter_b.strip() == '0':
            filter_b = False
        else:
            a, b = [int(i) for i in filter_b.split('_')]
            print('a', a, 'b', b)

        if (filter_a is True or filter_a) and (filter_b is True or filter_b):
            queryset = queryset.filter(showplacesType__typeOfLooks=filter_a, price__range=(a, b))
        elif (filter_a is True or filter_a) and filter_b is False:
            queryset = queryset.filter(showplacesType__typeOfLooks=filter_a)
        elif filter_a is False and (filter_b is True or filter_b):
            queryset = queryset.filter(price__range=(a, b))
        else:
            queryset = queryset
            
        return queryset

    
class LookPageView(generic.DetailView):
    model = Showplaces
    context_object_name = 'look'
    template_name = 'main/_look_card.html'

class ExcursionView(generic.ListView):
    model = Excursion
    context_object_name = 'excursions'
    template_name = 'main/excursion.html'
    #paginate_by = 9

    @staticmethod
    def filter_options():
        return ExcursionType.objects.all()
    
    def get_unic_dict(self, dict1, dict2):
        # Найдем ключи, которые есть только в первом словаре
        unique_to_dict1 = set(dict1.keys()) - set(dict2.keys())

        # Создадим новый словарь, содержащий только уникальные элементы из первого словаря
        unique_dict1 = {k: dict1[k] for k in unique_to_dict1}

        # Выполним аналогичные операции для ключей, которые есть только во втором словаре
        unique_to_dict2 = set(dict2.keys()) - set(dict1.keys())
        unique_dict2 = {k: dict2[k] for k in unique_to_dict2}

        # Объединим два новых словаря в один
        unique_dict = {**unique_dict1, **unique_dict2}

        return unique_dict
    
    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.values())
        filters = self.request.GET.dict()
        temp_filter = {
            'hours': '0_0',
            'price_end': '',
            'price_start': ''
        }
        filters = temp_filter | filters

        # 1 filter
        a, b = [int(i) for i in filters['hours'].split('_')]
        if a != 0 and b != 0:
            queryset = queryset.filter(exDuration__range=(a, b))

        # 2 filter
        if filters['price_start'] == '':
            filters['price_start'] = 0
        if filters['price_end'] == '':
            filters['price_end'] = 0

            if int(filters['price_start']) > filters['price_end']:
                filters['price_end'] = 10000000000
        
        filter_c = int(filters['price_start']) 
        filter_d = int(filters['price_end'])

        if 0 < filter_d < 10000000000:
            queryset = queryset.filter(price__range=(filter_c, filter_d))

        # 3 filter
        # эта функция необходима чтобы получить другие поля фильтра, 
        # поскольку первые типы фильтров могут настраиваться пользователем,
        # и у нас может быть разное их количество
        # но они могут принимать значение On - Off
        unicfilter = self.get_unic_dict(temp_filter, filters)
        if unicfilter != {}:
            temparr = []
            for key in unicfilter.keys():
                temparr.append(key)

            queryset = queryset.filter(excursionType__typeOfexcursion__in=temparr)

        return queryset

class ExcursionPageView(generic.DetailView):
    model = Excursion
    template_name = 'main/_excursion_card.html'
    context_object_name = 'excursion'

# news pages
from datetime import datetime
class NewsListView(generic.ListView):
    model = News
    template_name = "main/news.html"
    #paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        news = self.request.GET.dict()

        if (news.get('start_date') is None and news.get('end_date') is None) or (news.get('start_date') == '' and news.get('end_date') == ''):
            return queryset
        print(news.get('start_date'), news.get('end_date'))

        if news.get('start_date') is None or news.get('start_date') == '':
            news['start_date'] = datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        if news.get('end_date') is None or news.get('end_date') == '':
            news['end_date'] = datetime.strptime('2100-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

        queryset = queryset.filter(date__range=(news['start_date'], news['end_date']))
        
        return queryset

class NewsDetailView(generic.DetailView):
    model = News
    template_name = "main/_news_card.html"
    context_object_name = 'news_detail'

class CotactsView(generic.ListView):
    model = CiteInformations
    template_name = "main/contacts.html"
    context_object_name = 'contacts'


# hotels function

def test(request):
    return render(request, 'main/__test.html')

def page_not_found_view(request, exception):
    return render(request, 'main/404.html', status=404)



        
    

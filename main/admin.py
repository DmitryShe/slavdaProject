from django.contrib import admin

from .models import PlacementType
from .models import ShowplacesType
from .models import KitchenType
from .models import OrganizationCoordinaties
from .models import HotelsGallery
from .models import FoodBusinessGallery
from .models import ShowplacesGallery
from .models import OrganizationGallery

from .models import News
from .models import Hotels
from .models import FoodBusiness
from .models import Showplaces
from .models import CiteInformations




admin.site.register(PlacementType)
admin.site.register(KitchenType)
admin.site.register(ShowplacesType)
admin.site.register(News)
admin.site.register(OrganizationCoordinaties)



class GalleryHotelInline(admin.TabularInline):
    fk_name = 'hotel'
    model = HotelsGallery

class GalleryFoodInline(admin.TabularInline):
    fk_name = 'foodBusiness'
    model = FoodBusinessGallery

class GalleryShowplacesInline(admin.TabularInline):
    fk_name = 'showplaces'
    model = ShowplacesGallery

class OrganizationGalleryInline(admin.TabularInline):
    fk_name = 'contacts'
    model = OrganizationGallery


@admin.register(Hotels)
class HotelAdmin(admin.ModelAdmin):
    inlines = [GalleryHotelInline,]

@admin.register(FoodBusiness)
class FoodAdmin(admin.ModelAdmin):
    inlines = [GalleryFoodInline, ]

@admin.register(Showplaces)
class ShoplacesAdmin(admin.ModelAdmin):
    inlines = [GalleryShowplacesInline, ]

@admin.register(CiteInformations)
class CiteInformationsAdmin(admin.ModelAdmin):
    inlines = [OrganizationGalleryInline, ]

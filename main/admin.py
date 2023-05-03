from django.contrib import admin
from .models import Hotels
from .models import News
from .models import PlacementType
from .models import HotelsGallery


admin.site.register(News)
admin.site.register(PlacementType)


class GalleryInline(admin.TabularInline):
    fk_name = 'hotel'
    model = HotelsGallery

@admin.register(Hotels)
class HotelAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
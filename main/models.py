from django.db import models

from froala_editor.fields import FroalaField


# # # # # # # # #
# справочники
# # # # # # # # #


# тип заведения: отель, гостиница...
class PlacementType(models.Model):
    typeOfPlacment = models.CharField('Тип заведения', max_length=100)

    def __str__(self):
        return self.typeOfPlacment
    
    class Meta:
        verbose_name = 'Формат отеля'
        verbose_name_plural = 'Формат отеля'

# тип заведения: столовая, бар...
class KitchenType(models.Model):
    typeOfKitchen = models.CharField('Тип кухни', max_length=100)

    def __str__(self):
        return self.typeOfKitchen
    
    class Meta:
        verbose_name = 'Формат общепита'
        verbose_name_plural = 'Формат общепита'

# тип кухни: суши, въетнамская, горячее, холодное и пр.
class FoodType(models.Model):
    typeOfFood = models.CharField('Вид еды', max_length=100)

    def __str__(self):
        return self.typeOfFood
    
    class Meta:
        verbose_name = 'Вид еды'
        verbose_name_plural = 'Вид еды'

# тип места которое можно посмотреть
class ShowplacesType(models.Model):
    typeOfLooks = models.CharField('Тип достопримечательности', max_length=100)

    def __str__(self):
        return self.typeOfLooks
    
    class Meta:
        verbose_name = 'Формат достопримечательности'
        verbose_name_plural = 'Формат достопримечательности'

# коориднаты организации, чтобы отметить ее на картах яндекса
class OrganizationCoordinaties(models.Model):
    title = models.CharField('Наименование', max_length=200)
    pointX = models.FloatField('X координата', blank=False, default=55.751574, help_text='Координата X для отображения предприятия на карте')
    pointY = models.FloatField('Y координата', blank=False, default=37.573856, help_text='Координата Y для отображения предприятия на карте')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Координаты предприятия'
        verbose_name_plural = 'Координаты предприятий'

class CiteTags(models.Model):
    title = models.CharField('Название тега', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг сайта'
        verbose_name_plural = 'Тэг сайта'


# вид экскурсии, пешая на машине, велосипед
class ExcursionType(models.Model):
    typeOfexcursion = models.CharField('Вид экскурсии', max_length=100)

    def __str__(self):
        return self.typeOfexcursion
    
    class Meta:
        verbose_name = 'Вид экскурсии'
        verbose_name_plural = 'Вид экскурсии'


# # # # # # # # #
# Модели
# # # # # # # # #


# модель для отелей, гостиниц и пр.
class Hotels(models.Model):
    title         = models.CharField('Название', max_length=200)
    isShowedInIndexPage = models.BooleanField('Показывать карточку организации на главной странице')
    address       = models.TextField('Адрес', max_length=250)
    contacts      = models.TextField('Контакты')
    link          = models.TextField('Ссылки на сайт', blank=False)
    workingHours  = models.TextField('Время работы', blank=False)
    price         = models.FloatField("Средний чек")
    coordinates   = models.ForeignKey(OrganizationCoordinaties, on_delete = models.SET_NULL, null=True, verbose_name="Координаты")
    placementType = models.ForeignKey(PlacementType, on_delete=models.SET_NULL, null=True, verbose_name="Заведение")
    description   = FroalaField()
    tags = models.ManyToManyField(CiteTags, null=True, verbose_name="Тэги", related_name='hotel_tags')
    
    
    def __str__(self):
        return self.title
    
    def getCoordinates(self):
        return self.coordinates
    
    class Meta:
        verbose_name = 'Отели'
        verbose_name_plural = 'Отели'

# модель для сохранения пути картинки для модели отелей
class HotelsGallery(models.Model):
    title = models.CharField('Наименование изображения', max_length=200)
    image = models.ImageField(upload_to='hotels_gallery')
    hotel = models.ForeignKey(Hotels, on_delete=models.SET_NULL, related_name='hotel_images', null=True)

    def getUrl(self):
        return self.image
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото из гостиниц'
        verbose_name_plural = 'Hotels Photo'

# модель для организаций по питанию
class FoodBusiness(models.Model):
    title         = models.CharField('Название', max_length=250)
    isShowedInIndexPage = models.BooleanField('Показывать карточку организации на главной странице')
    address       = models.TextField('Адрес', max_length=250)
    contacts      = models.TextField('Контакты')
    link          = models.TextField('Ссылки на сайт', blank=False)
    workingHours  = models.TextField('Время работы', blank=False)
    price         = models.IntegerField('Средний чек')
    orgFoodCoord  = models.ForeignKey(OrganizationCoordinaties, on_delete = models.SET_NULL, null=True)
    kitchenType   = models.ForeignKey(KitchenType, on_delete = models.SET_NULL, null=True)
    foodType      = models.ForeignKey(FoodType, on_delete = models.SET_NULL, null=True)
    description   = FroalaField()
    tags = models.ManyToManyField(CiteTags, null=True, verbose_name="Тэги")
    
    def __str__(self):
        return self.title
    
    def getCoordinates(self):
        return self.orgFoodCoord
    
    class Meta:
        verbose_name = 'Общепит'
        verbose_name_plural = 'Общепит'

# модель для сохранения пути картинки для модели общепита
class FoodBusinessGallery(models.Model):
    title = models.CharField('Наименование изображения', max_length=200)
    image = models.ImageField(upload_to='FoodBusiness_gallery/%Y/%m/%d/')
    foodBusiness = models.ForeignKey(FoodBusiness, on_delete=models.SET_NULL, related_name='FoodBusiness_images', null=True)

    def getUrl(self):
        return self.image
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото из общепита'
        verbose_name_plural = 'Фото из общепита'

# модель для достопримечательности
class Showplaces(models.Model):
    title            = models.CharField('Название', max_length=250)
    isShowedInIndexPage = models.BooleanField('Показывать карточку организации на главной странице')
    address          = models.TextField('Адрес', max_length=250)
    contacts         = models.TextField('Контакты')
    link             = models.TextField('Ссылки на сайт', blank=False)
    workingHours     = models.TextField('Время работы', blank=False)
    price            = models.IntegerField('Средний чек')
    showPlacesCoord  = models.ForeignKey(OrganizationCoordinaties, on_delete = models.SET_NULL, null=True)
    showplacesType   = models.ForeignKey(ShowplacesType, on_delete = models.SET_NULL, null=True)
    description      = FroalaField()
    tags = models.ManyToManyField(CiteTags, null=True, verbose_name="Тэги")
    
    def __str__(self):
        return self.title
    
    def getCoordinates(self):
        return self.showPlacesCoord

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'

# модель для сохранения пути картинки для модели достопримечательности
class ShowplacesGallery(models.Model):
    title = models.CharField('Наименование изображения', max_length=200)
    image = models.ImageField(upload_to='Showplaces_gallery/%Y/%m/%d/')
    showplaces = models.ForeignKey(Showplaces, on_delete=models.SET_NULL, related_name='Showplaces_images', null=True)

    def getUrl(self):
        return self.image
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото достопримечательности'
        verbose_name_plural = 'Фото достопримечательности'

# модель для экскурсии
class Excursion(models.Model):
    title = models.CharField('Название экскурсии', max_length=200)
    description = FroalaField()
    route = FroalaField()
    timeStart = models.CharField('Время начала экскурсии', max_length=20)
    exDuration = models.IntegerField('Продолжительность экскурсии')
    tourOperator = models.CharField('Организатор', max_length=100)
    link = models.CharField('Ссылка на экскурсию, организатора', max_length=100)
    price = models.IntegerField('Цена экскурсии')
    excursionType = models.ForeignKey(ExcursionType, on_delete = models.SET_NULL, null=True, verbose_name='вид экскурсии')
    routeCoordinaties = models.ManyToManyField(OrganizationCoordinaties, related_name='ex_route', verbose_name='экскурсия')
    tags = models.ManyToManyField(CiteTags, verbose_name="Тэги")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Экскурсии'
        verbose_name_plural = 'Экскурсии'

'''
class RouteCoordinates(models.Model):
    title = models.CharField('Название точки', max_length=40)
    routeX = models.FloatField('координата X')
    routeY = models.FloatField('координата Y')
    excursion = models.ForeignKey(Excursion, on_delete=models.SET_NULL, related_name='ex_route', null=True, verbose_name='экскурсия')
'''

class ExcursionGallery(models.Model):
    title = models.CharField('Наименование изображения', max_length=200)
    image = models.ImageField(upload_to='Excursion_gallery/%Y/%m/%d/')
    excursion = models.ForeignKey(Excursion, on_delete=models.SET_NULL, related_name='Excursion_images', null=True, verbose_name='фото')

    def getUrl(self):
        return self.image
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото экскурсии'
        verbose_name_plural = 'Фото экскурсии'

# новости
class News(models.Model):
    date = models.DateTimeField()
    title = models.TextField('Заголовок', max_length=100)
    description = FroalaField()
    #models.TextField('Описание', max_length=20000)
    
    newsImg = models.ImageField(upload_to='news')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

# 

class CiteInformations(models.Model):
    organizationTitle = FroalaField()
    organizationContacts = FroalaField()
    organizationDeveloper = FroalaField()
    organizationDeveloperImage = models.ImageField(upload_to='developer_img/%Y/%m/%d/')

    def getUrl(self):
        return self.organizationDeveloperImage

    def __str__(self):
        return 'Organization DB'

    class Meta:
        verbose_name = 'OrganizationDB'
        verbose_name_plural = 'OrganizationDB'




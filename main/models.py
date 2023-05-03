from django.db import models


class PlacementType(models.Model):
    typeOfInstitution = models.CharField('Тип заведения', max_length=100)

    def __str__(self):
        return self.typeOfInstitution
    
    class Meta:
        verbose_name = 'Placment type'
        verbose_name_plural = 'Placment type'

class Hotels(models.Model):
    title         = models.CharField('Название', max_length=200)
    description   = models.TextField('Описание')
    address       = models.TextField('Адрес', max_length=200)
    contacts      = models.TextField('Контакты')
    link          = models.TextField('Ссылки на сайт', blank=False)
    placementType = models.ForeignKey(PlacementType, on_delete=models.CASCADE)
    price         = models.FloatField("Средний чек")
    coordinates   = models.TextField("Координаты учреждения для яндекс карт")
    #hotelImg      = models.ImageField('Фотографии отеля', upload_to='hotels')
    #services      = models.TextField()
    #reviews       = models.TextField()
    #stars         = models.IntegerField()
    #isHear        = models.BooleanField(blank=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'

class HotelsGallery(models.Model):
    title = models.CharField('Наименование изображения', max_length=200)
    image = models.ImageField(upload_to='hotels_gallery')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='hotel_images')

    def getUrl(self):
        return self.image
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Фото из гостиниц'
        verbose_name_plural = 'Hotels Photo'








class News(models.Model):
    date = models.DateTimeField()
    title = models.TextField('Заголовок', max_length=100)
    description = models.TextField('Описание', max_length=2000)
    newsImg = models.ImageField(upload_to='news')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


from django.db import models

class Hotels(models.Model):
    title         = models.CharField('Название', max_length=50)
    address       = models.TextField('Адрес', max_length=200)
    contacts      = models.TextField('Контакты')
    description   = models.TextField()
    reviews       = models.TextField()
    services      = models.TextField()
    coordinates   = models.TextField()
    price         = models.FloatField()
    stars         = models.IntegerField()
    hotelImg      = models.ImageField(upload_to='hotels')
    #isHear        = models.BooleanField(blank=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'

class News(models.Model):
    title = models.TextField('Заголовок', max_length=100)
    description = models.TextField('Описание', max_length=2000)
    newsImg = models.ImageField(upload_to='news')
    date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
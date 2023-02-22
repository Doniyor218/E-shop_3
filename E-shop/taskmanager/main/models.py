
from django.db import models


class Task(models.Model):
    title = models.CharField('Наззвание', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар магазина'
        verbose_name_plural = 'Товары магазина'

class Resume(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length= 255, blank=False, null=False)
    file = models.FileField(upload_to= 'files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length= 255, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)

    def __str__ (self):
        return self.title
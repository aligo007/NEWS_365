
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(MPTTModel):

    title = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    image = models.ImageField(upload_to = 'category/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}'  

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория'

    class MPTTMeta:
        order_insertion_by = ['title']

    


class Post(models.Model): 

    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post/')
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField()  

    
    def __str__(self):
        return f'{self.title}'  

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'

    def publish(self):
        self.publish_date = timezone.now()
        self.save

    class MPTTMeta:
        order_insertion_by = ['title']



class Tags(models.Model):
    title = models.CharField(max_length=30)
    post = models.ManyToManyField(Post)



    def __str__(self):
        return f'{self.title}'  

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'

    class MPTTMeta:
        order_insertion_by = ['tags']
    


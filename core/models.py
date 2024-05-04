from django.db import models

# Create your models here.


class AbstractModel(models.Model):
    updated_date= models.DateTimeField(
        blank=True,
        auto_now=True,
    )
    created_date= models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
    class Meta:
         abstract=True





class GeneralSetting(AbstractModel):
    name =models.CharField(
        default='',
        max_length=254,
                blank=True,

    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    

class ImageSetting(AbstractModel):
        name =models.CharField(
        default='',
        max_length=254,
        blank=True,

    )
        description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        file=models.ImageField(
            default='',
            verbose_name='Image',
            blank=True,
            upload_to='images/'
    )
        
class ProductImageSetting(AbstractModel):
        name =models.CharField(
        default='',
        max_length=254,
        blank=True,

    )
        description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        file=models.ImageField(
            default='',
            verbose_name='Image',
            blank=True,
            upload_to='images/'
    )
        class Meta:
            ordering = ['id']

class blogPageSetting(AbstractModel):
        name =models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        department = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        description = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        description1 = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )   
        description2 = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        description3 = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        comment = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        detail1 = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        detail2 = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
        file=models.ImageField(
            default='',
            verbose_name='Image',
            blank=True,
            upload_to='blog_images/'
    )
        fileSmall=models.ImageField(
            default='',
            verbose_name='Image',
            blank=True,
            upload_to='blog_images/'
    )
        class Meta:
            ordering = ['id']
   
class commentSetting(AbstractModel):
    comment =models.CharField(
        default='',
        max_length=254,
                blank=True,

    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    file=models.ImageField(
            default='',
            verbose_name='Image',
            blank=True,
            upload_to='comment_images/'
    )

class contactSetting(AbstractModel):
    address =models.CharField(
        default='',
        max_length=254,
                blank=True,

    )
    tel = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    email = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    calisma_week = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )
    calisma_weekend = models.CharField(
        default='',
        max_length=254,
        blank=True,
    )

class message(AbstractModel):
     name= models.CharField(
          default='',
          max_length=254,
          blank=True,
          verbose_name='Name',
          help_text='',
     )
     email= models.EmailField(
          default='',
          max_length=254,
          blank=True,
          verbose_name='Email',
          help_text='',
     )
     subject= models.CharField(
          default='',
          max_length=254,
          blank=True,
          verbose_name='Subject',
          help_text='',
     )
     message= models.TextField(
          default='',
          blank=True,
          verbose_name='Message',
          help_text='',
     )
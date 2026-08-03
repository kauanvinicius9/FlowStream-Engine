from django.db import models

class Manual(models.manual):
    manual_id=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=200,unique=True)
    lang=models.CharField(max_length=100,choices=[
        ('br','pt-BR'),
        ('en','en-US'),
        ('es','es-ES')])

    is_active=models.BooleanField(default=False)
    
    class Meta:
            verbose_name='Manual'
            verbose_name_plural='Manuals'
            ordering=['id']

    def __str__(self):
        return "{} ({})".format(self.description,self.manual_id)

class Product(models.Model):
    manual=models.ForeignKey(Manual,on_delete=models.PROJECT,related_name="manual_product")
    model_code=models.CharField(max_length=50)
    description=models.CharField(max_length=200,unique=True)

    class Meta:
        verbose_name="Product Registration (model)"
        verbose_name_plural="Products Registration (models)"
        ordering=['id']
    
    def __str__(self):
        return "{} ({})".format(self.manual,self.description)
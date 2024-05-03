from django.db import models

class weather(models.Model):
    city = models.CharField(max_length=32)
    temperature = models.CharField(max_length=24)
    description = models.TextField()
    icon = models.CharField(max_length=16)
    updated_date = models.DateTimeField()
    api_response = models.TextField ()
    
    
    def __str__(self) ->str:
        return self.city 
    

class Meta:
        managed = True  # This tells Django to create, modify, and delete the table
        db_table = 'weather'  # Custom database table name
        ordering = ['-temperature']  # Orders records by temperature in descending order
        verbose_name = 'Weather Report'
        verbose_name_plural = 'Weather Reports'
        
        
        







        
    

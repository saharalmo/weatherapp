from django.contrib import admin
from app.weathermodule.models import weather

class WeatherAdmin(admin.ModelAdmin):
    pass

admin.site.register(weather, WeatherAdmin)



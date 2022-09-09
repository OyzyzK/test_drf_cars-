from django.contrib import admin
from .models import *


@admin.register(CommentItem, CarItem, ProducerItem, CountryItem)
class NewsItemAdmin(admin.ModelAdmin):
    pass

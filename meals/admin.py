from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Meals, Category

# Apply summernote to all TextField in model.
class MealsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)




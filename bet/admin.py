from django.contrib import admin
from .models import Bet, Line
from django_summernote.admin import SummernoteModelAdmin 

# Register your models here.
@admin.register(Bet) 
class AboutAdmin(SummernoteModelAdmin):    
    list_display = ('punter', 'stake', 'settled', 'payout', 'created_on')
    search_fields = ['punter', 'settled']
    list_filter = ('punter', 'created_on', 'settled')
##    prepopulated_fields = {'punter': ('punter',)}
    
admin.site.register(Line)
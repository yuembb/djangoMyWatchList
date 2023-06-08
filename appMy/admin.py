from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    '''Admin View for Card'''

    list_display = ('title' , 'user' , 'category' , 'date_now' , 'id')
    search_fields = ('',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('title',)
    search_fields = ('',)
    
@admin.register(Type)
class Type(admin.ModelAdmin):
    
    list_display = ('title','category','category_id')
    search_fields = ('',)   
    
@admin.register(Dramatype)
class Dramatype(admin.ModelAdmin):
    
    list_display = ('title','category')
    search_fields = ('',)    

@admin.register(Gametype)
class Gametype(admin.ModelAdmin):

    list_display = ('title','category')
    search_fields = ('',)
    
@admin.register(Movietype)
class Movietype(admin.ModelAdmin):

    list_display = ('title','category')
    search_fields = ('',)
    
@admin.register(Animetype)
class Animetype(admin.ModelAdmin):

    list_display = ('title','category')
    search_fields = ('',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''Admin View for Comment'''

    list_display = ('card' , 'fname')
    search_fields = ('',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

   list_display = ('user', 'tel',  'id') 
   search_fields = ('',)
   
   
   
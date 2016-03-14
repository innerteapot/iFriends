from django.contrib import admin
from .models import Blog
from .models import Person

# Register your models here.
#admin.site.register(Person)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'blog_size',)
    list_filter = ('date',)
    date_hierarchy = 'date'
    search_fields = ('title', 'text',)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
            ('User', {'fields':('userID', 'name')}),
            ('Info', {'fields':('birthday', 'gender', 'desc')}),
            ('Contact', {
                'fields':('email', 'favoriteURL'),
            }),
            ('Friends', {
                'classes': ('collapse',),
                'fields':('friends',),
            }),
            ('Blogs', {'fields':('blogs',), 'classes': ('collapse',)}),
        )

    list_display = ('name', 'email', 'desc')
    list_filter = ('gender', 'friends',)
    ordering    = ('-name',)
    search_fields = ('name', 'email', 'desc')

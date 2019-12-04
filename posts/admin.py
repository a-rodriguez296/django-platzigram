from django.contrib import admin

from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'user', 'photo', 'created')

    list_display_links = ('pk',)

    list_editable = ('title','photo')

    search_fields = (
        'user__username',
        'user__email', 
        'title',
    )

    list_filter = (
        'modified',
    )


    fieldsets = (
        ('Post', {
            'fields': ('title', )
        }),
        ('Photo', {
            'fields': ('photo',)
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
                ('user'),
            )
            
        })
    )

    readonly_fields = ('created', 'modified', 'user')


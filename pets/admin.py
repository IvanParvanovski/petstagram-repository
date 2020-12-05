from django.contrib import admin

from pets.models.comment import Comment
from pets.models.pet import Pet
from pets.models.like import Like


class LikeInline(admin.TabularInline):
    model = Like


class PetAdmin(admin.ModelAdmin):
    # fields = ('type, name')
    list_display = ('id', 'type', 'name')
    list_filter = ('type',)
    inlines = (
        LikeInline,
    )


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
admin.site.register(Comment)

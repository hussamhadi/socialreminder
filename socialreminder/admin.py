from django.contrib import admin
from .models import Message, Person, Tag


class MessageAdmin(admin.ModelAdmin):
    list_display = ("__str__", )


class PersonAdmin(admin.ModelAdmin):
    list_display = ("__str__", "birthday", "get_tags")


class TagAdmin(admin.ModelAdmin):
    list_display = ("__str__",)


admin.site.register(Message, MessageAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Tag, TagAdmin)

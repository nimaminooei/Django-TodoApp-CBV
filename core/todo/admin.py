from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Tasks
class customtask(admin.ModelAdmin):
    model = Tasks
    list_display = ("user","task", "status")
    list_filter = ( "status",)
    fieldsets = (
        ("Tasks", {"fields": ("user","task", "status")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("user","task", "status")}
        ),
    )
    search_fields = ("task","user")
    ordering = ("task",)


admin.site.register(Tasks, customtask)
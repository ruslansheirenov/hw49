from django.contrib import admin

# Register your models here.

from .models import Issue, TypeModel, StatusModel

class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    search_fields = ['summary']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['statuses']
    search_fields = ['statuses']
    fields = ['statuses']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['types']
    search_fields = ['types']
    fields = ['types']


admin.site.register(Issue, IssueAdmin)
admin.site.register(TypeModel, TypeAdmin)
admin.site.register(StatusModel, StatusAdmin)
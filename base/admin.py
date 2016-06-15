from django.contrib import admin

# Register your models here.
from base.models import Dream, Budget, BudgetType


class DreamAdmin(admin.ModelAdmin):
    def creator(self, obj):
        if hasattr(obj.created_by, 'username'):
            return obj.created_by.username
        else:
            return 'None'
    creator.short_description = 'Dream created by'

    def save_model(self, request, obj, form, change):
        if obj.id:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()
    list_display = (
            'name',
            'visibility',
            'status',
            'total_budget',
            'created_by',
            'updated_by'
    )
admin.site.register(Dream, DreamAdmin)


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('get_dream_name', 'get_budget_type', 'amount')

    def get_dream_name(self, obj):
        return obj.dream.name

    def get_budget_type(self, obj):
        if obj.budget_type is not None:
            return obj.budget_type.name
        else:
            return None

admin.site.register(Budget, BudgetAdmin)


class BudgetTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(BudgetType, BudgetTypeAdmin)

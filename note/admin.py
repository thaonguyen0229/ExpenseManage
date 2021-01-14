from django.contrib import admin

from .models import Spending, Earning, Repeat_event

class SpendingAdmin(admin.ModelAdmin):
    fields = ['amount', 'description', 'create_date']

class EarningAdmin(admin.ModelAdmin):
    fields = ['amount', 'description', 'create_date']

admin.site.register(Spending, SpendingAdmin)
admin.site.register(Earning, EarningAdmin)
admin.site.register(Repeat_event)


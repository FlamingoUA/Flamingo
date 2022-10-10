from django.contrib import admin

from model.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'price', 'departure_time',
    )


admin.site.register(Ticket, TicketAdmin)

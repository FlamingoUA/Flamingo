from django.contrib import admin

from model.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    # ...
    list_display = (
        'name', 'price', 'date',
    )


admin.site.register(Ticket, TicketAdmin)
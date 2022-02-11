from django.contrib import admin
from .models import customer, transactionsTable

# Register your models here.
admin.site.register(customer)
admin.site.register(transactionsTable)
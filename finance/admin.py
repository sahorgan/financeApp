from django.contrib import admin

from .models import Account
from .models import Person
from .models import Transaction

admin.site.register(Account)
admin.site.register(Person)
admin.site.register(Transaction)


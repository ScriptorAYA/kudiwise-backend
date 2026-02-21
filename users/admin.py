from django.contrib import admin
from .models import User, Wallet

# users/admin.py
from django.contrib import admin
from .models import User

admin.site.register(User)

# wallet/admin.py
from django.contrib import admin
from .models import Wallet

admin.site.register(Wallet)


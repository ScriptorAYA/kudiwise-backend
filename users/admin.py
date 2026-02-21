from django.contrib import admin
from .models import User, Wallet

# users/admin.py
from django.contrib import admin
from .models import User

admin.site.register(User)

# wallet/admin.py
from django.contrib import admin
from .models import Wallet, Transaction

admin.site.register(Wallet)
admin.site.register(Transaction)

# trading/admin.py
from django.contrib import admin
from .models import Trade

admin.site.register(Trade)

# ai_tutor/admin.py
from django.contrib import admin
from .models import Lesson, UserLessonProgress

admin.site.register(Lesson)
admin.site.register(UserLessonProgress)


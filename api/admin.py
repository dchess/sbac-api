from django.contrib import admin
from .models import Entity, Type, Test, Grade, SubGroup, SubGroupAdmin

admin.site.register(Entity)
admin.site.register(Type)
admin.site.register(Test)
admin.site.register(Grade)
admin.site.register(SubGroup, SubGroupAdmin)

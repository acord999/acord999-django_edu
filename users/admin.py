from django.contrib import admin

from users.models import User


admin.site.register(User)

# @admin.register(User)
# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}

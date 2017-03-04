from django.contrib import admin
from .models import *
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
	pass
admin.site.register(Reviews, ReviewAdmin)

class BooksAdmin(admin.ModelAdmin):
	pass
admin.site.register(Books, BooksAdmin)

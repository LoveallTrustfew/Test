
from __future__ import unicode_literals
# -*- coding: utf-8 -*-


# Register your models here.


from django.contrib import admin

# Register your models here.
from .models import Blogpost


class BlogpostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blogpost, BlogpostAdmin)
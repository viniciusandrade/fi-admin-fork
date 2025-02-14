from django.contrib import admin
from text_block.models import *


class TextBlockLocalAdmin(admin.TabularInline):
    model = TextBlockLocal
    extra = 2


class TextBlockAdmin(admin.ModelAdmin):
    model = TextBlock
    inlines = [TextBlockLocalAdmin, ]


admin.site.register(TextBlock, TextBlockAdmin)

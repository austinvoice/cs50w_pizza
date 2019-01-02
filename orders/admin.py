from django.contrib import admin

from .models import Category, Type

# Register your models here.
class TypeInline(admin.TabularInline):
    model = Type
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('Size',             {'fields': ['item_size']})
    ]
    inlines = [TypeInline]
    list_display = ('category_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['category_text']

admin.site.register(Category, CategoryAdmin)



# from django.contrib import admin
#
# from .models import Choice, Question
#
#
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
#
# admin.site.register(Question, QuestionAdmin)

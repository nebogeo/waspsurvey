# -*- coding: utf-8 -*-

from django.contrib import admin

from survey.actions import make_published
from survey.exporter.csv import Survey2Csv
from survey.exporter.tex import Survey2Tex
from survey.models import Answer, Category, Question, Response, Survey, Image, Insect
from django.forms import TextInput, Textarea
from django.db import models
from django.utils.html import format_html

class QuestionInline(admin.TabularInline):
    model = Question
    ordering = ("order", "category")
    extra = 1
    formfield_overrides = {        
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':20})},
    }

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0


class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "need_logged_user", "template")
    list_filter = ("is_published", "need_logged_user")
    inlines = [CategoryInline, QuestionInline]
    actions = [make_published, Survey2Csv.export_as_csv, Survey2Tex.export_as_tex]


class AnswerBaseInline(admin.StackedInline):
    fields = ("question", "body")
    readonly_fields = ("question",)
    extra = 0
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    list_display = ("interview_uuid", "survey", "created", "user")
    list_filter = ("survey", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    readonly_fields = ("survey", "created", "updated", "interview_uuid", "user")

class ImageAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="/{}" />'.format(obj.photo))

    image_tag.short_description = 'Image'
    list_display = ['image_tag',]

class InsectAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="/{}" />'.format(obj.photo))

    image_tag.short_description = 'Insect'
    list_display = ['image_tag',]

#admin.site.register(Question, QuestionInline)
admin.site.register(Category)
admin.site.register(Insect, InsectAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Response, ResponseAdmin)

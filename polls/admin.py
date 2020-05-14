from django.contrib import admin

# Register your models here.

from polls.models import Question,Choice

admin.site.site_header="DailyUpdates Admin" 
admin.site.site_title="DailyUpdates Admin Page"
admin.site.index_title="Welcome to the DailyUpdates Admin Page"




class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),
    ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines=[ChoiceInLine]




admin.site.register(Question,QuestionAdmin)
#admin.site.register(Question)
#admin.site.register(Choice)

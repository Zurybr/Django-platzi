from django.contrib import admin
from .models import Question,Choice

# admin.site.register([Question, QuestionAdmin])


class ChoicesInline(admin.StackedInline): #traerte los nodos nodos 
    model = Choice
    extra: int = 3 #cuantas preguntas nuevas
    can_delete = False
    verbose_name_plural = 'choices'

@admin.register(Question) #es lo mismo que admin.site.register([Question, QuestionAdmin)
class QuestionAdmin(admin.ModelAdmin): #como en los test las clases van por bateria
    fields = ("pub_date","question_text",)
    inlines = (ChoicesInline,)

    list_display = ("question_text","pub_date","was_published_recently")

    list_filter = ["pub_date"]  #: _ListOrTuple[_ListFilterT] = 
    search_fields =["question_text"]      #: Sequence[str]


# @admin.display
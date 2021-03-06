
from django.urls import reverse
from typing import List
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.utils import timezone #para la hora
from django.utils.datastructures import MultiValueDictKeyError
from polls.models import Question,Choice #importar modelos
from django.db.models.query import QuerySet

#generic views
# from django.views.generic import ListView,DetailView
from django.views import generic
# def index(request):
#     # print(Question.objects.all())
#     # q = Question(question_text = "es una pregunta?",pub_date = timezone.now())
#     # q.save()
#     # q = Question(question_text = 'abc pregunta para buscar xyzz')
#     # q.save()
#     # print(Question.objects.get(question_text ='hola2?'))
#     # print(Question.objects.filter(pub_date__year =timezone.now().year))
#     # print(Question.objects.filter(question_text__startswith ="abc"))
#     q= Question.objects.get(pk =1)
#     # print(q.choice_set.all())
#     # q.choice_set.create(choice_text = 'Curso basico de python', votes = 0)
#     print(q.choice_set.all())
#     print(q.choice_set.count())

#     Choice.objects.filter(question__pub_date__year=timezone.now().year) #del atributo question del  modelo Choice, podemos acceder aninado al atributo pub_date de Questions, por su llave foranea
#     return HttpResponse('hola')

# def detail(request: HttpRequest, question_id: int):
#     question:Question = get_object_or_404(Question, pk=question_id)
#     choices:List[Choice] = question.choice_set.all()
#     return render(request, 'polls/detail.html', {
#         'question': question,
#         "choices":choices
#     })


def result(request:HttpRequest, question_id:int):
    question:Question = get_object_or_404(Question, pk=question_id)
    choices:List[Choice] = question.choice_set.all()
    return render (request, 'polls/results.html', {
        'question': question,
        "choices":choices
    })

#Post
def vote(request:HttpRequest):
    question_id:int = request.POST['question_id']
    choise_id:int
    question:Question = get_object_or_404(Question, pk=question_id)
    try:
        choise_id = request.POST['choice']
        selected_choices:Choice = question.choice_set.get(pk = choise_id)

    except(KeyError,Choice.DoesNotExist,MultiValueDictKeyError):
        return render(request,"polls/detail.html",{
            question:question,
            'error_message':"no elegiste una respuesta"
        })
    else:
        selected_choices.votes +=1
        selected_choices.save()
        return HttpResponseRedirect(reverse("polls:result",args = (question_id)))


# def iindex(request:HttpRequest):
#     lates_question_list = Question.objects.all()
#     return render(request,"polls/index.html",{"lates_question_list":lates_question_list})

class IndexView(generic.ListView):
    template_name= "polls/index.html"
    context_object_name = 'all_questions'
    queryset= Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5] # se puede usar la funcion de abajo, o este atributo
    # def get_queryset(self):
    #     return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    #en la vista podemos acceder a los nodos con question.choice_set.all
    def get_queryset(self):
        """
        Exlclude question that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now()) #modificador de modelo __ lte = less than o equals to 

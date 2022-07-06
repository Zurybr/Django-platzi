import imp
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpRequest
from django.utils import timezone #para la hora
from polls.models import Question,Choice #importar modelos

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


def index(request:HttpRequest):
    lates_question_list = Question.objects.all()
    return render(request,"polls/index.html",{"lates_question_list":lates_question_list})


def detail(request: HttpRequest, question_id: int):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    print(choices)
    return render(request, 'polls/detail.html', {
        'question': question,
        "choices":choices
    })


def result(request:HttpRequest):
    lates_question_list = Question.objects.all()
    return render(request,"polls/index.html",{"lates_question_list":lates_question_list})


def vote(request:HttpRequest):
    lates_question_list = Question.objects.all()
    return render(request,"polls/index.html",{"lates_question_list":lates_question_list})
import datetime
from urllib import response

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Question

class QuestionModelTest(TestCase): #a estos modelos se les llaman materias
    def setUp(self) -> None:
        _time = timezone.now() + datetime.timedelta(days=30)
        self.question = Question(question_text = "holas?", pub_date = _time)

    def test_was_published_recently_with_future_questions_without_setup(self):
        """was_published_recently retunrs False for questions who pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question =  Question(question_text = "hola?", pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently retunrs False for questions who pub_date is in the future"""
        self.assertIs(self.question.was_published_recently(),False)
    
    def test_was_published_recently_with_future_questions_with_otherdata(self):
        """was_published_recently retunrs False for questions who pub_date is in the future"""
        self.question.question_text = "alggo?"
        self.question.pub_date = timezone.now() - datetime.timedelta(days=30)
        self.assertIs(self.question.was_published_recently(),False)
    def test_was_published_recently_with_future_questions_now(self):
        """was_published_recently retunrs False for questions who pub_date is in the future"""
        self.question.question_text = "alggo?"
        self.question.pub_date = timezone.now()
        self.assertIs(self.question.was_published_recently(),True)

class QuestionIndexViewTest(TestCase):
    def setUp(self) -> None:
        _time = timezone.now() + datetime.timedelta(days=30)
        self.question = Question(question_text = "holas?", pub_date = _time)

    def test_no_questions(self):
        """If no question exist , an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index")) #reverse sirve para poner url sin harcodearla
        self.assertEqual(response.status_code,200)  #afirmo que son iguales
        self.assertContains(response, 'No polls are available.') #afirmo que contiene
        self.assertQuerysetEqual (response.context["all_questions"],[])
        #si llegan a salir preguntas publicadas en el futuro test de que no existan
    
    def test_future_question(self):
        """Questions with a pub_date in hte futrue aren't display on the index """
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual (response.context["all_questions"],[])


    def test_pasado_question(self):
        """Questions with a pub_date in the futrue aren display on the index """
        question = Question.objects.create(question_text = "holas?", pub_date = timezone.now() - datetime.timedelta(days=2)) #crear una pregunta en base de datos virtual
        response = self.client.get(reverse("polls:index"))
        self.assertNotEqual(response.context["all_questions"],[])
        self.assertQuerysetEqual(response.context["all_questions"],[question])

class QuestionDetailViewTests(TestCase):
    def test_future_questions(self):
        question = Question.objects.create(question_text = "holas?", pub_date = timezone.now() + datetime.timedelta(days=2))
        url = reverse("polls:detail", args = (question.pk,)) # los args tienen que ser una tupla por eso la coma  checar con el comando tuple([question.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)

    def test_past_question(self):
        question = Question.objects.create(question_text = "holas?", pub_date = timezone.now() - datetime.timedelta(days=2))
        url = reverse("polls:detail", args = tuple([question.pk])) # los args tienen que ser una tupla por eso la coma  checar con el comando tuple([question.pk])
        response = self.client.get(url)
        self.assertContains(response,question.question_text)
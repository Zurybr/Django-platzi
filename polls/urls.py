from django.urls import  path
from .views import IndexView,DetailView,result,vote

app_name = 'polls'
urlpatterns = [
    #ex: 'polls/'
    #path('',iindex,name='index'),
    path('',IndexView.as_view(),name='index'),
    #ex: 'polls/5'
    #path('<int:question_id>',detail,name='detail'),
    path('<int:pk>',DetailView.as_view(),name='detail'), #SI LA VISTA ES GENERIC DEBE DE LLEVAR PK 
    # 'polls/result/5'
    path('result/<int:question_id>',result,name='result'),
    # 'polls/vote/5'
    path('vote/',vote,name='vote'),
]
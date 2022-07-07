from django.urls import  path
from .views import index,detail,result,vote

app_name = 'polls'
urlpatterns = [
    # 'polls/'
    path('',index,name='index'),
    # 'polls/5'
    path('<int:question_id>',detail,name='detail'),
    # 'polls/result/5'
    path('result/<int:question_id>',result,name='result'),
    # 'polls/vote/5'
    path('vote/',vote,name='vote'),
]
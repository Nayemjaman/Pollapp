from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    # try:
    question = get_object_or_404(Question,pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('question dose not exist')
    return render(request,'polls/detail.html',{'question': question})
def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)
def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)










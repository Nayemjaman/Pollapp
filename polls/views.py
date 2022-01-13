from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

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
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{"question":question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':question,'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))















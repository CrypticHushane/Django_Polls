from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from .models import Profile, Question, Choice
# Create your views here.

def home(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        return render(request,'index.html', {'name':name, 'age':age})
    else:
        return render(request,'index.html' )

def about(request):
    profile = Profile.objects.all()
    first = Profile.objects.first()
    return render(request,'about.html', {'profile':profile, 'first':first})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice_text = get_list_or_404(Choice, question=question_id)
    return render (request,'detail.html', {'question':question, 'choice':choice_text})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'results.html', {'question':question})
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('djangoapp:results', args=(question.id,)))

def initial(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'initial.html',{'output':latest_question_list})
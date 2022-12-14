from audioop import reverse

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView, FormView, ListView, TemplateView, UpdateView
from django.template import loader
from .models import Question, Guests


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('love/index.html')
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request, 'love/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'love/detail.html', {'question':question})


class GuestViev(CreateView):
    model = Guests
    fields = ['name', 'surname']
    success_url = '/love/guestslist'



class GuestListView(ListView):
    model = Guests
    template_name = 'love/guests_list.html'
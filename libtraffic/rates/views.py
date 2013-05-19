# Create your views here.

from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext
from rates.models import Rate, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/rates/login/')

def index(request):
    latest_rate_list = Rate.objects.all()
    return render_to_response('rates/index.html',{'latest_rate_list': latest_rate_list})

def detail(request, rate_id):
    p = get_object_or_404(Rate, pk=rate_id)
    return render_to_response('rates/detail.html',{'rate': p},context_instance=RequestContext(request))

def results(request, rate_id):
    p = get_object_or_404(Rate, pk=rate_id)
    return render_to_response('rates/results.html', {'rate':p})

def vote(request, rate_id):
    p = get_object_or_404(Rate, pk=rate_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('rates/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('rates.views.results', args=(p.id,)))

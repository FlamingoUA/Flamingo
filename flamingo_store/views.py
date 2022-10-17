from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render
from django.urls import reverse


from flamingo_api.views import get_tickets
from model.models import Ticket


def wellcome(request):
    if request.method == "POST":
        # return reverse('test')
        # kwargs = {
        #     'dep_city': request.POST.get('dep_city'),
        #     'arr_city': request.POST.get('arr_city'),
        #     'date_from': request.POST.get('calendar_from'),
        #     'date_to': request.POST.get('calendar_to')
        # }
        # print(kwargs)
        kwargs = {
            'token': 'T1RLAQLc4fHjgvEuanP+n5HtqTjxby1I2OP4aCvxcZ9CziWLXBCYKZaiiwhhtY+poImWNo4bAADgisMtIDRF3A1OKCgxyLxhl4iPX76HhqvH/cUcahko8x11LOtCo+eqJKojVzSHvSvMdEpLGSjSgzItQICtwBZQX2CwC7rBqP03hzkEO3Ud3EDYuMJP2vOx/gZezWvJ9f7EvWzMrCD4jVIh0VGssIrm8BSF0OP3ibDxSAdZPMR8p95ltQnpLoeILmhP/hVw65tB1jwI8jSrvsUDMyTQ04LFl9LVgFRvsEOG1lVyICzFO8LlpbGs+VVA6jDo5vq2qiBBjdg6cTo1AxUvVUZwD1ZKnQ2DdCYBZm4eSkmHxZHu0+0*'
        }
        get_tickets(request, kwargs)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'flamingo_store/index.html')


class TicketsListViews(generic.ListView):
    paginate_by = 5
    model = Ticket
    template_name = 'flamingo_store/index2.html'
    context_object_name = 'tickets'

    def post(self, request, *args, **kwargs):
        kwargs = {
            'token': 'T1RLAQLc4fHjgvEuanP+n5HtqTjxby1I2OP4aCvxcZ9CziWLXBCYKZaiiwhhtY+poImWNo4bAADgisMtIDRF3A1OKCgxyLxhl4iPX76HhqvH/cUcahko8x11LOtCo+eqJKojVzSHvSvMdEpLGSjSgzItQICtwBZQX2CwC7rBqP03hzkEO3Ud3EDYuMJP2vOx/gZezWvJ9f7EvWzMrCD4jVIh0VGssIrm8BSF0OP3ibDxSAdZPMR8p95ltQnpLoeILmhP/hVw65tB1jwI8jSrvsUDMyTQ04LFl9LVgFRvsEOG1lVyICzFO8LlpbGs+VVA6jDo5vq2qiBBjdg6cTo1AxUvVUZwD1ZKnQ2DdCYBZm4eSkmHxZHu0+0*'
        }
        get_tickets(request, kwargs)
        return HttpResponseRedirect(reverse('home'))


def index(request):
    # print(request.GET.get('dep_city'))
    # print(request.GET.__dict__)
    return render(request, 'flamingo_store/test.html', {})

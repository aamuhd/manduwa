from django.views.generic import ListView, DetailView, View
from .helpers import Egg
from .models import MainPage, HomePageSlider, UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import reverse, render
# from blog.models import Post


# Create your views here.
class HomeView(View):
    template_name = "core/home.html"
    def get(self, *args, **kwargs):
        context = {}
        # context['posts'] = Post.objects.all().filter(publish=True).order_by('-pub_time')[:4]
        context['slider'] = HomePageSlider.objects.filter(active=True).first()
        return render(self.request, template_name='core/home.html', context=context)


class MainPageDetailView(DetailView):
    template_name = "core/pages.html" #.format(themeVersion() )
    model = MainPage
    query_pk_and_slug = True
    context_object_name = 'page'
    # context = {}
    def get_context_data(self, *args, **kwargs):  
        try:            
            context = super(MainPageDetailView, self).get_context_data(*args, **kwargs)
            print('Found')
            return context
        except MainPage.DoesNotExist:
            context['page'] =  Egg
            #TODO: send mail on error
            print('Not Found')
            return context
        return context

def contactView(request):
    next_url = reverse('audience:contact')
    return HttpResponseRedirect(next_url)

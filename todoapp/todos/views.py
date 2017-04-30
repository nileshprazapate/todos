from django.shortcuts import render
from django.http import HttpResponse

# from django.views.generic import TemplateView

# # Create your views here.
# class HomeView(TemplateView):
#     def get(self, request, **kwarge):
#         return render(request, 'index.html', context = None)



def index(request):
    context = {
        'app_title':'TodoApp'


    }
    return render (request, 'index.html',context)



def create(request):
    return render(request, 'create.html')
    # return HttpResponse ('this is my first #####')
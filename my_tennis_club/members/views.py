# importing package and modules
    # for rendering HttpResponse
from django.http import HttpResponse   
    # used for loading and rendering Django templates.
from django.template import loader 
    # importing Member Module from current directory models.py
from .models import Member


# Create your views here.
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context))

# view for details.html
def details(request, id):
  # passing keyword argument to get method
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    'firstname': 'Linus',
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))



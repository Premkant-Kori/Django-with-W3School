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
  value_list = Member.objects.values_list('firstname')
  filter = Member.objects.filter(firstname='Emil').values()
  mydata1 = Member.objects.filter(lastname='Refsnes', id=2).values()
  mydata2 = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  mydata3 = Member.objects.filter(firstname__startswith='L').values()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    'firstname': 'Linus',
    'mymembers': mymembers,
    'value_list':value_list,
    'filter':filter,
    "mydata1":mydata1,
    'mydata2':mydata2,
    'mydata3':mydata3,
  }
  return HttpResponse(template.render(context, request))



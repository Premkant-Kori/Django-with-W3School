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

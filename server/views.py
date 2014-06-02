from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from server.models import *
from django import forms
from django.forms.models import inlineformset_factory
from django.db import models
from django.forms import ModelForm
from django.template import RequestContext

class course_form(forms.Form):
    course_list = forms.ModelChoiceField(queryset=Course.objects.all())

class submission_form(ModelForm):
    class Meta:
        model = Submission
        fields = ['student','problem','image','answer']

def index(request):
    #AssignmentForm=inlineformset_factory(Problem,Submission) 
    if request.method == "POST": 
        formset = submission_form(request.POST,request.FILES) 
        print formset
        if formset.is_valid():
           formset.save()
        return HttpResponse("Thanks for uploading")      
    else: 
        formset = submission_form(initial={'student':Student.objects.get(id=1)})
        print request.user
        return render_to_response("student/index.html",{ "formset":formset, },RequestContext(request))

# Create your views here.
#ef index(request):
 #  inlineforms= inlineformset_factory(Problem, Submission)
  # formset=inlineforms()
    #form = submission_form()
    #print form
  ##print formset
   #ontext={'form':formset}
  # return render(request,'student/index.html',context)
    #if request.method == "POST":
    #    print request.POST['course_list']
    #    return HttpResponse("THanks %s" % request.POST)
    #else:
    #    form = course_form()
    #    context ={'form': form}
    #return render(request, 'student/index.html', context)

def upload(request, course_id):
    return HttpResponse("You're uploading for course." % course_id)



from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

def Djforms(request):
    SUFO=SignUpForms()
    d={'SUFO':SUFO}
    # if request.method=='POST':
    #     SUFDT=SignUpForms(request.POST)
    #     if SUFDT.is_valid():
    #         name=SUFDT.cleaned_data['name']
    #         return HttpResponse(str(SUFDT.cleaned_data))
    return render(request,'djforms.html',d)










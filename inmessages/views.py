from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import *
# Create your views here.

# Create your views here.

def request_in_house_proposal(request):
    course_id = request.GET.get('course_id')
    course_name = request.GET.get('course_name')
    form = InHouseProposalForm(request.POST or None)

    print(course_id)

    if form.is_valid():
        form.save()
        return redirect('sent_success')



    context = {'course_id':course_id,
               'course_name':course_name,
               'form':form}

    return render(request, "inmessages/inhouse-proposal-form.htm", context)

def sent_success(request):

    context = {}

    return render(request, "inmessages/inhouse-proposal-success.htm", context)

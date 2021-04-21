from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from datacenter.models import Applicant
from datacenter.models import Mark

def show_start_page(request):
    applicants = Applicant.objects.all()
    context = {
        "applicants": sorted(applicants, key=lambda paper: paper.full_name)
    }
    return render(request, 'applicants.html', context)
from django.shortcuts import render
from django.db.models import Q
from .models import Countries
from .models import Regions
from .models import Departments
from .models import Ishchilar
from django.http import HttpResponse
# Create your views here.
def orr_list(request):
    # region = Regions.objects.get(region_name="Asia")
    queryset=Ishchilar.objects.filter(Q(first_name__startswith="M")|Q(last_name__startswith="N"))
    print(queryset.query)
    country_list =""
    for i in queryset:
        country_list +=f"<li>{i.first_name}{i.last_name}</li>"
    return HttpResponse(f"<ol>{country_list}</ol>")



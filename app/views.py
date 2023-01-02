from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
from .result_list import *
from .models import *
from .age_list import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def year(request):
    global year_num
    global day_num
    try:
        year_num=int(request.GET["year"])
        day_num=request.GET["day"]
    except:
        error={"error":"It must be 1234 and no space"}
        return render(request,"index.html",error)
    else:
        if year_num<1400:
            l=r_list(year_num %7)
            data=Result.objects.get(id=l.index(day_num))
            return render(request,"result.html",{"data":data})
        elif year_num>1900:
          #  r=range(1,30){"range":r}
            return render(request,"month.html",)

def month(request):
    month_num=int(request.GET["month"])
    date_num=int(request.GET["date"])
    if month_num<4:
        l=r_list(year_num-638)
        data=Result.objects.get(id=l.index(day_num))
        return render(request,"result.html",{"data":data})
    elif month_num>4:
        l=r_list(year_num-639)
        data=Result.objects.get(id=l.index(day_num))
        return render(request,"result.html",{"data":data})
    elif month_num==4 and date_num<=16:
        l=r_list(year_num-638)
        data=Result.objects.get(id=l.index(day_num))
        return render(request,"result.html",{"data":data})
    elif month_num==4 and date_num>16:
        l=r_list(year_num-639)
        data=Result.objects.get(id=l.index(day_num))
        return render(request,"result.html",{"data":data})


def age(request):
    if year_num > 1400:
        age=(2023-year_num) % 8 
        
    else:
        age=(1384-year_num) % 8 
    age_list=for_age(day_num)
    age_data=Age.objects.get(id=age_list[age])
    
    return render(request,"age_result.html",{"age_data":age_data})

    
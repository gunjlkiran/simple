
from django.shortcuts import render
from .models import student
from rest_framework.renderers import JSONRenderer
from .serializers import studentserializers
from django.http import HttpResponse

# Create your views here.
def detail(request):
    stu=student.objects.get(id=1)
    pd=studentserializers(stu)
    jd=JSONRenderer().render(pd.data)
    return HttpResponse(jd,content_type='application/json')

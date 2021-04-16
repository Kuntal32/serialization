from django.shortcuts import render
from .models import Student
from .serializers import StuSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
   
def student_details(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StuSerializer(stu)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    serializer = StuSerializer(stu, many=True)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
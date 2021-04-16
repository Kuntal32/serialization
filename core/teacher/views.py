from django.shortcuts import render
from .serializers import TeacherSerializer
from .models import Teacher
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.

def get_teacher(req,pk):
    teacher = Teacher.objects.get(id=pk)
    teach = TeacherSerializer(teacher)
    return JsonResponse(teach.data)


def teachers(request):
    teacher = Teacher.objects.all()
    teach = TeacherSerializer(teacher, many=True)
    print(teach)
    return JsonResponse(teach.data, safe=False)
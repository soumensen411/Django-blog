from django.shortcuts import render
from .models import Student
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def StudentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

def StudentDetail(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)

@csrf_exempt
def createStudentView(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        parser_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=parser_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        error = serializer.errors
        return HttpResponse(error, content_type='application/json')
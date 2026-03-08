from django.shortcuts import render

# Create your views here.
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})


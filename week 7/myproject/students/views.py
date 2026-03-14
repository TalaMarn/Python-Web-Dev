from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator

# Create your views here.
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 3)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'student.html', {'students': students})

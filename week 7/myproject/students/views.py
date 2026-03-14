from django.shortcuts import redirect, render
from .models import Student
from django.core.paginator import Paginator
from .forms import StudentForm

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

def dashboard(request):
    total_students = Student.objects.count()

    context = {
        'total_students': total_students,
    }
    return render(request, 'dashboard.html', context)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
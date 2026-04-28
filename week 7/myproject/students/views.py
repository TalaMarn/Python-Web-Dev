from django.shortcuts import redirect, render
from .models import Student
from django.core.paginator import Paginator
from .forms import StudentForm

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    
    paginator = Paginator(students, 3)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    return render(request, 'student.html',{'students':page_obj})

def dashboard(request):
    total_students = Student.objects.count()
    male_students = Student.objects.filter(gender='Male').count()
    female_students = Student.objects.filter(gender='Female').count()
    recent_students = Student.objects.all().order_by('-id')[:5]

    context = {
        'total_students': total_students,
        'male_students' : male_students,
        'female_students': female_students,
        'recent_students': recent_students,
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


def edit_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'add_student.html',{'form':form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')
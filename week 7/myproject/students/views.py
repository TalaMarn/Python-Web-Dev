from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import Student, Profile
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StudentForm,LoginForm, RegisterForm

# Login

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('dashboard')
                profile = Profile.objects.filter(user=user).first()
                if profile and profile.role == 'Teacher':
                    return redirect('teacher_dashboard')
                return redirect('student_dashboard')
    return render(request, 'Login.html', {'form': form})

# Register
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )

            Profile.objects.create(
                user=user,
                role=form.cleaned_data['role']
            )
            return redirect('login')
    return render(request, 'register.html', {'form': form})


# Create your views here.
# Student Dashboard
@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


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

def school_info(request):
    return render(request, 'school_info.html')

def logout_view(request):
    logout(request)
    return redirect('login')
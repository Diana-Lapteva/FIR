from django.shortcuts import render, redirect
from .models import ProgramInfo, Student
from .forms import StudentForm
from django.db.models import Avg
from django.db.models import Q


def home(request):
    user_info = {
        'name': 'Лаптева Диана Дмитриевна',
        'photo': 'eduapp/images/me.png',
        'email': 'ddlapteva@edu.hse.ru',
        'phone': '+7 977 111 22 33',
        'program_name': 'Математика',
        'program_description': 'Описание программы: too much mathssss',
        'manager': {
            'name': 'Вот бы госы на 10',
            'photo': 'eduapp/images/s1.png',
            'email': 'kakzhit@mail.ru',
        },
    }
    return render(request, 'eduapp/home.html', {'user_info': user_info})

def students_table(request):
    students = Student.objects.all()
    avg_score = students.aggregate(Avg('average_score'))['average_score__avg']
    return render(request, 'eduapp/students_table.html', {'students': students, 'avg_score': avg_score})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_table')
    else:
        form = StudentForm()
    return render(request, 'eduapp/add_student.html', {'form': form})

def filter_students(request):
    students = Student.objects.all()

    gender = request.GET.get('gender')
    course = request.GET.get('course')
    sort = request.GET.get('sort')

    if gender:
        students = students.filter(gender=gender)
    if course:
        students = students.filter(course=course)

    if sort == 'name_asc':
        students = students.order_by('name')
    elif sort == 'name_desc':
        students = students.order_by('-name')
    elif sort == 'average_score_asc':
        students = students.order_by('average_score')
    elif sort == 'average_score_desc':
        students = students.order_by('-average_score')

    context = {
        'students': students,
        'selected_gender': gender,
        'selected_course': course,
        'selected_sort': sort,
    }
    return render(request, 'eduapp/filter_students.html', context)

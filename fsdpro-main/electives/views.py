from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Course, Question, Student
from .forms import TestForm
from .utils import calculate_final_score, check_eligibility
from django.shortcuts import render, redirect
from .models import Student
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'electives/course_list.html', {'courses': courses})
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'electives/course_detail.html', {'course': course})
def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        student = Student.objects.filter(name=username).first()

        if not student:
            return render(request, 'login.html', {'message': 'User not found'})

        if password != "student123":
            return render(request, 'login.html', {'message': 'Invalid password'})

        request.session['student_id'] = student.id
        return redirect('home')

    return render(request, 'login.html')
def take_test(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = Question.objects.filter(course=course)

    if request.method == "POST":
        form = TestForm(questions, data=request.POST)

        if form.is_valid():
            score = 0
            for q in questions:
                if form.cleaned_data[f"q_{q.id}"] == q.answer:
                    score += 1

            student = Student.objects.first()

            if not student:
                return render(request, 'electives/test_result.html', {
                    'score': score,
                    'final_score': 0,
                    'eligible': False,
                    'course': course,
                    'error': 'No student found. Please add student.'
                })

            final_score = calculate_final_score(score, student.cgpa)
            eligible = check_eligibility(final_score, course.difficulty)
            from .models import Result

            Result.objects.create(
                student=student,
                course=course,
                score=score,
                final_score=final_score,
                eligible=eligible
            )
            
            return render(request, 'electives/test_result.html', {
                'score': score,
                'final_score': final_score,
                'eligible': eligible,
                'course': course
            })

    else:
        form = TestForm(questions)

    return render(request, 'electives/test_page.html', {
        'form': form,
        'course': course
    })
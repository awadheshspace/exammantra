from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Test, Question, ExamResult
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import login
                                    
def my_view(request):
    user = request.user 

# @login_required
def test_list(request):
    tests = Test.objects.filter(active=True)
    return render(request, 'exam/test_list.html', {'tests': tests})

@login_required
def take_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = Question.objects.filter(test=test)
    end_time = timezone.now() + timezone.timedelta(minutes=test.duration)    
    print(end_time)
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option and int(selected_option) == question.correct_option:
               score += 1
            if selected_option:
                request.session[f'q{question.id}'] = int(selected_option)
        ExamResult.objects.create(
            student=request.user,
            test=test,
            score=score
        )
        return redirect('examresult:test_result', result_id=ExamResult.objects.latest('id').id)
    
    return render(request, 'exam/take_test.html', {
        'test': test,
        'questions': questions,
        'end_timestamp': int(end_time.timestamp() * 1000), 
        })




# @login_required
# def test_result(request, result_id):
#     result = get_object_or_404(ExamResult, pk=result_id, student=request.user)
#     questions = result.test.question_set.all()
    
#     # Get user's answers from session or database
#     user_answers = {}
#     for question in questions:
#         user_answers[question.id] = request.session.get(f'q{question.id}', None)
    
#     context = {
#         'result': result,
#         'questions': questions,
#         'user_answers': user_answers,
#         'total_questions': questions.count()
#     }
#     return render(request, 'exam/result.html', context)


@login_required
def test_result(request, result_id):
    result = get_object_or_404(ExamResult, pk=result_id, student=request.user)
    questions = result.test.question_set.all()
    
    # Get user's answers from session or database
    user_answers = {}
    for question in questions:
        user_answers[question.id] = request.session.get(f'q{question.id}', None)
    
    context = {
        'result': result,
        'questions': questions,
        'user_answers': user_answers,
        'total_questions': questions.count()
    }
    return render(request, 'exam/result.html', context)

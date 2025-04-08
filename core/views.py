from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        q = form.save(commit=False)
        q.user = request.user
        q.save()
        return redirect('home')
    return render(request, 'post_question.html', {'form': form})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        a = form.save(commit=False)
        a.user = request.user
        a.question = question
        a.save()
        return redirect('question_detail', question_id=question_id)
    return render(request, 'question_detail.html', {'question': question, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    answer.likes += 1
    answer.save()
    return redirect('question_detail', question_id=answer.question.id)

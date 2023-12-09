from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def all_categories(request):
    category_data = models.QuizCategory.objects.all()
    return render(request, 'category.html', {'data': category_data })

@login_required
def category_questions(request, cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'questions.html', {'question':question, 'category':category})

@login_required
def submit_answer(request, cat_id, que_id):

        if request.method == "POST":
            category = models.QuizCategory.objects.get(id=cat_id)
            question = models.QuizQuestion.objects.filter(category=category, id__gt=que_id).exclude(id=que_id).order_by('id').first()  # id__gt = id greater than
            if 'skip' in request.POST:
                if question:
                    que = models.QuizQuestion.objects.get(id=que_id)
                    user = request.user
                    answer = 'Not Submitted'
                    models.SubmitAnswer.objects.create(user=user, question=que, correct_answer=answer)
                    return render(request, 'questions.html', {'question':question, 'category':category})
            #     else:
            #         result = models.SubmitAnswer.objects.filter(user = request.user)
            #         return render(request, 'result.html', {'result':result})
            else:
                que = models.QuizQuestion.objects.get(id=que_id)
                user = request.user
                answer = request.POST['answer']
                models.SubmitAnswer.objects.create(user=user, question=que, correct_answer=answer)
            if question:
                return render(request, 'questions.html', {'question':question, 'category':category})
            else:
                result = models.SubmitAnswer.objects.filter(user = request.user)
                skipped = models.SubmitAnswer.objects.filter(user = request.user, correct_answer='Not Submitted').count()
                attempted = models.SubmitAnswer.objects.filter(user = request.user).exclude(correct_answer='Not Submitted').count()
                
                right_answer = 0
                percentage = 0
                for row in result:
                    if row.question.correct_option ==  row.correct_answer:
                        right_answer += 1
                percentage = (right_answer*100)/result.count()

                percent = round(percentage, 2)
                
                        
                return render(request, 'result.html', {'result':result, 'total_skipped':skipped, 'attempted':attempted, 'right_answer': right_answer, 'percent': percent})
        else:
            return HttpResponse("Method not allowed.")
        

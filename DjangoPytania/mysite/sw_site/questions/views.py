from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.views.generic import ListView, TemplateView
# Create your views here.
from .forms import AnswerForm



def home(response):
    return render(response, 'home.html', {"title": "Tytuł"})


def practise(response):
    all_questions = Question.objects.all()
    context = {
        "all_questions": all_questions
    }

    return render(response, 'practise.html', context)

def single_question_view(response, pk):

    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404("Question not exist")


    return render(response, 'single_question.html', {'question': question})


import random  
class PlayView(ListView):
    template_name = 'play.html'
    
    def get_queryset(self):
        single_question = random.choice(Question.objects.all())
        return single_question
    
    def post(self, request):
        # form = AnswerForm(request.POST or None)
        # if form.is_valid():

        question_number = request.POST.get("question_number")
        answer = Answer()
        answer.number_of_question = int(question_number)
        print(answer.number_of_question)
        answer.answer_a = "A" == request.POST.get("answera")
        answer.answer_b = "B" == request.POST.get("answerb")
        answer.answer_c = "C" == request.POST.get("answerc")
        user_answers = [answer.answer_a, answer.answer_b, answer.answer_c]

        single_question = Question.objects.get(pk=question_number)
        answer.answer_is_proper = single_question.check_answers(user_answers)

        answer.save()
        return redirect(request.path)




    # def get(self, request):
    #     all_questions = Question.objects.all()
    #     random_question = random.randint(1, len(all_questions))
    #     context = {
    #                 "all_questions": all_questions,
    #                 "random_number": random_question
    #             }
    #     return render(request, 'play.html', context)    

    # def post(self, request):
    #     answer = request.POST.get("answer")
    #     self.object = self.get_object()
    #     print(answer)
    #     print(self.object)


# def play_view(request):
#     all_questions = Question.objects.all()
#     random_question = random.randint(1, len(all_questions))
#     correct_answers = all_questions[random_question - 1].give_answers()

    
#     context = {
#             "all_questions": all_questions,
#             "random_number": random_question,
#             "correct_answers": correct_answers
#         }

#     if request.method == "GET":
#         return render(request, 'play.html', context)
    

#     if request.method == "POST":
#         answer = request.POST.get("answer")
#         correct_ans = get_object()
#         print(answer)
#         print(correct_ans)

        
#         return render(request, 'check_answer.html')
    

    


        
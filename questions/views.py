import random
from django.http import HttpResponse
from django.shortcuts import render
from . import QuestionBank

# Create your views here.
ques_id=randint(1,100) #100 questions for example (to be changed later)
def QuestionDisplay(request,ques_id) :
    question = Question.objects.get(id=ques_id)
    return render(request , tempname ,{ 'question': question }) #tempname=template_name (not specified yet)
                         
def CheckAns(request , ques_id ) # assuming the option input to be in forms
    if method == 'POST':
        Chosen_ans = request.POST[''] #get_the_chosen ans.
        return render(request , tempname , {'Chosen_ans':Chosen_ans})
        #currently returning the chosen answer which can be validated in the template , the question details are passed in the method above.
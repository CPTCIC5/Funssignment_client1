from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import QuizPost,Question, Result
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    qset=QuizPost.objects.all()
    return render(request,'index/home.html',{'qset':qset})

def rules(request):
    return render(request,'index/rules.html')


def paginated_quiz(request,title):
    queryset=QuizPost.objects.filter(title=title)
    post_query=QuizPost.objects.all()
    return render(request,'index/paginated_quiz.html',{'queryset':queryset,'post_query':post_query})

def search(request):
    if request.method=='POST':
        searched=request.POST.get('searched')
        print(searched)
        #qset2=QuizPost.objects.filter(title__icontains=searched)
        qset2=QuizPost.objects.filter(Q(title__icontains=searched) | Q(title__startswith=searched))
        return render(request,'index/search-result.html',{'qset2':qset2,'searched':searched})
    return render(request,'index/search-result.html')


@login_required
def quiz(request,post_id):
    queryset=Question.objects.filter(id=post_id)
    if request.method == 'POST':
        #queryset=Question.objects.get(id=post_id)
        queryset=get_object_or_404(Question,id=post_id)
        answer=request.POST.get('answer')
        answer2=request.POST.get('answer2')
        answer3=request.POST.get('answer3')
        answer3=request.POST.get('answer3')
        answer4=request.POST.get('answer4')
        answer5=request.POST.get('answer5')
        answer6=request.POST.get('answer6')
        answer7=request.POST.get('answer7')
        answer8=request.POST.get('answer8')
        answer9=request.POST.get('answer9')
        answer10=request.POST.get('answer10')
        answer11=request.POST.get('answer11')
        answer12=request.POST.get('answer12')
        answer13=request.POST.get('answer13')
        answer14=request.POST.get('answer14')
        answer15=request.POST.get('answer15')
        answer16=request.POST.get('answer16')
        answer17=request.POST.get('answer17')
        answer18=request.POST.get('answer18')
        answer19=request.POST.get('answer19')
        answer20=request.POST.get('answer20')
        correct=0
        wrong=0
        not_attempted=0
        if answer == queryset.answer:
            
            correct+=1
        elif answer is None or answer == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer2 == queryset.answer2:
            
            correct+=1
        elif answer2 is None or answer2 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer3 == queryset.answer3:
            
            correct+=1
        elif answer3 is None or answer3 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer4 == queryset.answer4:
            
            correct+=1
        elif answer4 is None or answer4 == "":
            not_attempted+=1
        else:
            wrong+=1

        if answer5 == queryset.answer5:
            
            correct+=1
        elif answer5 is None or answer5 == "":
            not_attempted+=1
        else:
            
            wrong+=1
        
        if answer6 == queryset.answer6:
            
            correct+=1
        elif answer6 is None or answer6 == "":
            not_attempted+=1
        else:
            
            wrong+=1
        
        if answer7 == queryset.answer7:
            
            correct+=1
        elif answer7 is None or answer7 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer8 == queryset.answer8:
            
            correct+=1
        elif answer8 is None or answer8 == "":
            not_attempted+=1
        else:
            
            wrong+=1
    
        if answer9 == queryset.answer9:
            
            correct+=1
        elif answer9 is None or answer9 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer10 == queryset.answer10:
            
            correct+=1
        elif answer10 is None or answer10 == "":
            not_attempted+=1
        else:
            
            wrong+=1
        
        if answer11 == queryset.answer11:
            
            correct+=1
        elif answer11 is None or answer11 == "":
            not_attempted+=1
        else:
            
            wrong+=1
        
        if answer12 == queryset.answer12:
            
            correct+=1
        elif answer12 is None or answer12 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer13 == queryset.answer13:
            
            correct+=1
        elif answer13 is None or answer13 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer14 == queryset.answer15:
            
            correct+=1
        elif answer14 is None or answer14 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer15 == queryset.answer15:
            
            correct+=1
        elif answer15 is None or answer15 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer16 == queryset.answer16:
            
            correct+=1
        elif answer16 is None or answer16 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer17 == queryset.answer17:
            
            correct+=1
        elif answer17 is None or answer17 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer18 == queryset.answer18:
            
            correct+=1
        elif answer18 is None or answer18 == "":
            not_attempted+=1
        else:
            
            wrong+=1

        if answer19 == queryset.answer19:
            
            correct+=1
        elif answer19 is None or answer19 == "":
            not_attempted+=1
        else:
            wrong+=1

        if answer20 == queryset.answer20:
            
            correct+=1
        elif answer20 is None or answer20 == "":
            not_attempted+=1
        else:
            wrong+=1
        score= correct *4 - wrong
        entry=Result(post=queryset,result_of=request.user,wrong=wrong,correct=correct,not_attempted=not_attempted,score=score)
        entry.save()
        messages.success(request,'Response Recorded!')
        return render(request,'index/result.html',{'queryset':queryset})
        #return HttpResponseRedirect(reverse('index:'))
    return render(request,'index/quiz.html',{'queryset':queryset})
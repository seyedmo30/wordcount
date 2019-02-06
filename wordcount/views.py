from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html',{'name':'mostafa'})

def count (request):
    fulltext = request.GET['txt']
    list=fulltext.split()
    dic={}


    for word in list:
        if word in dic:
            dic[word] +=1

        else:
            dic[word] =1


    lenn=len(list)

    return render(request,'cc.html',{'fulltext':fulltext,'lenn':lenn,'dic':dic})

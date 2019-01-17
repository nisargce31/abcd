from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "hello.html")

def test(request):
	return HttpResponse("This is just a test page")

def about(request):
    return render(request, "about.html")

def count(request):
    fulltext=request.GET["wordcount1"]
    print(fulltext)
    wordcount = fulltext.split()

    worddictionary={}

    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorted(worddictionary.items())
    return render(request, "count.html",{"fulltext":fulltext,"count":len(wordcount),"worddictionary":worddictionary.items()})
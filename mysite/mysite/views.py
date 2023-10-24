from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':"Pratham"  ,'place':"Patiala"}
    return render(request,'index.html',params)
    # return HttpResponse('''Hello, world. You're at the polls index. <a href=https://google.com>Google</a>''')

def about (request):
    return HttpResponse("about")

def uppercasefunc(djtext):
    return djtext.upper()
    
    
    # return HttpResponse("capitalize")

def removepunc(djtext):

    # print(djtext)
    # print(removepunctuation)

    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyse=""

    for c in djtext:
        if c not in punctuations:
            analyse=analyse+c

    return analyse

    # params={"purpose": "Removed Punctuations" ,"analysedtext":analyse}

    # return render(request,"analyse.html",params)

    # print(djtext)
    # return HttpResponse("remove punctuation")

def newlineremovefunc(djtext):
    djtext.replace("\n"," ")

    return djtext
    # return HttpResponse("newlineremove")

def spaceremovefunc(djtext):
    # return HttpResponse("spacere")
        return djtext.replace(" ","")
        # return djtext
        

# def charcountfunc(djtext):
#     djtext.len()

#     return djtext
    # return HttpResponse("charcount")


def AnalyseText(request):
    djtext=request.GET.get("text","default")
    removepunctuation=request.GET.get("removepunctuation", "off")
    uppercase=request.GET.get("uppercase","off")
    newlineremove=request.GET.get("newlineremove","off")
    spaceremove=request.GET.get("spaceremove","off")
    # charcount=request.GET.get("charcount","off")

    finalstring=djtext
    func=""
    if(removepunctuation=="on"):
        finalstring=removepunc(finalstring)
        # print(removepunctuation)
        func=func+" Removed Punctuations"

    if(uppercase=="on"):
        finalstring=uppercasefunc(finalstring)
        # print(uppercase)
        func=func+" Uppercase"

    if(newlineremove=="on"):
        finalstring=newlineremovefunc(finalstring)
        # print(newlineremove)
        func=func+" New lines removed"

    if(spaceremove=="on"):
        finalstring=spaceremovefunc(finalstring)
        print(spaceremove)
        func=func+" Spaces removed"

    # if(charcount=="on"):
    #    finalstring=finalstring+charcountfunc(djtext)
    #    print(charcount)

    func="Performed Operations"+func
    params={
        "answer":"Your analysed text"+finalstring,
        "operations":func,
    }

    return render(request,"analyse.html",params)






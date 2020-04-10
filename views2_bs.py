# I have written this code - Yash

from django.http import HttpResponse
from django.shortcuts import render


def index_Bs(request):
    return render(request,"index2(bs).html")

def analyze_Bs(request):

    #Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    charactercount = request.GET.get('charactercount','off')
    parameters = {}
    print(djtext)
    print(removepunc)

    if removepunc == "on":
        #analyze = djtext
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyze = ""
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char

        parameters= {'purpose':'Removed Punctuations', 'analyzed_text': analyze}

        djtext = analyze
        #Analyze the text
        #return render(request, 'analyze.html', parameters)

    if(fullcaps=="on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()

        parameters = {'purpose': 'Changed to uppercase', 'analyzed_text': analyze}

        djtext = analyze
        #return  render(request, 'analyze.html', parameters)

    if(newlineremover=="on"):
        analyze = ""
        for char in djtext:
            if char != "\n":
                analyze = analyze + char

        parameters = {'purpose':"Removed NewLines", 'analyzed_text': analyze}
        djtext = analyze

        #return render(request, "analyze.html", parameters)

    if(extraspaceremover=="on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index+1] == " "):
                pass
            else:
                analyze = analyze + char

        parameters = {"purpose":"Remove Extra Space","analyzed_text":analyze}
        djtext = analyze

        #return render(request, "analyze.html", parameters)

    if(charactercount=="on"):
        analyze = ""
        count = 0
        for char in djtext:
            count = count + 1

        parameters = {"purpose": "Character Count" ,"analyzed_text":count}


    if (removepunc != "on" and charactercount != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover !="on"):
         return HttpResponse("ERROR! Please select")

    return render(request, "analyze2(bs).html", parameters)
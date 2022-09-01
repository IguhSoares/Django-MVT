from django.shortcuts import render, redirect
from AppMVT.forms import ContactForm, LanguagesForm, SearchLanguageForm
from AppMVT.models import Contact, Languages
from django.http import HttpResponse, HttpResponseRedirect

def inicioApp(request):
    return render(request, "AppMVT/inicioApp.html")


def about(request):
    return render(request, 'AppMVT/about.html')

def languages(request, language=False):
    search_form = SearchLanguageForm()
    if language:
        result = Languages.objects.filter(language__icontains=language)
        return render(
            request,
            'AppMVT/languages.html',
            {'result': result}
        )
    else:
        return render(request,'AppMVT/languages.html', {'form': search_form})

def searchlanguages(request):
    if request.GET["language"]:
        lang=request.GET["language"]
        # text=Languages.objects.filter(language=language)
        return redirect(languages, language=lang)
    else:
        return render(request,'AppMVT/languages.html', {'msg': "No enviaste datos"})

def contactform(request):
    if request.method == 'POST':
        myform = ContactForm(request.POST)
        if myform.is_valid():
            info = myform.cleaned_data
            contact=Contact(full_name=info['full_name'],email=info['email'], phone=info['phone'], message=info['message'])
            contact.save()
            return render(request, 'AppMVT/inicioApp.html')
        else:
            return render(request, 'AppMVT/contactform.html')
    else:
        myform = ContactForm()
        return render(request,'AppMVT/contactform.html', {'contactform':myform})





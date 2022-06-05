# Virtual environment name = Learn
# Project name = DjangoProject


# COMMAND LINE in pwd = Directory of the project (folder = Learn)
# virtualenv .       		—> to create virtual environment
# source bin/activate	—> to activate virtualenv

# pip3 install django
# django-admin startproject DjangoProject		//creates project

# python manage.py startapp Learn	

# python3 manage.py runserver	//to run our app on webserver

# //sends any changes made to our models.py file to our db
# python3 manage.py makemigrations
# python3 manage.py migrate
# //creates an admin login page

# python3 manage.py createsuperuser

# Username : Fin
# Password : DjangoProject



# python3 manage.py runserver

from django.shortcuts import render, redirect   #redirect will allow us to redirect the user to another page when loged in sucessfully
from django.http import HttpResponse
from django.contrib.auth.models import User, auth   #this is the module in the databse admin page where users are logged in, & auth allows us to dedicate
from django.contrib import messages
from gtts import gTTS
import pdftotext



# When a page is requested, Django creates an HttpRequest object that 
# contains metadata about the request. Then Django loads the appropriate 
# view, passing the HttpRequest as the first argument to the view function. gtt
# Each view is responsible for returning an HttpResponse object.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():     #filters the database to check whether the email already exists
                messages.info(request, 'Email Already Used')    #sends a response back
                return redirect('register')
            elif User.objects.filter(username = username).exists():     #filters the database to check whether the email already exists
                messages.info(request, 'Username Already Used')    #sends a response back
                return redirect('register')
            elif username!='' and password!='':
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')
            else:
                messages.info(request, 'Invalid Input')
                return redirect('register')
        else:
            messages.info(request, 'Password doesnot match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')    #if user logged in successfully he is redirected to the home page
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def notepad(request):
    language = 'en'
    audio_is_TRUE = ''

    if request.method == 'POST':
        text = request.POST['text']
        language = request.POST['lang']
        if text:
            myobj = gTTS(text=text, lang=language , slow=False, )
            myobj.save("static/speech.mp3")
            audio_is_TRUE = 'ok'
            # context = {
            #     'audio_is_TRUE': audio_is_TRUE,
            # }
            # return render(request, 'notepad.html', context)
        else:
            messages.info(request, 'Enter text')
            return redirect('notepad')

    context = {
        'audio_is_TRUE': audio_is_TRUE,
    }
    return render(request, 'notepad.html', context)
    
def PdfToAudio(request):
    language = 'en'
    audio_is_TRUE = ''

    if request.method == 'POST':#and request.FILES['uploaded_pdf']:
        
        uploaded_pdf = request.FILES['uploaded_pdf']
        language = request.POST['lang']
        
        # if pdf available
        if uploaded_pdf :
            
            pdf_Reader = pdftotext.PDF(uploaded_pdf)
            Content_Of_PDF = ''

            for page in pdf_Reader:
                Content_Of_PDF += page


            text = Content_Of_PDF

            Audio_Object = gTTS(text=text, lang=language, slow=False, )
            Audio_Object.save("static/speech.mp3")
            
            audio_is_TRUE = 'ok'

            context = {
                'audio_is_TRUE': audio_is_TRUE,
            }
            return render(request, 'PdfToAudio.html', context)
        else:
            messages.info(request, 'Upload PDF')
            return redirect('PdfToAudio')

    context = {
        'audio_is_TRUE': audio_is_TRUE,
    }
    return render(request, 'PdfToAudio.html', context)

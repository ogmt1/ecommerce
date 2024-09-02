from django.shortcuts import redirect, render, HttpResponse
from home.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'home/home.html' )
    # return HttpResponse("This is the Home Page")
def about(request):
    return render(request, 'home/about.html' )
    # return HttpResponse("This is the About Page")
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        content = request.POST['content']
        email = request.POST['email']
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, "Please fill the form properly")
        else:
            contact = Contact(name=name, phone=phone, content=content, email=email)
            contact.save()
            messages.success(request, 'Your request has been submitted successfully!')
    return render(request, 'home/contact.html' )
    # return HttpResponse("This is the Contact Page")
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPosts = Post.objects.filter(title__icontains=query)
        allPosts = Post.objects.filter(author__icontains=query)
        allPosts = Post.objects.filter(content__icontains=query)
    if allPosts.count()==0:
       messages.warning(request, "No search reults found. Please refine your query")
    result = { 'query': query, 'allPosts': allPosts}
    return render(request, 'home/search.html', result)
def usersignup(request):
    if request.method == "POST":

        #parameters
        username = request.POST['username']
        inputfname = request.POST['inputfname']
        inputlname = request.POST['inputlname']
        inputemail = request.POST['inputemail']
        inputPass1 = request.POST['inputPass1']
        inputPass2 = request.POST['inputPass2']

        #check for errorneous input
        # if len(username)<20:
        #     messages.error(request, "Your username must be below 10 characters! ")
        #     return redirect('home')
        # if not username.islanum():
        #     messages.error(request, "Your username should in only letters format otherwise in numbers format! ")
        #     return redirect('home')
        if (inputPass1 != inputPass2):
            messages.error(request, "Passwords do not match, Please Check password and try again! ")
            return redirect('home')


        #creating user
        myuser = User.objects.create_user(username, inputemail, inputPass1)
        myuser.first_name = inputfname
        myuser.last_name = inputlname
        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('home')
    
    else:
        return HttpResponse(" Error - Please try again? ")

def userlogin(request):
    if request.method == 'POST':
        # parameter for the post
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is None:
            messages.error(request, "Invalid credentials, Please check and retry! ")
            return redirect('home')
        else:
            login(request, user)
            messages.success(request, "Hey !! You Have Successfully Logged In! ")
            return redirect('home')
    return HttpResponse("404 - Not Found")

def userlogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out! ")
    return redirect('home')










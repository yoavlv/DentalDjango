from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.



def home(request):
    return render(request, 'home.html',{})


def about(request):
    return render(request, 'about.html',{})


def blog(request):
    return render(request, 'blog.html',{})


def blog_details(request):
    return render(request, 'blog_details.html',{})


def contact(request):
        if request.method == 'POST':
            message_name= request.POST['message-name']
            message_email= request.POST['message-email']
            message = request.POST['message']

            sent = f"Thank you {message_name} The message sent! "

            # Send email - subject , message, from email, to emil
            send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['yoavlv12@gmail.com'], # to email
            fail_silently= False, # if the email fail send message - on production turn it on
            )
            return render(request, 'contact.html', {"sent":sent})



        else:
            return render(request, 'contact.html', {})




def pricing(request):
    return render(request, 'pricing.html',{})


def service(request):
    return render(request, 'service.html',{})

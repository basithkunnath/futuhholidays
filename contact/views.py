from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

# Create your views here.


def contact(request):
    view_contactus = Contact.objects.first()
    context = {
        'view_contact': view_contactus
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Construct the message
        email_message = '''
        From: {}\n
        Message: {}\n
        Email: {}\n
        Phone: {}\n
        '''.format(name, message, email, phone)

        # Prepare the email
        email_subject = 'You got a mail!'
        from_email = email  # Customer's email
        to_email = ['basith6k@gmail.com']

        # Create EmailMessage object with reply-to header
        email_msg = EmailMessage(
            email_subject,
            email_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=to_email,
            reply_to=[email]
        )

        try:
            email_msg.send()
            print("Email sent successfully")
        except Exception as e:
            print("Failed to send email:", e)
    return render(request, 'contact.html',context)
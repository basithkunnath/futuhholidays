from django.shortcuts import render
from . models import Packages,ItineraryItem
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.



def view_packages(request):
    view_package = Packages.objects.all()
    context = {
        'packages': view_package
    }
    return render(request, 'packages.html',context)


def package_details(request,pk):
    package_details = get_object_or_404(Packages, pk=pk)
    
    itinerary_items = ItineraryItem.objects.filter(package=package_details).order_by('day_number')
    context = {
        'details': package_details,
        'itinerary_items': itinerary_items
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
    return render(request, 'package_details.html',context)
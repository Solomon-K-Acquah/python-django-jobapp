import email
from pyexpat import model
from django.shortcuts import redirect, render
from django.urls import reverse

from app import views
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def subscribe(request):
    email_error_empty = ""

    # making an instance of the subscribe form model
    subscribe_form = SubscribeForm()

    if request.POST:
        # getting the data from the form
        # first_name = request.POST['firstname']
        # last_name = request.POST['lastname']
        # email = request.POST['email']
        # ------------------------------------------

        # binding data to form using the form model
        subscribe_form = SubscribeForm(request.POST)

        # validate
    
        # adding validation
        # if email == "":
        #     email_error_empty = "The email field cannot be empty"
        # print('Post Request', email)

        # using django form
        if subscribe_form.is_valid():
            print('Valid Form')
        # --------------------------------------------

        # saving data into the database
        # subscribe = Subscribe()

        # subscribe.first_name = first_name
        # subscribe.last_name = last_name
        # subscribe.email = email
        # subscribe.save()

            # -------------------------------------------------------------
            # saving data with django form
            # print(subscribe_form.cleaned_data)
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # email = subscribe_form.cleaned_data['email']
            
            # print(last_name)

            # subscribe = Subscribe(
            #     first_name = first_name,
            #     last_name = last_name,
            #     email = email
            # )
            # subscribe.save()

            # -------------------------------------------------------------
            # saving data to the database using 'ModelForm' save method
            subscribe_form.save() 

            return redirect(reverse('thank_you'))
        # -------------------------------------------

        # Method 2
        # subscribe.first_name = request.POST['firstname']
        # subscribe.last_name = request.POST['lastname']
        # subscribe.email = request.POST['email']
        # subscribe.save()

    context = {'form':subscribe_form, 'email_error_empty':email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
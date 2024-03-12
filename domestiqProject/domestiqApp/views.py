from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


# - - - - - PAGE ROUTE ADDRESSES - - - - -
#Immediate routing to index.html on server launch
def index(request):
    return render(request, 'domestiqApp/html/index.html')

# Client registration functionality
def client_signup(request):
    if request.method == 'POST':
        
        client_fname = request.POST['client_fname']
        client_lname = request.POST['client_lname']
        client_username = request.POST['client_username']
        client_email = request.POST['client_email']
        client_password = request.POST['client_password']
        client_dob = request.POST['client_dob']
        client_gender = request.POST['client_gender']
        client_maritalStatus = request.POST['client_maritalStatus']
        client_nationality = request.POST['client_nationality']
        client_acceptTerms = request.POST['client_acceptTerms']

        myClient = CustomUser.objects.create_user(
            username=client_username,
            email=client_email,
            password=client_password,
        )

        myClient.first_name = client_fname
        myClient.last_name = client_lname
        myClient.client_dob = client_dob
        myClient.client_gender = client_gender
        myClient.client_maritalStatus = client_maritalStatus
        myClient.client_nationality = client_nationality
        myClient.client_acceptTerms = client_acceptTerms

        myClient.save()

        messages.success(request, 'You have successfully registered as a client!')

        return redirect('login')

    return render(request, 'domestiqApp/html/client-sign-up.html')


#Route to WORKER sign up page on ...8000/worker-signup/
def worker_signup(request):
        
    return render(request, 'domestiqApp/html/worker-sign-up.html')

#Route to log in page on ...8000/login/

def log_in(request):
    if request.method == 'POST':
        client_username = request.POST['client_username']
        client_password = request.POST['client_password']

        user = authenticate(username=client_username, password=client_password)

        if user is not None:
            login(request, user)
            client_lname = user.last_name
            return render(request, 'domestiqApp/html/index.html', {'client_lname': client_lname})
        
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('index')

    return render(request, 'domestiqApp/html/log-in.html')

# ...




    '''
    # - - - GOOD CODE FOR LOG_IN VIEW(One form only though - - - -)
    if request.method == 'POST':
        client_username = request.POST['client_username']
        client_password = request.POST['client_password']

        user = authenticate(username=client_username, password=client_password)

        if user is not None:
            login(request, user)
            client_lname = user.last_name
            return render(request, 'domestiqApp/html/index.html', {'client_lname': client_lname})
        
        else:
            messages.error(request, 'Wrong credentials')
            return redirect ('index')


    return render(request, 'domestiqApp/html/log-in.html')
'''
# Log out view
def log_out(request):
    logout(request)
    messages.success(request, 'Logged Out successfully')

    return redirect('index')



#Route to about.html on ...8000/about/
def about(request):
    return render(request, 'domestiqApp/html/about.html')
#Route to services.html on ...8000/services/
def services(request):
    return render(request, 'domestiqApp/html/services.html')
def search(request):
    return render(request, 'domestiqApp/html/search.html')
#Route to contact.html on ...8000/contact/
def contact(request):
    return render(request, 'domestiqApp/html/contact.html')
#Route to success.html on ...8000/success/
def success(request):
    return render(request, 'domestiqApp/html/success.html')
#Route to client-dashboard.html on ...8000/clientdash/
def clientdash(request):
    return render(request, 'domestiqApp/html/client-dash.html')
#Route to worker-dashboard.html on ...8000/workerdash/
def workerdash(request):
    return render(request, 'domestiqApp/html/worker-dash.html')
#Route to admin-dashboard.html on ...8000/admindash/
def admindash(request):
    return render(request, 'domestiqApp/html/admin-dash.html')





'''
# - - - - - REGISTRATION FORM VIEWS - - - - -
#Client registration form initial view: form handling?
def client_registration(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # You can perform additional actions before saving if needed
            instance.save()

            # Log in the user
            # login(request, instance.user)

            return redirect('client_dash')  # Redirect to success page after successful registration
    else:
        # If it's a GET request or the form is invalid, use the existing form instance
        form = ClientRegistrationForm()

    return render(request, 'domestiqApp/html/client-sign-up.html', {'form': form})



def worker_registration(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # You can perform additional actions before saving if needed
            instance.save()
            return redirect('worker_dash')  # Redirect to success page after successful registration
    else:
        # If it's a GET request or the form is invalid, use the existing form instance
        form = WorkerRegistrationForm()

    return render(request, 'domestiqApp/html/worker-sign-up.html', {'form': form})


# - - - - - DATABASE QUERIES - - - - -
def client_name(request):
    client_name = request.user.clientRegistration.client_lname  # Adjust this based on your model structure
    return render(request, 'domestiqApp/html/client-dash.html', {'client_name': client_name})
'''
















'''
# - - - - -BASIC REGISTRATION CODE FROM GPT - - - - -
# - - - - - PAGE ROUTE ADDRESSES - - - - -
#Immediate routing to index.html on server launch
def index(request):
    return render(request, 'domestiqApp/html/index.html')
#Route to CLIENT sign up page on ...8000/client-signup/
def client_signup(request):
    return render(request, 'domestiqApp/html/client-sign-up.html')
#Route to WORKER sign up page on ...8000/worker-signup/
def worker_signup(request):
    return render(request, 'domestiqApp/html/worker-sign-up.html')
#Route to log in page on ...8000/login/
def login(request):
    return render(request, 'domestiqApp/html/log-in.html')
#Route to about.html on ...8000/about/
def about(request):
    return render(request, 'domestiqApp/html/about.html')
#Route to services.html on ...8000/services/
def services(request):
    return render(request, 'domestiqApp/html/services.html')
def search(request):
    return render(request, 'domestiqApp/html/search.html')
#Route to contact.html on ...8000/contact/
def contact(request):
    return render(request, 'domestiqApp/html/contact.html')
#Route to success.html on ...8000/success/
def success(request):
    return render(request, 'domestiqApp/html/success.html')
#Route to client-dashboard.html on ...8000/clientdash/
def clientdash(request):
    return render(request, 'domestiqApp/html/client-dash.html')
#Route to worker-dashboard.html on ...8000/workerdash/
def workerdash(request):
    return render(request, 'domestiqApp/html/worker-dash.html')
#Route to admin-dashboard.html on ...8000/admindash/
def admindash(request):
    return render(request, 'domestiqApp/html/admin-dash.html')

# Log out view
def log_out(request):
    pass




# - - - - - REGISTRATION FORM VIEWS - - - - -
#Client registration form initial view: form handling?
def client_registration(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # You can perform additional actions before saving if needed
            instance.save()

            # Log in the user
            # login(request, instance.user)

            return redirect('client_dash')  # Redirect to success page after successful registration
    else:
        # If it's a GET request or the form is invalid, use the existing form instance
        form = ClientRegistrationForm()

    return render(request, 'domestiqApp/html/client-sign-up.html', {'form': form})



def worker_registration(request):
    if request.method == 'POST':
        form = WorkerRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            # You can perform additional actions before saving if needed
            instance.save()
            return redirect('worker_dash')  # Redirect to success page after successful registration
    else:
        # If it's a GET request or the form is invalid, use the existing form instance
        form = WorkerRegistrationForm()

    return render(request, 'domestiqApp/html/worker-sign-up.html', {'form': form})


# - - - - - DATABASE QUERIES - - - - -
def client_name(request):
    client_name = request.user.clientRegistration.client_lname  # Adjust this based on your model structure
    return render(request, 'domestiqApp/html/client-dash.html', {'client_name': client_name})
'''
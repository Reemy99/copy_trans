from django.contrib.messages import success
from django.shortcuts import render, redirect
from .database_managment import DatabaseManagement

from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
from django.http import HttpResponse
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
from . import views



# Redirects users to the 42 Intra authentication page.

#     This view constructs a URL with the required query parameters for OAuth2 authentication,
#     including the response type, client ID, redirect URI, and desired scopes. Users will be
#     redirected to this URL, where they'll log in to 42 Intra. After successful login, 42 Intra
#     will redirect them back to our application using the provided redirect URI.
    
# Constants (replace with your actual values)
CLIENT_ID = 'u-s4t2ud-7930e369d50b3f8094be31a616ccfd8733f37608390fa7847559e89bd8381ef1'
CLIENT_SECRET = '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'
#  The Redirect URI - replace with the URI where 42 Intra should redirect after login
REDIRECT_URI = 'https://localhost:8000/intra_callback/'
# The URL to redirect users to for authentication with 42 Intra
AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
TOKEN_URL = 'https://api.intra.42.fr/oauth/token'



def intra_login(request):
    # Your view logic here
    pass

# def index(request):
#     return render(request, 'index.html')

# def hello(request):
#     return render(request, 'hello.html')

def landing_page(request):
    return render(request, 'Front-end/landing_page.html')

def intra_html(request):
    # Add any logic you need to render the intra.html page
    return render(request, 'Front-end/intra.html')

def register(request):
    return render(request, 'Front-end/register.html')

def game_options(request):
    return render(request, 'Front-end/gameOptions.html')
#view that renders the intra.html template.


# ... (your existing code)

# def intra_login(request):
#     return render(request, 'Front-end/intra.html')


# Constants (replace with your actual values)
CLIENT_ID = 'u-s4t2ud-7930e369d50b3f8094be31a616ccfd8733f37608390fa7847559e89bd8381ef1'
CLIENT_SECRET = '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'
#  The Redirect URI - replace with the URI where 42 Intra should redirect after login
REDIRECT_URI = 'http://localhost:3000/intra_callback/'
# The URL to redirect users to for authentication with 42 Intra
AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
TOKEN_URL = 'https://api.intra.42.fr/oauth/token'

# Create your views here.
#-----------Authentication intra------------------------#

def redirect_to_intra_auth(request):
    # Construct the authorization URL
    params = {
        'response_type': 'code',  # Indicates we want an authorization code
        'client_id': CLIENT_ID, # The Client ID obtained from 42 Intra
        'redirect_uri': REDIRECT_URI, # Where to redirect users after authentication
        'scope': 'public'  # The scope of access
    }
    # Construct the full URL for redirection
    auth_url = f"{AUTHORIZATION_URL}?{urlencode(params)}"
    print(f"Authorization URL: {auth_url}")
    # Redirect the user to the authentication URL
    return redirect(auth_url)

    # Handles the callback from 42 Intra after user authentication.

    # This view is responsible for processing the callback from 42 Intra. It will extract the
    # authorization code from the callback request and exchange it for an access token using
    # 42 Intra's token endpoint.
def intra_callback(request):
    # Extract the authorization code from the callback
    print("Callback function triggered")
    code = request.GET.get('code')
    print(f"Authorization code received: {code}")
    if not code:
        return HttpResponse("Error: No code provided", status=400)

    # Exchange the code for an access token
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    # Make a POST request to the token endpoint to exchange the code for an access token
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        # Handle successful authentication and token retrieval
        access_token = response.json().get('access_token')
       # Here, you can use the access token to make authenticated requests to the 42 Intra API
        # For example, save the token in the user's session or database
        return HttpResponse("Authentication successful")
    else:
        return HttpResponse("Error retrieving access token", status=response.status_code)


def redirect_to_intra_auth(request):
    # Construct the authorization URL
    params = {
        'response_type': 'code',  # Indicates we want an authorization code
        'client_id': CLIENT_ID, # The Client ID obtained from 42 Intra
        'redirect_uri': REDIRECT_URI, # Where to redirect users after authentication
        'scope': 'public'  # The scope of access
    }
    # Construct the full URL for redirection
    auth_url = f"{AUTHORIZATION_URL}?{urlencode(params)}"
    print(f"Authorization URL: {auth_url}")
    # Redirect the user to the authentication URL
    return redirect(auth_url)

    # Handles the callback from 42 Intra after user authentication.

    # This view is responsible for processing the callback from 42 Intra. It will extract the
    # authorization code from the callback request and exchange it for an access token using
    # 42 Intra's token endpoint.
def intra_callback(request):
    # Extract the authorization code from the callback
    print("Callback function triggered")
    code = request.GET.get('code')
    print(f"Authorization code received: {code}")
    if not code:
        return HttpResponse("Error: No code provided", status=400)

    # Exchange the code for an access token
    data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    # Make a POST request to the token endpoint to exchange the code for an access token
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        # Handle successful authentication and token retrieval
        access_token = response.json().get('access_token')
       # Here, you can use the access token to make authenticated requests to the 42 Intra API
        # For example, save the token in the user's session or database
        return HttpResponse("Authentication successful")
    else:
        return HttpResponse("Error retrieving access token", status=response.status_code)

#------------------------------------------------------------------------------#

def hello(request):
    return render(request, 'hello.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        db_management = DatabaseManagement()

        # Check if the login was successful
        is_authenticated = db_management.login_user(email, password)

        if is_authenticated:
            # Login successful
            print(request, f"User {email} authenticated successfully.")
            return render(request,'Front-end/homepage.html')
        else:
            # Login failed
            print(request, "Invalid email or password.")
            return redirect('login')  # Redirect to the login page
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        email = request.POST.get('Email')
        db_management = DatabaseManagement()
        user_id = db_management.create_user(username, password)
        db_management.create_email_user(username, email, password)
        db_management.create_user_settings(user_id, nickname, email, "Hi! Would you like to play?", False)
        print(request, "Register successful.")
        return render(request, 'login.html')
    else:
        print(request, "Register Not successful.")
        return render(request, 'Front-end/register.html')

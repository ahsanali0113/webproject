from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
class Home(TemplateView):
    template_name = 'index.html'


class Dashboardconfirm(View):
    template_name = 'dashboard-l.html'

    def get(self, request):
        return render(request, self.template_name)


class About(View):
    template_name = 'about-us.html'

    def get(self, request):
        return render(request, self.template_name)


class Borrow(View):
    template_name = 'dashboard-b.html'

    def get(self, request):
        data = Lender.objects.all()
        context = {
            'data': data
        }
        return render(request, self.template_name, context)


class Dashboard(View):
    template_name = 'dashboard-l-2nd.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        first_name = request.POST.get('fname','')
        last_name = request.POST.get('lname','')
        numbers = request.POST.get('number','')
        location = request.POST.get('location','')
        address = request.POST.get('address','')
        id_card = request.POST.get('cnic','')
        title = request.POST.get('title','')
        description = request.POST.get('description','')
        category = request.POST.get('checkbox[]','')
        price = request.POST.get('price','')
        image_one = request.FILES.get('pic','')
        image_two = request.FILES.get('pic_two','')
        pst = Lender.objects.create(first_name=first_name, last_name=last_name, phone=numbers, city=location, address=address,
                     cnic=id_card, title=title, description=description, category=category, price=price, photo_one=image_one, photo_two=image_two)
        pst.save()
        messages.success(request, 'message sent successfull!')
        return redirect('home')


class Message(View):
    template_name = 'contact-us.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            msg = Contact(name=name, email=email, message=message)
            msg.save()
            messages.success(request, 'message sent successfull!')
        return redirect('home')


class Registration(TemplateView):
    template_name = 'register-signup.html'

    def post(self, request):
        # Get the post parameters
        user = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pswd1')
        pass2 = request.POST.get('pswd2')

        # check for errorneous input
        # check for errorneous input
        if len(user) < 5:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('registration')
        if User.objects.filter(username=user):
            messages.error(request, " user already exist")
            return redirect('registration')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('registration')
        # Create the user
        myuser = User.objects.create_user(username=user, email=email, password=pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect("registration")


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request):
            # Get the post parameters
        loginname = request.POST.get('name')
        loginpassword = request.POST.get('password')
        user = authenticate(username=loginname, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("Login")


class ProductDetailView(View):
    template_name = 'd-sandals.html'

    def get(self, request, id):
        data = Lender.objects.filter(id=id)
        context = {
            'data' : data
        }
        return render(request, self.template_name, context)

class SearchResultsView(ListView):
    model = Lender
    template_name = "search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        results = Lender.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return results    

def search(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Lender.objects.filter(title__contains=query_name)
            return render(request, 'search.html', {"results":results})

    return render(request, 'search.html')
# def search(request):

#     results = []

#     if request.method == "GET":

#         query = request.GET.get('search')

#         if query == '':

#             query = 'None'

#         results = Lender.objects.filter(Q(description __icontains=query) | Q(title __icontains=query))

#     return render(request, 'search.html', {'query': query, 'results': results})

def search_home(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Lender.objects.filter(title__contains=query_name)
            return render(request, 'hsearch.html', {"results":results})

    return render(request, 'hsearch.html')



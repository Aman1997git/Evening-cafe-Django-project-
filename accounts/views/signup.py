from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from accounts.models.customer import Customer


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):

        # get data given by user
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        # validate customer
        if password == confirm_password:
            # check if customer with same email exist
            if Customer.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return render(request, 'signup.html')

            # check if customer with same username exist
            elif Customer.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return render(request, 'signup.html')

            # save customer
            else:
                customer = Customer(name=name, username=username, email=email, password=password)
                customer.register()
                request.session['customer'] = customer.id
                request.session['customer_name'] = name
                request.session['customer_email'] = email
                print(name, username, email, password, confirm_password)
                return redirect('home')
        else:
            messages.info(request, 'Password not matched')
            return render(request, 'signup.html')








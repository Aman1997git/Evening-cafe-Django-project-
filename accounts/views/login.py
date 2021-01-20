from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from accounts.models.customer import Customer


class Login(View):
    return_link = None

    def get(self, request):

        Login.return_link = request.GET.get('return_link')
        print("tttt", Login.return_link)
        return render(request, 'login.html')

    def post(self, request):

        # get data given by user
        email = request.POST.get('email')
        password = request.POST.get('password')

        # get customer of corresponding email from database, if exists
        customer = Customer.get_customer_by_email(email)

        # validate customer
        if customer:

            if password == customer.password:
                request.session['customer'] = customer.id
                request.session['customer_name'] = customer.name
                request.session['customer_email'] = email
                print("ttsst", Login.return_link)
                if Login.return_link:
                    return HttpResponseRedirect(Login.return_link)
                else:
                    return redirect('home')

            else:
                messages.info(request, 'wrong Password')
                return render(request, 'login.html')

        else:
            messages.info(request, 'customer do not exist')
            return render(request, 'login.html')

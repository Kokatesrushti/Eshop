from django.shortcuts import render, redirect

# Create your views here.
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        # customer object
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving data
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:

            data = {
                'values': value,
                'error': error_message
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):

        error_message = None
        if not customer.first_name:
            error_message = "First name is required"
        elif len(customer.first_name) < 4:
            error_message = "Length of first name must be greater than or equal to 4 character"
        elif not customer.last_name:
            error_message = 'Last name is required'
        elif len(customer.last_name) < 4:
            error_message = 'Length of lat name must be greater than or equal to 4 character'
        elif not customer.phone:
            error_message = 'phone number is required'
        elif len(customer.phone) < 10:
            error_message = 'The length of the phone number must be 10 digit'
        elif len(customer.email) < 5:
            error_message = 'The length of the email must be 5 character long'
        elif not customer.password:
            error_message = 'password is required'
        elif len(customer.password) < 5:
            error_message = 'The length of the password must be 5'
        elif customer.isExists():
            error_message = "Email address already exist"
        return error_message

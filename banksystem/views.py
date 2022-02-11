from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . forms import transactions
from banksystem.models import customer, transactionsTable

import time

def index(request):
    try:
        data = customer.objects.all()
        Context = {
			'data':data,
		}
    except customer.DoesNotExist:
        raise Http404("Data does not exist")
    
    return render(request,'banksystem/index.html', Context)

def profile(request, id):
    message=None
    error=None
    try:
        data = customer.objects.get(id=id)
        customers = customer.objects.all().exclude(id=id)
        if request.method == 'POST':
            form = transactions(request.POST or None)
            if form.is_valid():
                amount = request.POST.get('amount')
                if ( int(amount) < data.balance ):
                    form.save()
                    nameOne = request.POST.get('name_one')
                    nameTwo = request.POST.get('name_two')
                    #new_entery = transactionsTable.objects.create(name_one = nameOne,name_two=nameTwo,amount = amount)
                    userb2 = customer.objects.get(name = nameTwo)
                    data.balance -= int(amount)
                    userb2.balance += int(amount)
                    data.save()
                    userb2.save()
                    message = 'Your transaction is successful'
                else:
                    error = "Your transaction is being cancelled, Because your request more than your balance!"
            else:
                raise Http404("form does not exist")
        Context = {
			'data':data,
            'customers':customers,
            'error': error,
            'message': message,
		}
    except customer.DoesNotExist:
        raise Http404("Data does not exist")
    return render(request,'banksystem/profile.html', Context)

def transactions_records(request):
    try:
        data = transactionsTable.objects.all()
        Context = {
			'data':data,
		}
    except transactionsTable.DoesNotExist:
        raise Http404("Data does not exist")
    
    return render(request,'banksystem/transactions.html', Context)
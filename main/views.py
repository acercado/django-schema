from django.shortcuts import render
from .models import Account

# Create your views here.

def accounts(request):
    accounts_obj = Account.objects.all()
    return render(request, 'main/accounts.html', {'accounts': accounts_obj})
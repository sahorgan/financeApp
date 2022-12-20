from django.shortcuts import render

def account_list(request): return render(request, 'finance/account_list.html', {})

from django.shortcuts import redirect, render


def dash_index(request):        
    return render(request, 'dashboard/dashboard.html')
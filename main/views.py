from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306152393',
        'name': 'ARZAKA RAFFAN MAWARDI',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
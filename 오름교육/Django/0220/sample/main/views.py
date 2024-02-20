from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def notice(request):
    return render(request, "notice/notice.html")

def notice1(request):
    return render(request, "main/notice1.html")

def notice2(request):
    return render(request, "main/notice2.html")

def notice3(request):
    return render(request, "main/notice3.html")

def contact(request):
    return render(request, "main/conteac.html")

def abcd(request):
    return render(request, "main/abcd.html")

def vin(request):
    return render(request, "main/vin.html")

def notice2(request):
    return render(request, "main/mini.html")
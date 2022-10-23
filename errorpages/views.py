from django.shortcuts import render

# Create your views here.
# ==================== Errors =========================

def error_500(request):
    return render (request,"errorpages/error_500.html")

def error_404(request,exception):
    return render (request,"errorpages/error_404.html")

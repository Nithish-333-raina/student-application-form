from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentApplication

# Create your views here.


def student_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        course = request.POST.get('course')

        StudentApplication.objects.create(
            name=name,
            email=email,
            phone=phone,
            dob=dob,
            course=course
         )
        return HttpResponse(f"<h2>Thank you, {name}. Application received.</h2>")
    
    return render(request, 'application_form.html')

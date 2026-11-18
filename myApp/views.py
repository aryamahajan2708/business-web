from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse   
from .models import Person

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        city = request.POST.get('city')
        age = request.POST.get('age')
        email = request.POST.get('email')

        Person.objects.create(
            first_name = fname,
            last_name = lname,
            age = age,
            city = city,
            email = email   
        )
        return redirect('form')
    return render(request , 'form.html')

def data(request):
    per = Person.objects.all()
    return render(request , 'data.html' , {'persons': per})

def confirm_person(request):
    if request.method == 'POST':
        first_name = request.POST.get('fName')
        last_name = request.POST.get('lName')
        
        # Querying the database
        P = Person.objects.filter(
            first_name__iexact = first_name,
            last_name__iexact = last_name,
        )
        
        if P.count() == 1:
            p = P.first()  # Fixed: changed p.first() to P.first()
            return redirect('update_person', id=p.id)  # Fixed: changed P.id to p.id
            
        elif P.count() > 1:  # Fixed: changed < 1 to > 1 to match the error message
            return render(request, 'confirm.html', {
                'error': 'Multiple students found. Please use a unique student ID.'
            })
            
        else:  # This will handle exactly P.count() == 0
            return render(request, 'confirm.html', {
                'error': 'Student not found! Please check the name.'
            })
            
    return render(request, 'confirm.html')


def update_person(request, id):  # 1. Added id parameter here
    persons = get_object_or_404(Person, id=id)
    
    if request.method == 'POST':
        persons.first_name = request.POST.get('fName')
        persons.last_name = request.POST.get('lName')
        persons.age = request.POST.get('age')
        persons.city = request.POST.get('city')
        persons.email = request.POST.get('email')
        persons.save()
        return redirect('form')
    
    return render(request, 'update.html', {'persons': persons})

def delete_person(request, id):
    # ID ke basis par person ko dhoodhna aur delete karna
    person = get_object_or_404(Person, id=id)
    person.delete()
    
    # Delete hone ke baad wapas 'data' wale page par redirect karega
    return redirect('data') 
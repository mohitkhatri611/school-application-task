from .models import *
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse


def home(request):
    try:
        students = Students.objects.all().order_by('id')
        paginator = Paginator(students, 4)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)

        context = {
            'page_obj': page_obj
        }
        return render(request, "home.html", context)
    except:
        messages.error(request, "Database table is not created Run migrate command")
    return render(request, "home.html")


def add_student(request):
    if request.method != "POST":
        return render(request, 'add_student.html')
    else:
        name = request.POST.get('inputName')
        father_name = request.POST.get('inputFatherName')
        dob = request.POST.get('dob')

        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')

        pincode = request.POST.get('pincode')
        phone = request.POST.get('inputPhone')
        email = request.POST.get('email')
        class_opted = request.POST.get('classOpted')
        marks = request.POST.get('marks')

        email1 = Students.objects.filter(email=email).exists()
        ph = Students.objects.filter(phone=phone).exists()

        if email1 and ph:
            messages.add_message(request, messages.ERROR, 'Email should be unique')
            messages.add_message(request, messages.ERROR, 'Phone should be unique')
            return redirect("add_student")

        elif email1:
            messages.add_message(request, messages.ERROR, 'Email should be unique')
            return redirect("add_student")
        elif ph:
            messages.add_message(request, messages.ERROR, 'Phone should be unique')
            return redirect("add_student")
        else:

            try:
                student = Students(name=name, father_name=father_name, dob=dob, address=address, city=city, state=state, \
                                   pincode=pincode, phone=phone, email=email, class_opted=class_opted, marks=marks)
                student.save()
                messages.success(request, "Student Added Successfully!")
                return redirect('home')
            except:

                messages.error(request, "Failed to Add student!")
                return redirect('add_student')


@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = Students.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    inputPhone = request.POST.get("inputPhone")
    inputPhone = Students.objects.filter(phone=inputPhone).exists()
    if inputPhone:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def display_student(request, id):
    if request.method != "POST":
        student = Students.objects.get(id=id)
        context = {
            "student": student,
        }
        return render(request, 'edit_student.html', context)


def edit_student(request, id):
    if request.method != "POST":
        student = Students.objects.get(id=id)
        context = {
            "student": student,
        }
        return render(request, 'edit_student.html', context)
    else:
        name = request.POST.get('inputName')
        father_name = request.POST.get('inputFatherName')
        dob = request.POST.get('dob')

        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')

        pincode = request.POST.get('pincode')
        phone = request.POST.get('inputPhone')
        email = request.POST.get('email')
        class_opted = request.POST.get('classOpted')
        marks = request.POST.get('marks')

        try:
            subject = Students.objects.get(id=id)
            subject.name = name
            subject.father_name = father_name
            subject.dob = dob
            subject.address = address
            subject.city = city
            subject.state = state
            subject.pincode = pincode
            subject.phone = phone
            subject.email = email
            subject.class_opted = class_opted
            subject.marks = marks
            subject.save()

            messages.success(request, "Student Updated Successfully.")
            return HttpResponseRedirect(reverse("edit_student", kwargs={"id": id}))

        except:
            messages.error(request, "Failed to Update Student.")
            return HttpResponseRedirect(reverse("edit_student", kwargs={"id": id}))


from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect,render
from .forms import StudentForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.core.mail import send_mail
from .serializers import StudentSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
import random
from main.models import Student 
from .utils import generate_otp, send_otp_email
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

class StudentData(APIView):
    serializer_class = StudentSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                student = Student.objects.get(pk=pk)
                student_serializer = self.serializer_class(student)
                return Response({'status': 'success', 'student': student_serializer.data}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'status': 'failure', 'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            student_serializer = self.serializer_class(students, many=True)
            return Response({'status': 'success', 'students': student_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            student_serializer = self.serializer_class(data=request.data, context={'request': request})
            student_serializer.is_valid(raise_exception=True)
            student_serializer.save()
            response = {'status': 'success', 'message': "successfully posted", 'student_details': student_serializer.data}
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as error:
            response = {'status': 'failure', 'message': "retry", 'error': str(error)}
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student_serializer = self.serializer_class(student, data=request.data, partial=True)
            student_serializer.is_valid(raise_exception=True)
            student_serializer.save()
            return Response({'status': 'success', 'message': 'successfully updated', 'student_details': student_serializer.data}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'status': 'failure', 'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response({'status': 'success', 'message': 'successfully deleted'}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'status': 'failure', 'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)


def home(request):
    return render(request, 'main/Home.html')

def index(request):
    return render(request, 'main/Home.html')

def administration(request):
    return render(request, 'main/administration.html')

def admissions(request):
    return render(request, 'main/Admissions.html')

def departments(request):
    return render(request, 'main/departments.html')

def placements(request):
    return render(request, 'main/placements.html')

def research(request):
    return render(request, 'main/research.html')

def amenities(request):
    return render(request, 'main/amenities.html')

def activities(request):
    return render(request, 'main/activities.html')

def contact(request):
    return render(request, 'main/contact.html')

def dashboard(request):
    return render(request, "dashboard.html")

# Student Signup View
def student_signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            rollno = form.cleaned_data['rollno']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            # Saving the student data to database
            student = Student(
                name=name,
                rollno=rollno,
                age=age,
                email=email,
                phone=phone
            )
            student.save()

            messages.success(request, 'Student data has been saved successfully!')
            return redirect('student_signup')  # Redirect to the signup page or another page
        else:
            messages.error(request, 'There was an error with your signup form.')

    else:
        form = StudentForm()

    return render(request, 'main/student_signup.html', {'form': form})


# Student Login View
def student_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            messages.error(request, "Email not found!")
            return redirect("student_login")

        # Generate and save OTP for the student
        otp = random.randint(1000, 9999)  # Generate a 4-digit OTP
        student.otp = otp
        student.save()

        # Send OTP to email
        send_mail(
            "Your OTP Code",
            f"Your OTP is {otp}",
            "karrilokesh108@gmail.com",
            [email],
            fail_silently=False,
        )

        # Save the email in session for verification
        request.session["email"] = email
        return redirect("verify_otp")

    return render(request, "main/student_login.html")


# Verify OTP View
def verify_otp(request):
    if request.method == "POST":
        email = request.session.get("email")

        if not email:
            messages.error(request, "Session expired! Please login again.")
            return redirect("student_login")

        otp_entered = request.POST["otp"].strip()

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            messages.error(request, "Invalid session! Please login again.")
            return redirect("student_login")

        if student.otp == otp_entered:
            request.session["student_id"] = student.id  # Store session
            messages.success(request, "Login successful!")
            return render(request, "main/dashboard.html")  # Render dashboard directly
        else:
            messages.error(request, "Invalid OTP! Please try again.")
            return redirect("verify_otp")

    return render(request, "main/verify_otp.html")

def student_logout(request):
    logout(request)  # Logs out the user
    return redirect("student_login") 
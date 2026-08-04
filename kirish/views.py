from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
import logging
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Parollar bir xil emas')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu email allaqachon ro'yxatdan o'tgan")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu login allaqachon band")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz")
            return redirect('index')

        messages.error(request, "Noma'lum xatolik yuz berdi")
        return render(request, 'register.html')

    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        parol = request.POST.get("parol", "").strip()

        if not username:
            messages.warning(request, "Iltimos login kriting")
            messages.error(request, "username bosh")
            return redirect('login')
    
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                logger.info(f"Admin{user.username} login qildi")
                return redirect("home")
            else:
                if not parol:
                    messages.warning(request, "Iltimos parolni kriting")
                    messages.warning(request, "Parolni kriting")
                    return redirect("login")
                user = authenticate(request, username=username, password=parol)
                if user:
                    auth_login(request, user)
                    return redirect("index")
                else:
                    logger.warning(f"{user.username} login qilolmadi")
                    messages.error(request, "Parol xato")
                    return redirect("login")
        except User.DoesNotExist:
            logger.warning(f"{username} login qilinmadi")
            return redirect("login")

    return render(request, "login.html")

@login_required
def profil(request):
    return render(request, "profil.html", {
        "user": request.user
    })
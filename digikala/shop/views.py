from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Order
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, UpdateUserForm, AdditionalInfoForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import ProductSerializer

def category_summary(request):
    all_cat = Category.objects.all()
    return render(request, 'category_summary.html', {'category': all_cat})


def helloworld(request):
    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'index.html', {'products': all_products, 'categories': all_categories})
    #return HttpResponse(all_products)


def about(request):
    all_categories = Category.objects.all()
    return render(request, 'about.html', {'categories': all_categories})


def login_user(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        User = get_user_model()
        try:
            user = User.objects.get(username=phone_number)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید')
                return redirect('home')
            else:
                messages.error(request, 'اسم کاربری یا رمز اشتباه است')
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'کاربری با این شماره تلفن وجود ندارد')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد')
    return redirect('home')


def signup_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data.get('phone_number')  # Use phone number as username
            user.save()
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=phone_number, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'اکانت شما ساخته شد')
                return redirect('home')
            else:
                messages.error(request, 'مشکلی در ورود به سیستم وجود دارد')
                return redirect('signup')
        else:
            messages.error(request, 'ثبت نام انجام نشد')
            return redirect('signup')
    else:
        return render(request, 'signup.html', {'form': form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        categories = Category.objects.all()  # بارگذاری دسته‌بندی‌ها
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'پروفایل شما ویرایش شد')
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form, 'categories': categories})
    else:
        messages.error(request, 'ابتدا باید لاگین شوید!')
        return redirect('home')


def product(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})


def category(request, cat):
    cat = cat.replace('-', ' ')
    try:
        category = Category.objects.get(name=cat)
        products = Product.objects.filter(category=category)
        all_categories = Category.objects.all()
        return render(request, 'category.html', {'products': products, 'category': category,
                                                 'categories': all_categories})
    except:
        messages.error(request, 'دسته بندی وجود دارد')
        return redirect('home')




@login_required
def additional_info(request):
    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST, request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "اطلاعات شما با موفقیت ثبت شد")
            return redirect('home')
    else:
        form = AdditionalInfoForm(instance=request.user)
    return render(request, 'additional_info.html', {'form': form})


@login_required
def complete_profile(request):
    all_categories = Category.objects.all()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل شما تکمیل شد')
            return redirect('home')

    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'complete_profile.html', {'form': form})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category, Booking, Package, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, ProfileEditForm
from django.db.models import Q
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    
    return render(request, 'main/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        user = authenticate(request, username=username, password=password1)
        login(request, user)

        return redirect('index')

    return render(request, 'main/signup.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    categories = Category.objects.all()
    packages = Package.objects.all() 
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.GET.get('category_id'):
        category_id = request.GET.get('category_id')
        events = Category.objects.filter(id=category_id)
        package_id = request.POST.get('package')
        package = Package.objects.get(id=package_id)
        category_data = [
            {
                'id': category.id,
                'name': category.name,
                'image_url': category.image.url if category.image else None,
            }
            for category in events
        ]
        return JsonResponse(category_data, safe=False)

    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        date = request.POST.get('date')
        time = request.POST.get('time')

        booking = Booking(user=request.user, category=category, date=date, time=time)
        booking.save()

        messages.success(request, 'Booking successful!')
        return redirect('index')

    return render(request, 'main/index.html', {
        'categories': categories,
        'packages': packages,
    })


def category_bookings(request, category_id):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    category = get_object_or_404(Category, id=category_id)
    bookings = Booking.objects.filter(user=request.user, category=category)

    return render(request, 'main/category_bookings.html', {
        'category': category,
        'bookings': bookings,
    })


def category_events(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'main/category_events.html', {
        'category': category,
    })


def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    benefits_list = package.benefits.split('\n') if package.benefits else []

    return render(request, 'main/package_detail.html', {
        'package': package,
        'benefits_list': benefits_list,
    })


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    packages = event.category.packages.all()
    bookings = Booking.objects.filter(user=request.user, event=event)

    context = {
        'event': event,
        'bookings': bookings,
        'packages': packages,
    }

    return render(request, 'main/event_detail.html', context)


@login_required
def user_dashboard(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'main/user_dashboard.html', {
        'bookings': bookings
    })


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user, status='Confirmed')
    return render(request, 'main/user_bookings.html', {
        'bookings': bookings
    })


def search_events(request):
    query = request.GET.get('q')
    
    if query:
        events = Event.objects.filter(
            Q(title__icontains=query) | Q(location__icontains=query) | Q(description__icontains=query)
        )
    else:
        events = Event.objects.all()

    return render(request, 'main/search_results.html', {'events': events, 'query': query})


@login_required
def profile_edit(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_dashboard')
    else:
        form = ProfileEditForm(instance=user)
    
    return render(request, 'main/profile_edit.html', {
        'form': form
    })


def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        email = request.POST.get('Email')
        phone_number = request.POST.get('PhoneNumber')
        message = request.POST.get('Message')

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            message=message
        )
        contact.save()

        return redirect('success_page')

    return render(request, 'main/contact.html')


def success_page(request):
    return render(request, 'main/success.html')

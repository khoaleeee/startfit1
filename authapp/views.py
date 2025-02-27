from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import TrackedActivitie
from django.contrib.auth.decorators import login_required
from .forms import TrackedActivitieForm 
from django.http import HttpResponse
from django.http import JsonResponse
from .models import TrackedActivitie
from django.views.decorators.http import require_GET



# Create your views here.
def Home(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def profile(request):
    return render(request, "profile.html")

def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
        
        
    return render(request,"signup.html")

def handlelogin(request):
    if request.method=="POST":        
        username=request.POST.get('usernumber')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
            
        
    return render(request,"handlelogin.html")

def handleLogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")


def password_reset_view(request):
    context = {}

    # Depending on the step, set a flag for the template
    if 'password_reset_done' in request.GET:
        context['password_reset_done'] = True
    elif 'password_reset_confirm' in request.GET:
        context['password_reset_confirm'] = True
    elif 'password_reset_complete' in request.GET:
        context['password_reset_complete'] = True
    else:
        context['password_reset_done'] = False

    return render(request, 'password_reset.html', context)

# receive POST and send it to forms.py,
def calendar(request):
    if request.method == 'POST':
        form = TrackedActivitieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')  # Adjust the redirect as needed
    else:
        form = TrackedActivitieForm()

    activities = TrackedActivitie.objects.all()
    context = {
        'form': form,
        'activities': activities
    }
    return render(request, 'calendar.html', context)

@require_GET
def get_activities(request):
    year = int(request.GET.get('year'))
    month = int(request.GET.get('month'))

    # Fetch activities for the given month and year
    activities = TrackedActivitie.objects.filter(date__year=year, date__month=month)
    activities_dict = {}

    for activity in activities:
        date_str = activity.date.strftime('%Y-%m-%d')
        activities_dict[date_str] = {
            'type': activity.activity_type,
            'duration': activity.duration,
            'notes': activity.notes,
        }

    return JsonResponse({'activities': activities_dict})

def calendar_view(request):
    if request.method == 'POST':
        activityType = request.POST['activityType']
        duration = request.POST['duration']
        notes = request.POST['notes']
        date = request.POST['date']

        TrackedActivitie.objects.create(
            activityType=activityType,
            duration=duration,
            notes=notes,
            date=date
        )
        return redirect('calendar')  # Redirect to avoid form resubmission

    # Fetch all activities to display on the calendar
    activities = list(TrackedActivitie.objects.values())
    return render(request, 'calendar.html', {'activities': activities})

def database(request):
    all_activities = TrackedActivitie.objects.all
    return render(request, 'database.html', {'all':all_activities})

def calendar_view(request):
    return render(request, 'calendar/calendar.html')

def bench_press(request):
    return render(request, "Activities_Library/bench_press.html")

def squat(request):
    return render(request, "Activities_Library/squat.html")

def barbell_row(request):
    return render(request, "Activities_Library/barbell_row.html")
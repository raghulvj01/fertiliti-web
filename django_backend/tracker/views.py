from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import CycleEntry, MedicineReminder, Appointment, DietPlan, LifestyleLog


@login_required
def dashboard(request):
    user = request.user
    today = timezone.now().date()
    upcoming = Appointment.objects.filter(user=user, date__gte=today)[:3]
    medicines = MedicineReminder.objects.filter(user=user, active=True)[:3]
    last_cycle = CycleEntry.objects.filter(user=user).first()
    today_diet = DietPlan.objects.filter(user=user, date=today)
    context = {
        'upcoming_appointments': upcoming,
        'active_medicines': medicines,
        'last_cycle': last_cycle,
        'today_diet': today_diet,
        'today': today,
    }
    return render(request, 'fertiliti/dashboard.html', context)


@login_required
def cycle(request):
    if request.method == 'POST':
        end_date = request.POST.get('end_date') or None
        CycleEntry.objects.create(
            user=request.user,
            start_date=request.POST['start_date'],
            end_date=end_date,
            notes=request.POST.get('notes', ''),
        )
        return redirect('cycle')
    entries = CycleEntry.objects.filter(user=request.user)
    return render(request, 'fertiliti/cycle.html', {'entries': entries})


@login_required
def medicine(request):
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            MedicineReminder.objects.filter(
                id=request.POST.get('id'), user=request.user
            ).delete()
        else:
            MedicineReminder.objects.create(
                user=request.user,
                name=request.POST['name'],
                dosage=request.POST['dosage'],
                frequency=request.POST['frequency'],
                time=request.POST['time'],
            )
        return redirect('medicine')
    reminders = MedicineReminder.objects.filter(user=request.user)
    return render(request, 'fertiliti/medicine.html', {'reminders': reminders})


@login_required
def appointments(request):
    today = timezone.now().date()
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            Appointment.objects.filter(
                id=request.POST.get('id'), user=request.user
            ).delete()
        else:
            Appointment.objects.create(
                user=request.user,
                title=request.POST['title'],
                doctor=request.POST.get('doctor', ''),
                location=request.POST.get('location', ''),
                date=request.POST['date'],
                time=request.POST['time'],
                notes=request.POST.get('notes', ''),
            )
        return redirect('appointments')
    appts = Appointment.objects.filter(user=request.user)
    return render(request, 'fertiliti/appointments.html', {
        'appointments': appts,
        'today': today,
    })


@login_required
def diet(request):
    today = timezone.now().date()
    if request.method == 'POST':
        if request.POST.get('action') == 'delete':
            DietPlan.objects.filter(
                id=request.POST.get('id'), user=request.user
            ).delete()
        else:
            calories = request.POST.get('calories') or None
            DietPlan.objects.create(
                user=request.user,
                meal_type=request.POST['meal_type'],
                food_item=request.POST['food_item'],
                calories=calories,
                date=today,
            )
        return redirect('diet')
    plans = DietPlan.objects.filter(user=request.user, date=today)
    return render(request, 'fertiliti/diet.html', {'plans': plans, 'today': today})


@login_required
def lifestyle(request):
    today = timezone.now().date()
    if request.method == 'POST':
        sleep = request.POST.get('sleep_hours') or None
        exercise = request.POST.get('exercise_minutes') or None
        water = request.POST.get('water_glasses') or None
        stress = request.POST.get('stress_level') or None
        LifestyleLog.objects.update_or_create(
            user=request.user,
            date=today,
            defaults={
                'sleep_hours': sleep,
                'exercise_minutes': exercise,
                'water_glasses': water,
                'stress_level': stress,
                'notes': request.POST.get('notes', ''),
            }
        )
        return redirect('lifestyle')
    log = LifestyleLog.objects.filter(user=request.user, date=today).first()
    return render(request, 'fertiliti/lifestyle.html', {'log': log, 'today': today})


@login_required
def insights(request):
    user = request.user
    cycles = CycleEntry.objects.filter(user=user)[:6]
    logs = LifestyleLog.objects.filter(user=user)[:7]
    age = None
    try:
        from accounts.models import UserProfile
        profile = UserProfile.objects.get(user=user)
        age = profile.age
    except Exception:
        pass
    return render(request, 'fertiliti/insights.html', {
        'cycles': cycles,
        'logs': logs,
        'age': age,
    })

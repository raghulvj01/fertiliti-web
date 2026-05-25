from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


def get_fallback_reply(message):
    msg = message.lower()
    if any(w in msg for w in ['cycle', 'period', 'menstrual', 'ovulation']):
        return "Your menstrual cycle is key to understanding fertility. A typical cycle is 21-35 days. Ovulation usually occurs around day 14. Log your cycle in the Cycle Tracking section!"
    if any(w in msg for w in ['diet', 'food', 'eat', 'nutrition', 'meal']):
        return "A fertility-boosting diet includes folate-rich foods (spinach, lentils), healthy fats (avocado, nuts), antioxidants (berries) and lean protein (eggs, fish). Log your meals in Diet Plans!"
    if any(w in msg for w in ['medicine', 'pill', 'supplement', 'vitamin', 'folic']):
        return "Common fertility supplements: Folic Acid (400-800 mcg/day), Vitamin D (1000 IU/day), CoQ10 (200mg/day). Always consult your doctor first. Set reminders in the Medicine section!"
    if any(w in msg for w in ['stress', 'anxiety', 'relax', 'meditation', 'yoga']):
        return "High stress can suppress ovulation. Try daily meditation, deep breathing or yoga. Aim for 7-9 hours sleep. Log your stress levels in the Lifestyle section!"
    if any(w in msg for w in ['sleep', 'tired', 'rest']):
        return "Sleep is vital for reproductive health! Aim for 7-9 hours per night. Keep a consistent sleep schedule and avoid screens 1 hour before bed. Track your sleep in Lifestyle!"
    if any(w in msg for w in ['exercise', 'workout', 'walk', 'fitness']):
        return "Moderate exercise supports fertility. 30 min of walking, swimming or yoga 5x per week is ideal. Avoid extreme high-intensity training when trying to conceive."
    if any(w in msg for w in ['appointment', 'doctor', 'clinic', 'specialist']):
        return "Regular check-ups are important! See your gynaecologist every 6-12 months. Consider a fertility specialist if trying for 12+ months. Track appointments in the Appointments section!"
    if any(w in msg for w in ['age', 'fertility', 'older', '30', '35', '40']):
        return "Fertility by age: Under 25 (~25% per cycle), 25-29 (~22%), 30-34 (~18%), 35-39 (~12%), 40+ (~5%). Check your personalised insights in the Insights page!"
    if any(w in msg for w in ['water', 'hydration', 'drink']):
        return "Stay hydrated! Aim for 8-10 glasses of water daily. Good hydration supports cervical mucus quality and hormonal balance. Log water intake in Lifestyle!"
    return "Hello! I am your FertiliCare AI assistant. I can help with your cycle, diet, medicines, appointments, lifestyle and fertility insights. What would you like to know?"


@login_required
@require_POST
def chat(request):
    try:
        body = request.body.decode('utf-8')
        if not body:
            return JsonResponse({'reply': 'Please type a message.'})

        import json

        payload = json.loads(body)
        message = payload.get('message', '').strip()
        if not message:
            return JsonResponse({'reply': 'Please type a message.'})

        return JsonResponse({'reply': get_fallback_reply(message)})

    except Exception:
        return JsonResponse({'reply': 'Something went wrong. Please try again.'})

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    user: str = "anonymous"


class ChatResponse(BaseModel):
    reply: str


RESPONSES = {
    ('cycle', 'period', 'menstrual', 'ovulation', 'fertile'):
        "Your menstrual cycle is key to understanding fertility. A typical cycle is 21-35 days. Ovulation usually occurs around day 14 of a 28-day cycle. Tracking your cycle helps predict your fertile window. Log your start date regularly for better predictions!",
    ('diet', 'food', 'eat', 'nutrition', 'meal', 'calories'):
        "A fertility-boosting diet should include:\n✅ Folate-rich foods: leafy greens, lentils, beans\n✅ Healthy fats: avocado, olive oil, nuts\n✅ Antioxidants: berries, tomatoes, bell peppers\n✅ Lean protein: eggs, fish, chicken\n❌ Limit: processed foods, excess sugar, alcohol\nLog your meals in the Diet Plans section!",
    ('medicine', 'medication', 'pill', 'supplement', 'vitamin', 'folic'):
        "Common fertility supplements:\n💊 Folic Acid (400-800 mcg/day) - reduces neural tube defects\n💊 Vitamin D (1000-2000 IU/day) - hormonal balance\n💊 CoQ10 (200-600 mg/day) - egg quality\n💊 Iron and Omega-3 fatty acids\nAlways consult your doctor first. Set reminders in the Medicine section!",
    ('stress', 'anxiety', 'relax', 'meditation', 'yoga'):
        "Stress can affect hormone levels and fertility. Tips:\n🧘 Practice yoga or meditation daily (even 10 minutes helps)\n😴 Prioritise 7-9 hours of quality sleep\n🚶 Light exercise like walking reduces cortisol\n📝 Journaling helps process emotions\nLog your stress levels in the Lifestyle section!",
    ('sleep', 'rest', 'tired', 'fatigue'):
        "Sleep is vital for reproductive health!\n✅ Aim for 7-9 hours per night\n✅ Keep a consistent sleep schedule\n✅ Avoid screens 1 hour before bed\n✅ Keep your room cool and dark\nTrack your sleep hours in the Lifestyle section!",
    ('exercise', 'workout', 'gym', 'walk', 'fitness'):
        "Moderate exercise supports fertility!\n✅ 30 min of moderate activity 5 days per week\n✅ Best types: walking, swimming, yoga, cycling\n❌ Avoid extreme high-intensity training when trying to conceive\nLog your exercise minutes in the Lifestyle section!",
    ('appointment', 'doctor', 'clinic', 'specialist', 'gynecologist'):
        "Regular medical check-ups are essential!\n📅 See your gynaecologist every 6-12 months\n📅 Consider a fertility specialist if trying for 12+ months\n📅 Ask about: hormone panel, ultrasound, AMH level\nTrack all appointments in the Appointments section!",
    ('age', 'older', '30', '35', '40', 'fertility rate'):
        "Fertility and age:\n👶 Under 25: Peak fertility, ~25% chance per cycle\n👶 25-29: High fertility, ~22% per cycle\n👶 30-34: Good fertility, ~18% per cycle\n👶 35-39: Moderate decline, ~12% per cycle\n👶 40+: ~5% per cycle - specialist guidance recommended\nCheck your Insights page for personalised information!",
    ('water', 'hydration', 'drink'):
        "Staying hydrated supports fertility!\n💧 Aim for 8-10 glasses of water per day\n💧 Herbal teas are good options\n💧 Avoid excessive caffeine and alcohol\nLog your water intake in the Lifestyle section!",
}


def get_reply(message: str) -> str:
    msg = message.lower()
    for keywords, reply in RESPONSES.items():
        if any(kw in msg for kw in keywords):
            return reply
    return (
        "Hello! I am your FertiliCare AI assistant.\n\n"
        "I can help you with:\n"
        "📅 Menstrual cycle and ovulation tracking\n"
        "💊 Medicines and supplements\n"
        "🏥 Appointments and doctor visits\n"
        "🥗 Personalised diet plans\n"
        "🧘 Lifestyle and stress management\n"
        "📊 Age-based fertility insights\n\n"
        "What would you like to know?"
    )


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    return ChatResponse(reply=get_reply(req.message))

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()


class InsightRequest(BaseModel):
    age: Optional[int] = None
    avg_cycle_length: Optional[float] = None
    avg_sleep: Optional[float] = None
    stress_level: Optional[int] = None


class InsightResponse(BaseModel):
    fertility_status: str
    recommendations: List[str]
    risk_flags: List[str]


@router.post("/insights", response_model=InsightResponse)
def get_insights(req: InsightRequest):
    recommendations = []
    risk_flags = []
    fertility_status = "Good"

    if req.age:
        if req.age < 25:
            fertility_status = "Peak fertility range"
            recommendations.append("Maintain a healthy lifestyle to preserve fertility.")
        elif req.age < 30:
            fertility_status = "High fertility"
            recommendations.append("Great time to plan. Consider tracking cycles consistently.")
        elif req.age < 35:
            fertility_status = "Good fertility"
            recommendations.append("Consider a fertility check-up if planning in the next 2 years.")
        elif req.age < 40:
            fertility_status = "Moderate fertility"
            risk_flags.append("Fertility declines more rapidly after 35.")
            recommendations.append("Consult a specialist sooner rather than later.")
        else:
            fertility_status = "Advanced maternal age"
            risk_flags.append("Advanced maternal age — specialist guidance strongly recommended.")
            recommendations.append("Discuss AMH levels and egg quality with your doctor.")

    if req.avg_cycle_length:
        if req.avg_cycle_length < 21:
            risk_flags.append("Short cycles may indicate hormonal imbalance.")
        elif req.avg_cycle_length > 35:
            risk_flags.append("Long cycles may indicate PCOS or thyroid issues.")
        else:
            recommendations.append("Your cycle length is within the normal range. Keep tracking!")

    if req.avg_sleep:
        if req.avg_sleep < 6:
            risk_flags.append("Poor sleep disrupts reproductive hormones.")
            recommendations.append("Prioritise 7-9 hours of sleep per night.")
        elif req.avg_sleep >= 7:
            recommendations.append("Your sleep pattern looks healthy. Keep it up!")

    if req.stress_level:
        if req.stress_level >= 7:
            risk_flags.append("High stress levels can suppress ovulation.")
            recommendations.append("Try mindfulness, yoga, or speaking to a counsellor.")
        elif req.stress_level <= 3:
            recommendations.append("Great stress management! This positively supports fertility.")

    if not recommendations:
        recommendations.append("Keep logging data to receive personalised insights.")

    return InsightResponse(
        fertility_status=fertility_status,
        recommendations=recommendations,
        risk_flags=risk_flags,
    )

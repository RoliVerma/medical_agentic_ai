# print("STATE FILE LOADED")
from typing import TypedDict, Dict, List

class MedicalState(TypedDict):
    image_path: str
    predictions: Dict[str, float]
    heatmap_path: str
    reasoning: str
    report: str
    confidence: float
    flags: List[str]
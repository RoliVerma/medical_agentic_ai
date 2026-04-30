# print("STATE FILE LOADED")
from typing_extensions import TypedDict
from typing import Dict, List

class MedicalState(TypedDict):
    image_path: str
    predictions: Dict[str, float]
    heatmap_path: str
    
    reasoning: str
    second_opinion: str
    final_reasoning: str
    
    report: str
    confidence: float
    flags: List[str]
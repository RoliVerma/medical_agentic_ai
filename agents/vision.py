import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision import models

# Load pretrained DenseNet
model = models.densenet121(pretrained=True)
model.eval()

labels = ["Pneumonia", "Effusion", "No Finding"]

def vision_agent(state):
    image = Image.open(state["image_path"]).convert("RGB")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    x = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(x)
        probs = torch.sigmoid(outputs)[0]

    predictions = {
        labels[i]: float(probs[i]) for i in range(len(labels))
    }

    confidence = max(predictions.values())

    return {
        "predictions": predictions,
        "confidence": confidence
    }
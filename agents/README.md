

            ┌──────────────┐
            │ Chest X-ray  │
            └──────┬───────┘
                   ↓
        ┌────────────────────┐
        │ Vision Model Agent │
        │ (DenseNet/ViT)     │
        └────────┬───────────┘
                 ↓
        Predicted Labels + Confidence
                 ↓
        ┌────────────────────┐
        │ Reasoning Agent    │ (LLM)
        │ (Clinical logic)   │
        └────────┬───────────┘
                 ↓
        ┌────────────────────┐
        │ Report Agent       │
        │ (Structured output)│
        └────────┬───────────┘
                 ↓
        Final Medical Report

![Streamlit Output](image.png)
![Streamliy Output](image-1.png)
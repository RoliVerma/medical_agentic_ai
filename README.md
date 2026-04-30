# AI Radiology Workstation

An agentic AI system for chest X-ray analysis that combines computer vision and multi-agent reasoning to generate clinically structured radiology reports.

This project demonstrates a **stateful, multi-agent workflow** using **LangGraph**, where multiple AI agents collaborate to analyze medical images, reason about findings, and produce interpretable outputs in a **radiology-style format**.

## Features
- 🧠 Multi-agent AI pipeline using LangGraph
- 🔁 Conditional routing with second-opinion reasoning
- 🩺 Radiology-style structured reporting
- 📊 Confidence-aware decision making
- 🧭 Transparent workflow timeline (step-by-step logs)
- 💻 Fully local LLM inference using Ollama (no API cost)
- 🎨 Radiology workstation-style UI built with Streamlit

## Tech Stack
- Frontend: Streamlit
- Orchestration: LangGraph
- Vision Model: PyTorch (DenseNet baseline)
- LLM: Ollama (llama3)
- Language: Python

---

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/RoliVerma/medical_agentic_ai.git
cd medical_agentic_ai

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
```

```
## Install Dependencies and 
pip install -r requirements.txt
```
```
## Run local LLM using Ollama
brew install ollama   # macOS (use appropriate installer for your OS)
ollama pull llama3
ollama serve
```

## Usage
```
## Run the Streamlit application:
streamlit run app.py
```
### How it works
- Upload a medical scan image (example-chest X-ray)
- Click "Analyze" button
- The system executes a multi-agent workflow:
- **Vision Agent** → Predicts medical conditions from the image
- **Explainability Agent** → Highlights relevant regions
- **Reasoning Agent** → Generates clinical interpretation
- **Second Opinion Agent** → Triggered if confidence is low
- **Merge Agent** → Combines multiple opinions
- **Report Agent** → Produces structured radiology report
- **Validation Agent** → Flags uncertainty and safety issues

### Project Structure
```
medical-agentic-ai/
│
├── app.py
├── graph.py
├── state.py
│
├── agents/
│   ├── vision.py
│   ├── explain.py
│   ├── reasoning.py
│   ├── second_opinion.py
│   ├── merge.py
│   ├── report.py
│   ├── validate.py
│   └── router.py
│
├── utils/
│   └── gradcam.py
│
└── requirements.txt
```
## Contributing

Pull requests are welcome. For changes, please open an issue first
to discuss what you would like to change.

## Disclaimer

This project is for research and educational purposes only.
It is not intended for clinical use or real-world medical decision-making.

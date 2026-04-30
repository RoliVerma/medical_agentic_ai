import streamlit as st
from graph import app
import time

st.set_page_config(layout="wide")

# -------------------------------
# HEADER
# -------------------------------
st.markdown("## 🩺 AI Radiology Workstation")
st.markdown("### Chest X-ray Analysis System")
st.markdown("---")

# -------------------------------
# LAYOUT: LEFT PANEL + MAIN VIEWER
# -------------------------------
left_panel, main_panel = st.columns([1, 3])

# -------------------------------
# LEFT PANEL (Controls + Logs)
# -------------------------------
with left_panel:
    st.markdown("### 📂 Case Input")

    uploaded_file = st.file_uploader("Upload X-ray", type=["png", "jpg", "jpeg"])
    run_button = st.button("▶ Analyze")

    st.markdown("---")

    # 🔥 Workflow Log (NOW UNDER INPUT)
    st.markdown("### 🧭 Workflow Progress")
    log_display = st.empty()

    st.markdown("---")

    st.markdown("### 📊 Case Info")
    confidence_box = st.empty()
    flags_box = st.empty()

# -------------------------------
# MAIN IMAGE VIEWER
# -------------------------------
with main_panel:
    st.markdown("### 🖼️ Image Viewer")
    image_placeholder = st.empty()

# -------------------------------
# BOTTOM PANEL (Tabs)
# -------------------------------
st.markdown("---")
tabs = st.tabs([
    "🧠 Reasoning",
    "🧠 Second Opinion",
    "📊 Final Interpretation",
    "🧾 Report"
])

reasoning_tab, second_tab, final_tab, report_tab = tabs

# -------------------------------
# WORKFLOW LOG FUNCTION
# -------------------------------
logs = []

def log(step):
    logs.append(step)
    log_display.markdown("\n".join([f"- {l}" for l in logs]))

# -------------------------------
# RUN PIPELINE
# -------------------------------
if uploaded_file and run_button:

    # Save uploaded file
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    # Display image
    image_placeholder.image("temp.jpg", width="stretch")

    # Initial state
    state = {
        "image_path": "temp.jpg",
        "predictions": {},
        "heatmap_path": "",
        "reasoning": "",
        "second_opinion": "",
        "final_reasoning": "",
        "report": "",
        "confidence": 0.0,
        "flags": []
    }

    # Reset logs
    logs.clear()

    # -------------------------------
    # SIMULATED STEP-BY-STEP LOGGING
    # -------------------------------
    log("🧠 Running vision model...")
    time.sleep(0.3)

    log("🔍 Generating explainability map...")
    time.sleep(0.3)

    log("🧠 Performing initial reasoning...")
    time.sleep(0.3)

    # -------------------------------
    # RUN ACTUAL GRAPH
    # -------------------------------
    with st.spinner("Processing case..."):
        result = app.invoke(state)

    # -------------------------------
    # CONDITIONAL LOGIC (Agent Behavior)
    # -------------------------------
    if result["confidence"] < 0.6:
        log("⚠️ Low confidence detected → triggering second opinion")
    else:
        log("✅ High confidence → skipping second opinion")

    log("🧾 Generating report...")
    log("✅ Analysis complete")

    # -------------------------------
    # LEFT PANEL UPDATES
    # -------------------------------
    confidence = result["confidence"]

    if confidence > 0.8:
        confidence_box.success(f"Confidence: {confidence:.2f}")
    elif confidence > 0.5:
        confidence_box.warning(f"Confidence: {confidence:.2f}")
    else:
        confidence_box.error(f"Confidence: {confidence:.2f}")

    if result["flags"]:
        flags_box.warning(result["flags"])

    # -------------------------------
    # TABS CONTENT
    # -------------------------------
    with reasoning_tab:
        st.markdown("### 🧠 Initial Reasoning")
        st.write(result.get("reasoning", "No output"))

    with second_tab:
        st.markdown("### 🧠 Second Opinion")

        if result.get("second_opinion"):
            st.write(result["second_opinion"])
        else:
            st.info(
                "Agent chose not to use second opinion since initial reasoning achieved high confidence."
            )

    with final_tab:
        st.markdown("### 📊 Final Interpretation")
        st.write(result.get("final_reasoning", result.get("reasoning", "")))

    with report_tab:
        st.markdown("### 🧾 Radiology Report")
        st.write(result.get("report", "No report generated"))
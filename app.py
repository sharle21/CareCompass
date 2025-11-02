import streamlit as st

# --- Page Setup ---
st.set_page_config(layout="wide")
st.title("🏥 In-Network Care Navigator")
st.warning("This tool is a prototype and does not provide real medical advice.")

# --- Inputs (Now on the main page) ---
st.header("1. Enter Your Information")

# Use columns to organize the inputs
col1, col2 = st.columns(2)

with col1:
    insurance_plan = st.text_input("Your Insurance Plan (e.g., Aetna PPO)")
    
with col2:
    location = st.text_input("Your Location (e.g., College Park, MD)")

st.header("2. Describe Your Symptoms")
symptom_text = st.text_area(
    "Describe your symptoms (e.g., 'I have a fever and a bad cough')",
    height=150,
    label_visibility="collapsed" # Hides the "Describe Your Symptoms" label above the box
)

st.divider() # Adds a nice line

# --- Main Content Area for Results ---
if st.button("Find Care Options"):
    
    # 1. Check if inputs are filled
    if not insurance_plan or not location or not symptom_text:
        st.error("Please fill in all fields before proceeding.")
    
    else:
        # 2. Show that we're working
        st.info("Processing... Please wait.")
        
        # --- Debug Info (Phase 1) ---
        st.write(f"**Debug Info:**")
        st.write(f"* **Plan:** {insurance_plan}")
        st.write(f"* **Location:** {location}")
        st.write(f"* **Symptoms Input:** {symptom_text}") 

        # 3. Placeholder for final output
        st.markdown("---")
        st.header("3. Your Personalized Care Plan:")
        
        with st.spinner("Finding options..."):
            import time
            time.sleep(3) # Simulate work
            st.markdown("> **(Placeholder)** This is where the Gemini response will go.")
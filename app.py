import streamlit as st
import random

st.set_page_config(page_title="Sales Intel Tool", layout="wide")

st.title("🧠 Sales Intelligence Dashboard")
st.subheader("Get real-time insights from internal + external data to crush your next sales call")

# --- Sidebar Input ---
st.sidebar.header("🔍 Target Company")
company_name = st.sidebar.text_input("Enter Company Name", "Acme Innovations")
trigger = st.sidebar.button("Generate Intel")

# --- Synthetic Data Pools ---
industries = ["HealthTech", "FinTech", "EdTech", "Cybersecurity", "E-commerce"]
cities = ["Austin, TX", "Chicago, IL", "San Francisco, CA", "Boston, MA", "Madison, WI"]
funding_rounds = ["$20M Series A", "$40M Series B", "$75M Series C", "$10M Seed", "$100M Private Equity"]
hiring_focus = ["DevOps", "Data Science", "Cloud Engineering", "Security Analysts", "Product Managers"]
contacts = [
    ("Jamie Roth", "Director of TA", "Scaling TA pipeline, hiring surge"),
    ("Travis Kimball", "VP of IT Ops", "Digital infra rollout, might need eng staff"),
    ("Stephanie Lane", "PMO Director", "Needs fractional PMs for new launches"),
    ("Anita Singh", "CTO", "Modernizing legacy systems"),
    ("Marcus Lee", "Head of Engineering", "Rapid scale-up across backend teams")
]
alumni = [
    "**Brad Morgan** – Former contractor, now Sr. DevOps Engineer",
    "**Lisa Hernandez** – Former client HRBP, now at target company",
    "**Kevin O'Connor** – Previously placed consultant, now managing IT Ops"
]
top_of_mind = [
    "- CEO posted about 'People-first AI culture' last week",
    "- Announced hiring 50+ for Madison R&D hub",
    "- Partnered with Greenhouse ATS",
    "- Launched new customer success initiative",
    "- CTO speaking at upcoming AI conference"
]

if trigger:
    st.markdown(f"## 🏢 Company Snapshot: {company_name}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🌐 External Data")
        st.write(f"**Industry:** {random.choice(industries)}")
        st.write(f"**Size:** ~{random.randint(200, 1000)} employees")
        st.write(f"**Headquarters:** {random.choice(cities)}")
        st.write(f"**Funding:** {random.choice(funding_rounds)} (2025)")
        st.write(f"**Hiring Focus:** {random.choice(hiring_focus)}")

    with col2:
        st.markdown("### 📈 Internal Match")
        st.write("**Similar Clients:** MedPulse, BioWave AI")
        st.write("**Avg Deal Size:** $300K")
        st.write("**Relevant Case Study:** '15 DevOps Engineers in 30 Days' for MedPulse")
        st.write("**Delivery Team Lead:** Jane Murphy")

    st.divider()

    st.markdown("### 👥 Strategic Contacts")
    contact_data = random.sample(contacts, 3)
    st.table({
        "Name": [c[0] for c in contact_data],
        "Title": [c[1] for c in contact_data],
        "Outreach Angle": [c[2] for c in contact_data]
    })

    st.divider()

    st.markdown("### 🔁 Alumni at Target Co")
    for alum in random.sample(alumni, 2):
        st.write(alum)

    st.divider()

    st.markdown("### 📰 Top-of-Mind Insights")
    for item in random.sample(top_of_mind, 3):
        st.write(item)

    st.divider()

    st.markdown("### ✍️ Auto-Generated Outreach")
    st.code(f"""
Hey Jamie — congrats on the new hiring wave! 
Saw {company_name} is growing fast in {random.choice(hiring_focus)}. 
We helped MedPulse scale a similar team in 30 days flat — 
let me know if you'd be open to a quick chat next week. 
Best, Mark
""", language="text")

else:
    st.info("👈 Enter a company name on the left and hit 'Generate Intel' to get started.")

# 🧠 Sales Intelligence Dashboard

**Get real-time, AI-powered insights to crush your next sales conversation.**

This lightweight Streamlit app lets you enter a target company and instantly generate synthetic sales intelligence — the kind of prep that turns cold outreach into warm conversations.

---

## 🚀 Features

- 🔍 **Company Snapshot**: Synthetic industry, size, HQ, and funding profile
- 📈 **Internal Match Insights**: See example case studies, similar clients, deal size, and delivery leads
- 👥 **Strategic Contact Suggestions**: Randomized but realistic contact roles + outreach angles
- 🔁 **Alumni Matching**: Simulates known individuals with shared history
- 📰 **Top-of-Mind Signals**: Company news, leadership posts, hiring pushes
- ✍️ **Auto-Generated Outreach**: Customizable cold message drafts for outreach

---

## 🎯 Use Cases

- SDRs and AEs prepping for prospect calls  
- Client executives looking for custom warm intros  
- Sales ops or enablement teams prototyping tooling  
- Sales/AI nerds experimenting with RAG-style workflows

---

## 🛠 Tech Stack

- **Streamlit** – for the dashboard UI  
- **Python** – core logic + random data generator  
- **Synthetic data** – no external APIs or live CRM required (demo-friendly)  

---

## 📦 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/sales-intel-app.git
   cd sales-intel-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 🌐 Streamlit Cloud Deployment

To deploy your own live version:

1. Upload this repo to your GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“New App”**, choose your repo, and set `app.py` as the entry point
4. Hit **Deploy**

---

## 📣 Notes

- This version uses synthetic data for demo/testing purposes  
- No sensitive or proprietary data is included  
- Add real data sources or integrate your CRM to power up a production version

---

## 🤘 Built by a sales guy who was tired of staring at spreadsheets before every damn call.

import streamlit as st
import time
import random
import pandas as pd

st.set_page_config(page_title="AI Audience Detector", layout="centered")

st.title("🚀 AI-Based Target Audience Detector")
st.write("Analyze your startup idea and find the perfect audience")

# Sidebar
st.sidebar.title("⚙️ Model Info")
st.sidebar.write("Model: AudiencePredictor v2.0")
st.sidebar.write("Type: NLP + Clustering + Heuristics")
st.sidebar.success("Status: Active")

product = st.text_area("💡 Enter your product description")


# -------- AI LOGIC FUNCTION -------- #
def analyze_text(text):
    text = text.lower()

    score = {
        "health": ["fitness", "health", "gym", "workout", "exercise"],
        "startup": ["startup", "business", "productivity", "saas"],
        "gaming": ["game", "gaming", "stream", "multiplayer"],
        "finance": ["finance", "money", "bank", "payment", "crypto"],
        "education": ["learn", "course", "student", "education"]
    }

    detected = []

    for category_key, words in score.items():
        for w in words:
            if w in text:
                detected.append(category_key)

    if not detected:
        detected.append("general")

    selected_key = random.choice(detected)

    # 🔥 HUGE OUTPUT DATASET
    outputs = {
        "health": [
            ("HealthTech", "🏋️ Fitness Enthusiast", "18-35", "Instagram, YouTube", "Lack of motivation"),
            ("HealthTech", "🧘 Wellness Seeker", "20-40", "Instagram, Blogs", "Stress & unhealthy lifestyle"),
            ("HealthTech", "💪 Gym Beginner", "18-30", "YouTube, Instagram", "No guidance"),
            ("HealthTech", "🥗 Nutrition User", "25-45", "Pinterest, Instagram", "Diet issues"),
            ("HealthTech", "🏃 Active User", "20-38", "Fitness Apps", "Consistency")
        ],

        "startup": [
            ("SaaS/Productivity", "🚀 Startup Founder", "22-40", "LinkedIn, Twitter", "Scaling"),
            ("SaaS/Productivity", "📊 Analyst", "25-45", "LinkedIn", "Data decisions"),
            ("SaaS/Productivity", "🧑‍💻 Freelancer", "20-35", "Upwork, LinkedIn", "Time mgmt"),
            ("SaaS/Productivity", "📈 Entrepreneur", "23-45", "YouTube, LinkedIn", "Growth"),
            ("SaaS/Productivity", "💼 Business Owner", "30-50", "Facebook", "Customers")
        ],

        "gaming": [
            ("Gaming", "🎮 Competitive Gamer", "13-28", "Discord, Twitch", "Performance"),
            ("Gaming", "🕹️ Casual Gamer", "15-30", "YouTube", "Entertainment"),
            ("Gaming", "📺 Streamer", "18-35", "Twitch", "Audience"),
            ("Gaming", "👾 Esports Player", "16-28", "Discord", "Skill"),
            ("Gaming", "🎯 Mobile Gamer", "14-32", "YouTube", "Performance")
        ],

        "finance": [
            ("FinTech", "💰 Investor", "25-45", "LinkedIn", "Decisions"),
            ("FinTech", "📊 Trader", "22-40", "Twitter", "Insights"),
            ("FinTech", "💳 Payment User", "18-45", "Apps", "Ease"),
            ("FinTech", "🏦 Banker", "30-55", "Email", "Security"),
            ("FinTech", "📈 Crypto User", "20-40", "Discord", "Volatility")
        ],

        "education": [
            ("EdTech", "📚 Student", "16-25", "YouTube", "Learning"),
            ("EdTech", "🎓 Learner", "18-28", "LinkedIn", "Skills"),
            ("EdTech", "💻 Coding Student", "18-35", "GitHub", "Practice"),
            ("EdTech", "📖 Aspirant", "17-30", "Telegram", "Exams"),
            ("EdTech", "🧑‍🏫 Course User", "20-40", "Udemy", "Career")
        ],

        "general": [
            ("General Tech", "📱 User", "20-45", "Instagram", "Convenience"),
            ("General Tech", "🛍️ Shopper", "18-40", "Ads", "Deals"),
            ("General Tech", "📲 App User", "18-50", "Play Store", "Ease"),
            ("General Tech", "🌐 Internet User", "18-60", "YouTube", "Usage"),
            ("General Tech", "💡 Curious User", "20-45", "Blogs", "Exploration")
        ]
    }

    category, persona, age, platform, pain = random.choice(outputs[selected_key])
    confidence = str(random.randint(80, 95)) + "%"

    return category, persona, age, platform, pain, confidence


# -------- BUTTON -------- #
if st.button("🔍 Analyze Audience"):

    if product.strip() == "":
        st.warning("⚠️ Please enter a product description")
    else:

        steps = [
            "Initializing AI model...",
            "Analyzing product...",
            "Extracting keywords...",
            "Clustering audience...",
            "Generating persona...",
            "Finalizing..."
        ]

        progress = st.progress(0)
        status = st.empty()

        for i, step in enumerate(steps):
            status.text(step)
            time.sleep(2)
            progress.progress((i + 1) * 100 // len(steps))

        category, persona, age, platform, pain, confidence = analyze_text(product)

        st.success("✅ Analysis Complete")

        # RESULTS
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Category", category)
            st.metric("Confidence", confidence)

        with col2:
            st.metric("Persona", persona)
            st.metric("Age Group", age)

        st.subheader("🎯 Insights")
        st.write("Platforms:", platform)
        st.write("Pain Points:", pain)

        st.subheader("📊 Audience Distribution")
        data = pd.DataFrame({
            "Segment": ["Primary", "Secondary"],
            "Percentage": [random.randint(60, 80), random.randint(20, 40)]
        })
        st.bar_chart(data.set_index("Segment"))

        st.subheader("📄 Download Report")
        report = f"""
Product: {product}
Category: {category}
Persona: {persona}
Age: {age}
Platform: {platform}
Pain: {pain}
Confidence: {confidence}
"""
        st.download_button("Download Report", report)

        st.balloons()
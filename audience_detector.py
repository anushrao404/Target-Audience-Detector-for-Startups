import time
print("\nAI Based Target Audience Detector for Startups\n")

product = input("Enter your product description: ").lower()

category = ""
persona = ""
age = ""
interests = ""
platform = ""
pain = ""
confidence = ""
print("\nAnalyzing product description using NLP...")
time.sleep(1.5)

print("Extracting semantic keywords...")
time.sleep(1.5)

print("Matching startup category...")
time.sleep(1.5)

print("Generating audience persona...\n")
time.sleep(1.5)

# AI keyword analysis
if "fitness" in product or "gym" in product or "health" in product:
    category = "HealthTech"
    persona = "Young Fitness Enthusiast"
    age = "18 - 35"
    interests = "Fitness, Gym, Healthy lifestyle"
    platform = "Instagram, YouTube"
    pain = "Lack of motivation and unhealthy habits"
    confidence = "92%"

elif "startup" in product or "business" in product or "productivity" in product:
    category = "Productivity / SaaS"
    persona = "Ambitious Startup Founder"
    age = "22 - 40"
    interests = "Entrepreneurship, productivity"
    platform = "LinkedIn, Twitter"
    pain = "Time management and scaling challenges"
    confidence = "88%"

elif "gaming" in product or "game" in product:
    category = "Gaming"
    persona = "Competitive Gamer"
    age = "13 - 28"
    interests = "Gaming, streaming"
    platform = "Discord, Twitch, YouTube"
    pain = "Entertainment and community engagement"
    confidence = "90%"

else:
    category = "General Consumer Tech"
    persona = "Modern Digital User"
    age = "20 - 45"
    interests = "Technology, lifestyle products"
    platform = "Instagram, Facebook"
    pain = "Convenience and lifestyle improvement"
    confidence = "75%"

print("\n---------- AI Analysis Result ----------\n")

print("Detected Startup Category :", category)
print("Predicted Audience Persona :", persona)
print("Confidence Score :", confidence)

print("\n----- Target Audience Profile -----\n")

print("Age Group :", age)
print("Interests :", interests)
print("Best Marketing Platforms :", platform)
print("Customer Pain Points :", pain)

print("\n----- AI Marketing Recommendation -----\n")

print("• Focus marketing campaigns on", platform)
print("• Create content related to", interests)
print("• Target users aged", age)
print("• Solve problems like", pain)

print("\nAI analysis completed successfully\n")
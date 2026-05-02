import pandas as pd
import re

# -----------------------------
# Charger fichier
# -----------------------------
df = pd.read_excel("Deduplicated_Final.xlsx")

if "IsDuplicate" in df.columns:
    df = df[df["IsDuplicate"] == False].copy()

print("Non-duplicate records:", len(df))

# -----------------------------
# Normalisation
# -----------------------------
def norm(s):
    return re.sub(r"\s+", " ", str(s).lower()).strip()

# -----------------------------
# MOTS-CLÉS PRINCIPAUX
# -----------------------------

CARDIO = [
    "cardiovascular", "heart disease", "cardiac", "cvd"
]

AI = [
    "machine learning", "deep learning", "neural", "cnn", "rnn",
    "classification", "predictive", "risk prediction"
    
]

MONITORING = [
    "monitoring", "patient monitoring", "remote monitoring",
   
]

# -----------------------------
# ❌ EXCLUSIONS DEMANDÉES
# -----------------------------

EXCLUSION_IOT = [
    "iot", "internet of things", "wearable", "wearables",
    "smartwatch", "apple watch", "fitbit", "watch",
    "sensor", "biosensor", "biomarker",  "activity tracker", "digital health", "device", "mhealth", "ehealth"
]

EXCLUSION_PEDIATRIC = [
    "child", "children", "pediatric", "paediatric",
    "infant", "newborn", "adolescent"
]

EXCLUSION_REVIEW = [
    "review", "systematic review", "literature review", "meta-analysis"
]

ANIMAL = ["mouse", "mice", "rat", "murine", "zebrafish"]

HUMAN = ["human", "adult", "patient", "patients"]

# -----------------------------
# UTILITAIRE
# -----------------------------
def contains_any(text, kws):
    text = norm(text)
    return any(k in text for k in kws)

# -----------------------------
# SCORING / FILTRAGE
# -----------------------------
def score_record(title, abstract=None):
    t = norm(title)
    a = norm(abstract) if abstract else ""
    full_text = t + " " + a

    if not full_text.strip():
        return "Exclude", "Empty record", 1

    # ❌ EXCLUSIONS PRIORITAIRES
    if contains_any(full_text, EXCLUSION_IOT):
        return "Exclude", "IoT / wearable / watch study", 1

    if contains_any(full_text, EXCLUSION_PEDIATRIC):
        return "Exclude", "Pediatric study", 1

    if contains_any(full_text, EXCLUSION_REVIEW):
        return "Exclude", "Review article", 1

    if contains_any(full_text, ANIMAL):
        return "Exclude", "Animal study", 1

    score = 0
    reasons = []

    # CARDIO
    if contains_any(full_text, CARDIO):
        score += 2
        reasons.append("cardio")

    # AI
    if contains_any(full_text, AI):
        score += 2
        reasons.append("AI/ML")

    # MONITORING
    if contains_any(full_text, MONITORING):
        score += 1
        reasons.append("monitoring")

   

    score = min(score, 5)

    if score >= 4:
        decision = "Include"
    elif score < 4 and score >= 3:
        decision = "Maybe"
    else:
        decision = "Exclude"

    return decision, ", ".join(reasons) if reasons else "No keywords", score

# -----------------------------
# APPLICATION
# -----------------------------
out = df.copy()

if "Abstract" in df.columns:
    out[["Decision", "Reason", "Score"]] = out.apply(
        lambda x: pd.Series(score_record(x["Title"], x["Abstract"])),
        axis=1
    )
else:
    out[["Decision", "Reason", "Score"]] = out["Title"].apply(
        lambda x: pd.Series(score_record(x))
    )

out["Decision"] = out["Decision"].fillna("Exclude")

# -----------------------------
# STATISTIQUES
# -----------------------------
total = len(out)
counts = out["Decision"].value_counts()

include = counts.get("Include", 0)
maybe = counts.get("Maybe", 0)
exclude = counts.get("Exclude", 0)

print("\n===== FINAL COUNTS =====")
print(f"Include : {include}")
print(f"Maybe   : {maybe}")
print(f"Exclude : {exclude}")
print("------------------------")
print(f"TOTAL   : {include + maybe + exclude}")
print(f"EXPECTED: {total}")

if (include + maybe + exclude) != total:
    print("⚠️ ERREUR DE COMPTAGE")
else:
    print("✅ OK")

# -----------------------------
# SAVE
# -----------------------------
out.to_excel("Filtered_Final_PRISMA_Strict.xlsx", index=False)

print("\nSaved: Filtered_Final_PRISMA_Strict.xlsx")
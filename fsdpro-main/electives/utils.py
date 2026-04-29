def calculate_final_score(score, cgpa):
    return (score * 10) * 0.6 + (cgpa * 10) * 0.4

def check_eligibility(final_score, difficulty):
    thresholds = {
        "Easy": 40,
        "Medium": 60,
        "Hard": 75
    }

    return final_score >= thresholds.get(difficulty, 50)
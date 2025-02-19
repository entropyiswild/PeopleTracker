# stats_calculator.py
def calculate_average_age(people):
    """Calculate the average age from a list of people dictionaries."""
    if not people or len(people) == 0:
        return 0
    total_age = sum(person["age"] for person in people)
    return total_age / len(people)

def analyze_names(people):
    """Simulate AI analysis of names (e.g., count unique names, suggest trends, mimic Grok response)."""
    if not people or len(people) == 0:
        return "No data to analyze. Add some people to get insights!"

    unique_names = len(set(p["name"] for p in people))
    total_people = len(people)
    avg_age = calculate_average_age(people)
    
    # Simulate a Grok-like natural language response
    response = f"Insightful Analysis by xAI's Grok:\n"
    response += f"- There are {total_people} people recorded, with {unique_names} unique names.\n"
    response += f"- The average age is {avg_age:.2f} years, suggesting a {'young' if avg_age < 30 else 'mature'} group.\n"
    response += f"- {'High name diversity' if unique_names > total_people / 2 else 'Low name diversity'} observed.\n"
    if unique_names > 0:
        common_letters = set(p["name"][0].upper() for p in people)
        response += f"- Common name initials include: {', '.join(sorted(common_letters)) if common_letters else 'None'}.\n"
    response += "Would you like deeper insights? Contact xAI for advanced analysis!"

    return response
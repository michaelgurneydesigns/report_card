scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]



def get_letter_grade(score): # Defining a function

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
            return "C"
    elif score >= 60:
            return "D"
    else:
          return "F"


def calculate_stats(scores):  # (scores) is the parameter
      
      if not scores:
            return {"average": 0, "highest": 0, "lowest": 0}
     
      return {
            "average": sum(scores) / len(scores), # len is for length
            "highest": max(scores),
            "lowest": min(scores),
            "count": len(scores) 
      }


def count_grades(scores):
    # Calculates the count of each letter grade in a list of scores.
      counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

      for score in scores:  # This is the loop
            grade = get_letter_grade(score)  # Runs the top function
            counts[grade] += 1  # Add +1 to each letter
      return counts  # Return the counts dictionary

def display_report(scores):  # (scores) is a parameter

    stats = calculate_stats(scores)
    grades = count_grades(scores)
    passing = sum(1 for score in scores if score >= 60)

    print("=== Grade Report ===")  # Display the report Title
    print(f"Total Scores: {stats['count']}")  # Include an F string
    print(f"Average Scores: {stats['average']}")  # Call stats variable
    print(f"Highest: {stats['highest']}")
    print(f"Lowest: {stats['lowest']}")
    print(f"Passing: {passing} ({passing/stats['count']*100:.0f}%)")
    print()
    print("Grad Distribution")

    for grade, count in grades.items():  # Inserting a for loop
      print(f" {grade}: {count} students")  # Display grade distribution


print(display_report(scores))

honor_scores = [90, 98, 96, 97, 91]


print(display_report(honor_scores))  # honor_scores as an argument


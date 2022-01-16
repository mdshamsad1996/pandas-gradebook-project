"""
Calculate Grades

"""
from merging_the_dataframe import final_data
import pandas as pd
import numpy as np

# Calculating the Exam Total Score
n_exam = 3
for n in range(1, n_exam+1):
    final_data[f"Exam {n} Score"] = (
        final_data[f"Exam {n}"]/final_data[f"Exam {n} - Max Points"]
    )

# Calculating the Homework Scores
homework_score = final_data.filter(regex=r"^Homework \d\d?$", axis=1)
homework_max_points = final_data.filter(regex=r"^Homework \d\d? -", axis=1)

sum_of_hw_scores = homework_score.sum(axis=1)
sum_of_hw_max_points = homework_max_points.sum(axis=1)

final_data['Total Homework'] = sum_of_hw_scores/sum_of_hw_max_points

hw_max_renamed = homework_max_points.set_axis(homework_score.columns, axis=1)

average_hw_scores = (homework_score/hw_max_renamed).sum(axis=1)


final_data['Average Homework'] = average_hw_scores/homework_score.shape[1]

final_data["Homework Score"] = final_data[
    ["Total Homework", "Average Homework"]
].max(axis=1)


# Calculating the Quiz Score
quiz_scores = final_data.filter(regex=r"^quiz\d$", axis=1)
quiz_max_points = pd.Series(
    {"quiz1": 11, "quiz2": 15, "quiz3": 17, "quiz4": 14, "quiz5": 12}
)

sum_of_quiz_scores = quiz_scores.sum(axis=1)
sum_of_quiz_max_points = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_quiz_scores/sum_of_quiz_max_points

average_quiz_scores = (quiz_scores/quiz_max_points).sum(axis=1)
final_data["Average Quizzes"] = average_quiz_scores/quiz_scores.shape[1]

final_data["Quiz Score"] = final_data[
    ["Total Quizzes", "Average Quizzes"]
].max(axis=1)

# Calculating the Letter Grade
weightings = pd.Series(
    {
        "Exam 1 Score": 0.05,
        "Exam 2 Score": 0.1,
        "Exam 3 Score": 0.15,
        "Quiz Score": 0.30,
        "Homework Score": 0.4,
    }
)

final_data["Final Score"] = (final_data[weightings.index]*weightings).sum(axis=1)
final_data["Ceiling Score"] = np.ceil(final_data["Final Score"]*100) 

grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}

def grade_mapping(value):
    for key, letter in grades.items():
        if value>=key:
            return letter

letter_grades = final_data["Ceiling Score"].map(grade_mapping)

final_data["Final Grade"] = pd.Categorical(
    letter_grades, categories=grades.values(), ordered=True
)

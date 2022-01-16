# Gradebook Project Overview
This pandas project involves four main steps:
* Explore the data we’ll use in the project to determine which format and data we’ll need to calculate our final grades.
* Load the data into pandas DataFrames, making sure to connect the grades for the same student across all your data sources.
* Calculate the final grades and save them as CSV files.

## Loading the Data With Pandas
* **Loading the Roster File**
* **Loading the Homework and Exam File**
* **Loading the Quiz Files**

## Merging the Grade DataFrames
* **Merge** roster and hw_exam_grades together into a new DataFrame called final_data.
* **Merge** final_data and quiz_grades together.

## Calculating Grades With Pandas DataFrames
There are three categories of assignments that you had in your class:
* Exams
* Homework
* Quizzes

#### Calculating the Exam Total Score
Since each exam has a unique weight, we can calculate the total score for each exam individually. It makes the most sense to use a for loop, which we can see in this code:
```
n_exams = 3
for n in range(1, n_exams + 1):
    final_data[f"Exam {n} Score"] = (
        final_data[f"Exam {n}"] / final_data[f"Exam {n} - Max Points"]
    )
```
#### Calculating the Homework Scores
The max points for each homework assignment varies from 50 to 100. This means that there are two ways to calculate the homework score:

**By total score:** Sum the raw scores and maximum points independently, then take the ratio.
**By average score:** Divide each raw score by its respective maximum points, then take the sum of these ratios and divide the total by the number of assignments.
The first method gives a higher score to students who performed consistently, while the second method favors students who did well on assignments that were worth more points. To help students, we’ll give them the maximum of these two scores.
```
final_data["Homework Score"] = final_data[
    ["Total Homework", "Average Homework"]
].max(axis=1)
```
#### Calculating the Quiz Score
The quizzes also have different numbers of maximum points, so we need to do the same procedure we did for the homework

#### Calculating the Letter Grade
we’ll use a pandas Series to store the weightings. That way, we can multiply by the correct columns from final_data automatically. Create our weightings with this code:
```
weightings = pd.Series(
    {
        "Exam 1 Score": 0.05,
        "Exam 2 Score": 0.1,
        "Exam 3 Score": 0.15,
        "Quiz Score": 0.30,
        "Homework Score": 0.4,
    }
)
```
## Grouping the Data
To put the grades into our student administration system, we need to separate the students into each section and sort them by their last name. Fortunately, pandas has we covered here as well.

pandas has powerful abilities to group and sort data in DataFrames. we need to group our data by the students’ section number and sort the grouped result by their name.

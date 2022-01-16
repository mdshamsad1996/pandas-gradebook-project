"""
This script load the data  from

* roster
* HomeWork and exam grades
* Quiz grades

"""
import pandas as pd
from pathlib import Path

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

roster = pd.read_csv(
    DATA_FOLDER /"roster.csv",
    converters={"NetID": str.lower, "Email Address": str.lower},
    usecols=["Section", "Email Address", "NetID"],
    index_col="NetID"
)

hw_exam_grades = pd.read_csv(
    DATA_FOLDER /"hw_exam_grade.csv",
    converters={"SID": str.lower},
    usecols=lambda x: "Submission" not in x,
    index_col="SID"
)

quiz_grades = pd.DataFrame()
for file_path in DATA_FOLDER.glob("quiz_*_grades.csv"):
    quiz_name = "".join(file_path.stem.split("_")[:2])
    quiz = pd.read_csv(
        file_path,
        converters={"Email": str.lower},
        usecols=["Email", "Grade"],
        index_col="Email"
    ).rename(columns={"Grade": quiz_name})

    quiz_grades = pd.concat([quiz_grades, quiz], axis=1)
    

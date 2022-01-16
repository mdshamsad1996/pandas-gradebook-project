"""
This script merge the data frame

* roster
* HomeWork and exam grades
-- into final data

* final data
* quiz_grades
-- into final data

"""
import pandas as pd
from loading_the_data import roster, hw_exam_grades, quiz_grades

final_data = pd.merge(
    roster, hw_exam_grades, left_index=True, right_index=True
)

final_data = pd.merge(
    final_data, quiz_grades, left_on="Email Address", right_index=True
)

final_data.fillna(0)
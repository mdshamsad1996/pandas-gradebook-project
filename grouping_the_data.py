# Grouping the Data

from calculate_grades import final_data
from loading_the_data import DATA_FOLDER

for section, table in final_data.groupby("Section"):
    section_file = DATA_FOLDER /f"Section {section} Grades.csv"
    num_students = table.shape[0]
    print(
        f"In section {section} there are {num_students} saved to "
        f"file {section_file}"
    )
    table.sort_values(by=["Last Name", "First Name"]).to_csv(section_file)
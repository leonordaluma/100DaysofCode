student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_df = pandas.DataFrame(student_dict)

# for (key, value) in student_df.items():
#     print(key)


# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(row)
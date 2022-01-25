# Author: CRS 01/06/22
# Create rows
last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin", "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
# Create numbers to track what word the code is on
initial_number = 0
name_number = 0
# Create for loop to add last names to first names
for row in rows:
    for i, v in enumerate(rows):
        if name_number == initial_number:
            rows = rows[:20] + last_initials
            initial_number += 1
            name_number += 1
            print(rows)
            break
        elif rows.index != initial_number:
            break
# Print the result
print(rows)

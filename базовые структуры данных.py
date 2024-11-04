grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnyy', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
print(sorted_students) #['Aaron', 'Bilbo', 'Johnyy', 'Khendrik', 'Steve']
grades_aaron=(5 + 3 + 3 + 5 +4) / 5
grades_bilbo=(2 + 2 + 2 + 3) / 4
grades_johnyy=(4 + 5 + 5 +2) / 4
grades_khendrik=(4 + 4 + 3) / 3
grades_steve=(5 + 5 + 5 + 4 + 5) / 5
grades_students = { 'Aaron:' + '4', 'Bilbo:' + '2.25', 'Johnyy:' + '4', 'Khendrik:' + '3.6666666666666665', 'Steve:' + '4.8'}
print(sorted(grades_students))
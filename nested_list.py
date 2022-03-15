classroom = []

for i in range(25):
    classroom.append([])
    for students in range(0,5):
        classroom[i].append(students)

print(*classroom, sep="\n")
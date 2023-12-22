class Students:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_lists):
  sorted_students = sorted(student_lists,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


students = [
    Students("saru", "A123", 7.8),
    Students("saran", "A124", 8.9),
    Students("kalpana", "A215", 9.1),
    Students("sharmi", "A126", 9.9),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))

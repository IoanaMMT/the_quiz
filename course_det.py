from course import *

course = Course("Introduction", 100, 8, "python")

print course.name
print course.course_price()

print(course.name + " " + course.course_type + " " + str(course.course_price()))

print course.get_passing_grade()
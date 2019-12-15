class Course:
	def __init__(self, name, weekly_price, lenght, course_type = "python", age = 18):
		self.name = name
		self.weekly_price = weekly_price
		self.lenght = lenght
		self.course_type = course_type
		self.passing_grade = passing_grade
		self.age = int(age)

	def course_price(self):
		if self.course_type == "python":
			return (self.lenght * self.weekly_price)*0.5
		elif self.course_type == "Ruby":
			return (self.lenght * self.weekly_price)*0.25
		else:
			return self.lenght * self.weekly_price

	def get_passing_grade(self):
		if self.course_type == "python":
			self.passing_grade = 6
			return self.passing_grade
		elif self.course_type == "Ruby":
			self.passing_grade = 7
			return self.passing_grade
		else:
			return self.passing_grade

class CourseForKids(Course):

	def price_for_kids(self):

		if self.age <= 19:
			return self.course_price() * 0.5

		
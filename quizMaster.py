class Question():

	def __init__(self, number, question, answers=[]):
		self.number = number
		self.question = question
		self.answers = answers

class ExactAnswerQuestion(Question):

	def validate(self, user_answer):
		user_answer = int(user_answer)

		if user_answer == self.answers[0]:
			return self.answers[1], self.answers[3]
		else:
			return self.answers[2], self.answers[4]

class GreaterOrEqualThanQuestion(Question):

	def validate(self, user_answer):
		user_answer = int(user_answer)

		for x in self.answers:
			if user_answer >= x[0]:
				return x[1], x[2]

class Game():
	
	def user_input(self,msg):
		return raw_input(msg)

	def quizMaster(self, questions):
		score = 0

		for question in questions:
			user_answer = self.user_input(question.question)
			return_message, question_score = question.validate(user_answer)
			print return_message
			score += question_score

		print("Your score was:", score)

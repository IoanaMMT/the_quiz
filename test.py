import unittest
from quizMaster import * 

class TestTheQuiz(unittest.TestCase):
	greaterOrEqualThanQuestion = GreaterOrEqualThanQuestion(1,"How many cats do have?", 
							[(5, "OK...That is a bit creapy...You must REALLY love cats.",5),
							(3, "OK...That must be a bit of work, but hey! I guess you are a cat lover :).",1),
							(1, "Good for you. I bet you are having a great time together ;).",1),
							(0, "That's so sad! :( Cats are really fun loving creatures. You should get one.)",1),])
	
	exactAnswerQuestion = ExactAnswerQuestion(6,"Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby", 
							(3, "Because he is a little Bigger.","The baby of course. Because he is a little Bigger", 1, 0))

	def test_greaterOrEqualThanQuestion_for_input_0(self):
		user_answer = 0
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("That's so sad! :( Cats are really fun loving creatures. You should get one.)",1))
	
	def test_greaterOrEqualThanQuestion_for_input_1(self):
		user_answer = 1
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("Good for you. I bet you are having a great time together ;).",1))
	
	def test_greaterOrEqualThanQuestion_for_input_2(self):
		user_answer = 2
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("Good for you. I bet you are having a great time together ;).",1))
	
	def test_greaterOrEqualThanQuestion_for_input_4(self):
		user_answer = 4
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("OK...That must be a bit of work, but hey! I guess you are a cat lover :).",1))
	
	def test_greaterOrEqualThanQuestion_for_input_6(self):
		user_answer = 6
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("OK...That is a bit creapy...You must REALLY love cats.",5))
	
	def test_greaterOrEqualThanQuestion_for_input_150(self):
		user_answer = 150
		self.assertEqual(self.greaterOrEqualThanQuestion.validate(user_answer), ("OK...That is a bit creapy...You must REALLY love cats.",5))

	def test_exactAnswerQuestion_for_input_1(self):
		user_answer = 1
		self.assertEqual(self.exactAnswerQuestion.validate(user_answer), ("The baby of course. Because he is a little Bigger",0))
	
	def test_exactAnswerQuestion_for_input_3(self):
		user_answer = 3
		self.assertEqual(self.exactAnswerQuestion.validate(user_answer), ("Because he is a little Bigger.",1))

if __name__ == '__main__':
	unittest.main()

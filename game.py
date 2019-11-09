from quizMaster import *

questions = []
questions.append(GreaterOrEqualThanQuestion(1,"How many cats do have?", 
								[(5, "OK...That is a bit creapy...You must REALLY love cats.",1),
								(4, "OK...That must be a bit of work, but hey! I guess you are a cat lover :).",1),
								(2, "Good for you. I bet you are having a great time together ;).",1),
								(0, "That's so sad! :( Cats are really fun loving creatures. You should get one.)",1),]),)

questions.append(ExactAnswerQuestion(6,"Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby", 
							(3, "Because he is a little Bigger.","The baby of course. Because he is a little Bigger", 1, 0)))

questions.append(ExactAnswerQuestion(7,"What is the answer to the next math problem  6/2(1+2) ?", 
							(9, "Excellent!!!","This is not the right answer.", 1, 0)))


print("Welcome to the Quiz Master")
print("Please answer to the following questions to the best of your abilities")
print("Let's do the introductions first")
name = raw_input("What is your name please?")
print("Nice to meet you {}!. Enjoy the quiz!".format(name))
print("Let's go to the first question!")

g = Game() 
score = g.quizMaster(questions)



questions = {
	1 : "Question 1: How many cats do have?",
	# 2 : "Question 2: Are you having fun now? y/n",
	# 3 : "Question 3: Did you know that your tongue is as long as your thumb? y/n",
	# 4 : "Question 4: What is the name of our natural satellite?",
	# 5 : "Question 5: If you have a bowl with 6 apples and you take away four, how many do you have?",
	# 6 : "Question 6: Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby",
	# 7 : "Question 7: What is the answer to the next math problem  6/2(1+2) ?",
}

answers = {
	1 : [0, 3, 4] # why numbers don't work? # how to create range of numbers
	# 2 : ["No", "No2", "No3"],
	# 3 : ["Maybe", "Maybe2", "Maybe3"],
	# 4 : ["Try again", "Try again2", "Try again3"],
	# 5 : ["That's correct", "That's correct2", "That's correct3"],
	# 6 : ["Very close", "Very close2", "Very close3"],
	# 7 : ["Well done", "Well done2", "Well done3"],
	}

#use slices for multiple answers and outcomes

for i in range(1, len(questions)+1): # iterate over questions
	answer = raw_input(questions[i]) # how to expect strings and integers 
	
	for i in range(1,len(answers)+1): # iterate over possible answers 

		correct_answer = False

		for x in answers[i]: # iterate over answers 

			current_answer = x

			print(current_answer)
			
			if type(current_answer) is int:
				print(current_answer)
				answer = int(answer)

			if answer <= x:
				correct_answer = True

		if correct_answer:
			print("Correct!")
		else:
			print("Incorrect!")



# Replace the test answers with the real ones
# Have a different outcome to every answer
# Capturing errors
# Counting correct answers
# Break the game when requested
# List the results

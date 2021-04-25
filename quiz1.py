class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer


def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))


def store(examList,questions):
     Question = open("TextFile1.txt", "r")
     for Q in Question.read_lines():    
          print(Q)
          
     Question.close()


store(examList,questions)
run_quiz(questions)


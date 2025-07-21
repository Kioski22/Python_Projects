quiz = [
    {
        "question": "what is 1 + 1",
        "choices": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        }, 
        "answer" : "a",
            
    }, 

    {
         "question": "what is 3 + 2",
        "choices": {
            "a": "2",
            "b": "3",
            "c": "4",
            "d": "5"
        }, 
        "answer" : "d",
    }, 
    
    {
         "question": "what is 8 * 8",
        "choices": {
            "a": "78",
            "b": "95",
            "c": "64",
            "d": "81"
        }, 
        "answer" : "d",
    }

]

 
def ask_question(quiz):
    score = 0
    for q in quiz:
        print(q["question"])
        print(q["choices"])
        answers = input("type your answer: ")
        answers = answers.lower()
        score += check_answer(q["answer"], answers)
    print("Your final score is:", score, "/", len(quiz))
def check_answer(answer ,answers):
    if answer == answers:
        print("excellent!! That's Correct!")
        return 1 

    else:
        print("that's the wrong answer :<")
        return 0


ask_question(quiz)

        

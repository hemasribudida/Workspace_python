# quiz_app/quiz_service.py

from question import Question

def load_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    i = 0
    while i < len(lines):
        if lines[i].startswith('#'):
            number = lines[i][1:]
            question_text = lines[i+1]
            options = [lines[i+2], lines[i+3], lines[i+4], lines[i+5]]
            answer_line = lines[i+6]
            answer_index = int(answer_line.split(':')[1])
            questions.append(Question(number, question_text, options, answer_index))
            i += 7
        else:
            i += 1
    return questions

def start_quiz(questions):
    correct = 0
    total = len(questions)

    for q in questions:
        if q.display():
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong! Correct answer: {q.answer_index}")
    
    wrong = total - correct
    percentage = (correct / total) * 100
    result = "Pass" if percentage >= 60 else "Fail"

    print("\n---- Quiz Result ----")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {correct}")
    print(f"Wrong Answers  : {wrong}")
    print(f"Score          : {percentage:.2f}%")
    print(f"Result         : {result}")

if __name__ == "__main__":
    questions = load_questions_from_file("./question.txt")
    start_quiz(questions)

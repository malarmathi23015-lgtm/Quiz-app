questions = [
    {"question": "What is the capital of France?", "options": ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"], "answer": "3"},
    {"question": "Which planet is known as the Red Planet?", "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"], "answer": "2"},
    {"question": "What is 12 x 12?", "options": ["1. 124", "2. 144", "3. 132", "4. 148"], "answer": "2"},
    {"question": "Who invented the telephone?", "options": ["1. Thomas Edison", "2. Nikola Tesla", "3. Alexander Graham Bell", "4. Albert Einstein"], "answer": "3"},
    {"question": "What is the largest ocean on Earth?", "options": ["1. Atlantic", "2. Indian", "3. Arctic", "4. Pacific"], "answer": "4"},
]

score = 0
print("\n🧠 Welcome to the Quiz!\n")

for i, q in enumerate(questions, 1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")
    answer = input("Your answer (1/2/3/4): ").strip()
    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        correct = q["options"][int(q["answer"]) - 1]
        print(f"❌ Wrong! Correct answer: {correct}\n")

print(f"🎯 Your Score: {score}/{len(questions)}")
if score == len(questions):
    print("🏆 Perfect score!")
elif score >= 3:
    print("🎉 Good job!")
else:
    print("💪 Keep practicing!")

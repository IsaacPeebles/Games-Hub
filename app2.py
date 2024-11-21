from question import Question

# Define prompts and answers together
quiz_data = [
    ('What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n', 'a'),
    ('What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n', 'c'),
    ('What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n', 'b'),
]

# Generate Question objects dynamically
questions = [Question(prompt, answer) for prompt, answer in quiz_data]

def run_test(questions):
    score = sum(1 for q in questions if input(q.prompt) == q.answer)
    print(f'You got {score}/{len(questions)} correct')

# Run the test
run_test(questions)

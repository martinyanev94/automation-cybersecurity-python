def collect_feedback():
    feedback = input("How satisfied are you with the patch management speed? (1-5): ")
    return feedback

# Collect feedback and analyze the average satisfaction score
feedback_scores = []
for _ in range(10):  # Simulating collecting feedback from 10 team members
    score = collect_feedback()
    feedback_scores.append(int(score))

average_score = sum(feedback_scores) / len(feedback_scores)
print(f"Average team satisfaction score: {average_score}")

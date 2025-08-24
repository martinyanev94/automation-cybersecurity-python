class FeedbackCollector:
    def collect_feedback(self):
        feedback = input("Please provide feedback on the incident response: ")
        with open('feedback_log.txt', 'a') as f:
            f.write(feedback + '\n')
        print("Thank you for your feedback!")

# Usage
feedback_collector = FeedbackCollector()
feedback_collector.collect_feedback()

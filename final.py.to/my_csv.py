import csv
from collections import Counter

comments = [
    {"email": "alice@example.com", "comment": "Hello!"},
    {"email": "bob@example.com", "comment": "Hi there!"},
    {"email": "alice@example.com", "comment": "How are you?"},
    {"email": "charlie@example.com", "comment": "Good morning."},
    {"email": "bob@example.com", "comment": "Nice to meet you."}
]

email_counts = Counter(comment["email"] for comment in comments)

with open("comments.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["email", "comment_count"])  
    for email, count in email_counts.items():
        writer.writerow([email, count])
        print(f"{email}: {count} comments")


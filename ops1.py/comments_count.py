import csv
from collections import Counter

# Example comments data
comments = [
    {"email": "alice@example.com", "comment": "Hello!"},
    {"email": "bob@example.com", "comment": "Hi there!"},
    {"email": "alice@example.com", "comment": "Another comment."},
    {"email": "carol@example.com", "comment": "Hey!"},
    {"email": "bob@example.com", "comment": "Second comment."},
]

# Count comments per email
email_counts = Counter(comment["email"] for comment in comments)

# Save to CSV
with open("comments.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["email", "comment_count"])
    for email, count in email_counts.items():
        writer.writerow([email, count])

print("comments.csv saved!")

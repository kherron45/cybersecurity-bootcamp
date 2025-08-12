import csv
from collections import defaultdict

# Example data: list of dictionaries with 'email' and 'comment'
comments = [
    {"email": "alice@example.com", "comment": "Great post!"},
    {"email": "bob@example.com", "comment": "Thanks for sharing."},
    {"email": "alice@example.com", "comment": "I agree with this."},
    {"email": "carol@example.com", "comment": "Nice read."},
    {"email": "bob@example.com", "comment": "Very helpful, thanks."},
]

# Group and count comments by email
comment_counts = defaultdict(int)
for entry in comments:
    comment_counts[entry["email"]] += 1

# Save to CSV file
with open("comments.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["email", "comment_count"])  # header
    for email, count in comment_counts.items():
        writer.writerow([email, count])

print("comments.csv saved.")

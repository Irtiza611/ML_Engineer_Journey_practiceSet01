from faker import Faker
import random
import pandas as pd
from datetime import datetime
import uuid

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_USERS = 10
NUM_POSTS = 50
NUM_LIKES = 20
NUM_COMMENTS = 10


users = []
for _ in range(NUM_USERS):
    users.append({
        "user_id": str(uuid.uuid4()),
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email()
    })
user_ids = [u["user_id"] for u in users]

# ------------------ Generate Posts ------------------
posts = []
for _ in range(NUM_POSTS):
    user_id = random.choice(user_ids)
    posts.append({
        "post_id": str(uuid.uuid4()),
        "user_id": user_id,
        "content": fake.text(max_nb_chars=100),
        "timestamp": fake.date_time_this_year()
    })
post_ids = [p["post_id"] for p in posts]


likes = set()
like_data = []
while len(like_data) < NUM_LIKES:
    user_id = random.choice(user_ids)
    post_id = random.choice(post_ids)
    key = (user_id, post_id)
    if key not in likes:
        likes.add(key)
        like_data.append({
            "like_id": str(uuid.uuid4()),
            "user_id": user_id,
            "post_id": post_id,
            "timestamp": fake.date_time_this_year()
        })


comments = []
for _ in range(NUM_COMMENTS):
    comments.append({
        "comment_id": str(uuid.uuid4()),
        "user_id": random.choice(user_ids),
        "post_id": random.choice(post_ids),
        "comment_text": fake.sentence(nb_words=12),
        "timestamp": fake.date_time_this_year()
    })


pd.DataFrame(users).to_csv("users.csv", index=False)
pd.DataFrame(posts).to_csv("posts.csv", index=False)
pd.DataFrame(like_data).to_csv("likes.csv", index=False)
pd.DataFrame(comments).to_csv("comments.csv", index=False)

print("Data generation complete. Files saved:")
print("- users.csv")
print("- posts.csv")
print("- likes.csv")
print("- comments.csv")

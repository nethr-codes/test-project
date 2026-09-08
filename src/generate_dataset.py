import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = {
    "transaction_id": range(1, n + 1),
    "amount": np.random.randint(50, 50000, n),
    "transaction_hour": np.random.randint(0, 24, n),
    "failed_attempts": np.random.randint(0, 6, n),
    "new_device": np.random.randint(0, 2, n),
    "unusual_location": np.random.randint(0, 2, n),
    "transaction_count_1hr": np.random.randint(1, 15, n)
}

df = pd.DataFrame(data)

df["fraud"] = (
    (df["amount"] > 30000) |
    (df["failed_attempts"] >= 4) |
    (df["new_device"] == 1) & (df["unusual_location"] == 1) |
    (df["transaction_count_1hr"] >= 10)
).astype(int)

df.to_csv("data/upi_transactions.csv", index=False)

print("Dataset created successfully!")
print("Total transactions:", len(df))
print(df.head())

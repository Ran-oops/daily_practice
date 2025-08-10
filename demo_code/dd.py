
import pandas as pd

df = pd.DataFrame({"name":['l1', 'l2', 'l3'], "scores":[200, 400, 300]})
print(df)

# filter
new_df = df[df['scores']> 200].groupby('name')['scores'].agg(["max","mean"]).reset_index()
print(new_df)



import re
test_cases = [
    "abbccc",
    "bbball",
    "book",
    "bb_BB_b"
]

for i in test_cases:
    result = re.sub(r"b+", "b", i, flags=re.IGNORECASE)
    print(result)






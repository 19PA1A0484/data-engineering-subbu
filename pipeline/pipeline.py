import sys
import pandas as pd
day = int(sys.argv[1])
df = pd.DataFrame({"A":[1,2],"B":[4,3]})
df['day']=day
print(df.head())
df.to_parquet(f"output_{day}.parquet")
print(f"hello world day={day}")
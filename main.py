import pandas as pd

# loading
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# data filtering
df = pd.concat([df1, df2, df3], ignore_index=True)
df = df[df["product"] == "pink morsel"]

# string to numeric & remove $ sign
df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
df["price"] = pd.to_numeric(df["price"])
df["quantity"] = pd.to_numeric(df["quantity"])

# sales column
df["sales"] = df["quantity"]*df["price"]
# df["sales"] = df["sales"].apply(lambda x: f"${x:.2f}")
df = df[["sales", "date", "region"]]

# formatted csv file
df.to_csv("data/formatted_sales_data.csv", index=False)
import pandas as pd

df = pd.read_csv("retail_store_sales.csv")

df = df.head(5000).copy()

print("Original shape:", df.shape)

df = df.dropna(how="all")

df = df.drop_duplicates()

text_columns = [
    "Transaction ID",
    "Customer ID",
    "Category",
    "Item",
    "Payment Method",
    "Location"
]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].astype("string").str.strip()

if "Category" in df.columns:
    df["Category"] = df["Category"].str.title()

if "Location" in df.columns:
    df["Location"] = df["Location"].str.title()

numeric_columns = [
    "Price Per Unit",
    "Quantity",
    "Total Spent"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

for column in numeric_columns:
    if column in df.columns:
        df[column] = df[column].fillna(df[column].median())

if "Item" in df.columns:
    df["Item"] = df["Item"].fillna("Not Provided")

if "Payment Method" in df.columns:
    df["Payment Method"] = df["Payment Method"].fillna("Not Provided")


if "Transaction Date" in df.columns:
    df["Transaction Date"] = pd.to_datetime(
        df["Transaction Date"],
        errors="coerce"
    )

if "Discount Applied" in df.columns:
    df["Discount Applied"] = df["Discount Applied"].fillna("Not Provided")

df.to_csv("cleaned_retail_store_sales.csv", index=False)

print("\nCleaning completed successfully!")
print("Final shape:", df.shape)
print("Saved as: cleaned_retail_store_sales.csv")
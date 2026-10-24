from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
INPUT = BASE / "data" / "sample_customer_data.csv"
OUT = BASE / "output"

def main():
    df = pd.read_csv(INPUT)
    original_rows = len(df)
    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()
    log = [{"Step": 1, "Issue": "Duplicate rows", "Action": "Remove exact duplicates", "Affected": duplicate_count}]

    for col in ["Customer_Name", "Email", "City"]:
        df[col] = df[col].astype("string").str.strip().replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})
    df["Customer_Name"] = df["Customer_Name"].str.title()
    df["City"] = df["City"].str.title()
    df["Email"] = df["Email"].str.lower()

    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Purchase_Amount"] = pd.to_numeric(df["Purchase_Amount"], errors="coerce")
    age_n = int(df["Age"].isna().sum())
    age_median = float(df["Age"].median())
    df["Age"] = df["Age"].fillna(age_median).round().astype("Int64")
    city_n = int(df["City"].isna().sum())
    df["City"] = df["City"].fillna("Unknown")
    email_n = int(df["Email"].isna().sum())
    df["Email"] = df["Email"].fillna("Not Provided")
    purchase_n = int(df["Purchase_Amount"].isna().sum())
    purchase_median = float(df["Purchase_Amount"].median())
    df["Purchase_Amount"] = df["Purchase_Amount"].fillna(purchase_median).round(2)
    parsed = pd.to_datetime(df["Signup_Date"].astype("string").str.strip(), errors="coerce", dayfirst=True, format="mixed")
    invalid_dates = int(parsed.isna().sum())
    df["Signup_Date"] = parsed.dt.strftime("%Y-%m-%d").fillna("Unknown")
    df["Customer_ID"] = pd.to_numeric(df["Customer_ID"], errors="coerce").astype("Int64")
    df = df.sort_values("Customer_ID").reset_index(drop=True)
    missing = int(df.isna().sum().sum())

    log.extend([
      {"Step":2,"Issue":"Text formatting","Action":"Trim spaces, title-case names/cities, lowercase emails","Affected":len(df)},
      {"Step":3,"Issue":"Missing Age","Action":f"Fill with median {age_median:g}","Affected":age_n},
      {"Step":4,"Issue":"Missing City","Action":"Fill with Unknown","Affected":city_n},
      {"Step":5,"Issue":"Missing Email","Action":"Fill with Not Provided","Affected":email_n},
      {"Step":6,"Issue":"Missing Purchase_Amount","Action":f"Fill with median {purchase_median:.2f}","Affected":purchase_n},
      {"Step":7,"Issue":"Mixed/invalid dates","Action":"Standardize YYYY-MM-DD; invalid -> Unknown","Affected":invalid_dates},
      {"Step":8,"Issue":"Validation","Action":"Count remaining missing cells","Affected":missing}
    ])
    OUT.mkdir(exist_ok=True)
    df.to_csv(OUT/"cleaned_customer_data.csv",index=False)
    pd.DataFrame(log).to_csv(OUT/"cleaning_log.csv",index=False)
    summary = [
      "DATA CLEANING SUMMARY","=====================",
      f"Original rows: {original_rows}",f"Exact duplicate rows removed: {duplicate_count}",
      f"Final rows: {len(df)}",f"Final columns: {len(df.columns)}",
      f"Missing Age filled: {age_n}",f"Missing City filled: {city_n}",
      f"Missing Email filled: {email_n}",f"Missing Purchase_Amount filled: {purchase_n}",
      f"Invalid dates replaced with Unknown: {invalid_dates}",f"Remaining missing cells: {missing}","",
      "Rules: text standardized; median imputation used for Age and Purchase_Amount;",
      "City -> Unknown; Email -> Not Provided; invalid dates -> Unknown.",
      "Zero purchase amount retained as potentially valid.",
      "Synthetic practice dataset. Confirm rules with the data owner for real data."
    ]
    (OUT/"cleaning_summary.txt").write_text("\n".join(summary)+"\n",encoding="utf-8")
    print("\n".join(summary))

if __name__ == "__main__":
    main()

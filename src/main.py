import pandas as pd

from extract import load_data
from transform import (
    clean_data,
    create_customer_summary,
    create_product_summary,
    create_region_summary,
)
from validation import validate_required_columns, validate_cleaned_data
from load import load_to_postgres


RAW_DATA_PATH = "data/raw/samplesuperstore.csv"

CLEANED_DATA_PATH = "data/processed/cleaned_orders.csv"
CUSTOMER_SUMMARY_PATH = "data/processed/customer_summary.csv"
PRODUCT_SUMMARY_PATH = "data/processed/product_summary.csv"
REGION_SUMMARY_PATH = "data/processed/region_summary.csv"


def inspect_data(df: pd.DataFrame) -> None:
    """
    Print basic information about the dataset.
    """
    print("DATA PREVIEW:")
    print(df.head())

    print("\nDATA INFO:")
    print(df.info())

    print("\nCOLUMNS:")
    print(df.columns)

    print("\nMISSING VALUES:")
    print(df.isna().sum())


def save_to_csv(df: pd.DataFrame, file_path: str) -> None:
    """
    Save DataFrame to a CSV file.
    """
    df.to_csv(file_path, index=False)
    print(f"Saved CSV: {file_path}")


def main() -> None:
    raw_df = load_data(RAW_DATA_PATH)

    print("RAW DATA:")
    inspect_data(raw_df)

    validate_required_columns(raw_df)

    cleaned_df = clean_data(raw_df)

    print("\nCLEANED DATA:")
    inspect_data(cleaned_df)

    validate_cleaned_data(cleaned_df)

    customer_summary = create_customer_summary(cleaned_df)
    product_summary = create_product_summary(cleaned_df)
    region_summary = create_region_summary(cleaned_df)

    save_to_csv(cleaned_df, CLEANED_DATA_PATH)
    save_to_csv(customer_summary, CUSTOMER_SUMMARY_PATH)
    save_to_csv(product_summary, PRODUCT_SUMMARY_PATH)
    save_to_csv(region_summary, REGION_SUMMARY_PATH)

    load_to_postgres(cleaned_df, "cleaned_orders")
    load_to_postgres(customer_summary, "customer_summary")
    load_to_postgres(product_summary, "product_summary")
    load_to_postgres(region_summary, "region_summary")

    print("\nETL pipeline completed successfully.")


if __name__ == "__main__":
    main()
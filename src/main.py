import pandas as pd 

RAW_DATA_PATH = "data/raw/samplesuperstore.csv"
CLEANED_DATA_PATH = "data/processed/cleaned_orders.csv"

def load_data(file_path: str) -> pd.DataFrame:
    """
    load data sales from a CSV file.
    Parameters: file path(str)

    return: dataframe
    """
    df = pd.read_csv(file_path)
    
    return df





def inspect_data(df: pd.DataFrame) -> None:
    """
    Printing basic information about the set.
    """
    print("DATA PREVIEW:")
    print(df.head())
    print("\nDATA INFO")
    print(df.info())
    print("\nCOLUMNS: ")
    print(df.columns)
    print("\nMISSING VALUES:")
    print(df.isna().sum())

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Superstore sales data.

    Cleaning steps:
    - remove duplicated rows
    - convert date columns to datetime
    - remove rows with missing critical values
    - keep only valid sales and quantity values
    - standardize column names for future SQL usage

    Parameters:
        df (pd.DataFrame): Raw Superstore dataset.

    Returns:
        pd.DataFrame: Cleaned Superstore dataset.
    """
    cleaned_df = df.copy()

    cleaned_df = cleaned_df.drop_duplicates()

    cleaned_df["Order Date"] = pd.to_datetime(cleaned_df["Order Date"], errors="coerce")
    cleaned_df["Ship Date"] = pd.to_datetime(cleaned_df["Ship Date"], errors="coerce")

    cleaned_df = cleaned_df.dropna(
        subset=[
            "Order ID",
            "Order Date",
            "Ship Date",
            "Customer ID",
            "Customer Name",
            "Product ID",
            "Product Name",
            "Sales",
            "Quantity",
            "Profit",
        ]
    )

    cleaned_df = cleaned_df[cleaned_df["Sales"] >= 0]
    cleaned_df = cleaned_df[cleaned_df["Quantity"] > 0]

    cleaned_df.columns = (
        cleaned_df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("/", "_")
    )

    return cleaned_df




def main() -> None:
    df = load_data(RAW_DATA_PATH)

    print("RAW DATA:")
    inspect_data(df)

    cleaned_df = clean_data(df)

    print("\nCLEANED DATA:")
    inspect_data(cleaned_df)

    cleaned_df.to_csv(CLEANED_DATA_PATH, index=False)

    print(f"\nCleaned data saved to: {CLEANED_DATA_PATH}")
    print("Data cleaning completed successfully.")


if __name__ =="__main__":
    main()





import pandas as pd


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
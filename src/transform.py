import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Superstore sales data.
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


def create_customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create customer-level sales summary.
    """
    customer_summary = (
        df
        .groupby(["customer_id", "customer_name"], as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            average_sales=("sales", "mean"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values("total_sales", ascending=False)
    )

    return customer_summary


def create_product_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create product-level sales summary.
    """
    product_summary = (
        df
        .groupby(["product_id", "product_name", "category", "sub_category"], as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values("total_sales", ascending=False)
    )

    return product_summary


def create_region_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create region-level sales summary.
    """
    region_summary = (
        df
        .groupby("region", as_index=False)
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("sales", "sum"),
            total_profit=("profit", "sum"),
            total_quantity=("quantity", "sum"),
        )
        .sort_values("total_sales", ascending=False)
    )

    return region_summary
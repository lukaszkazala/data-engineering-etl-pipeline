import pandas as pd


def validate_required_columns(df: pd.DataFrame) -> None:
    """
    Check if required raw columns exist in the dataset.
    """
    required_columns = [
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

    missing_columns = []

    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def validate_cleaned_data(df: pd.DataFrame) -> None:
    """
    Validate cleaned dataset after transformation.
    """
    required_columns = [
        "order_id",
        "order_date",
        "ship_date",
        "customer_id",
        "customer_name",
        "product_id",
        "product_name",
        "sales",
        "quantity",
        "profit",
    ]

    missing_columns = []

    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(f"Missing cleaned columns: {missing_columns}")

    if df["order_id"].isna().any():
        raise ValueError("order_id contains missing values")

    if df["customer_id"].isna().any():
        raise ValueError("customer_id contains missing values")

    if df["product_id"].isna().any():
        raise ValueError("product_id contains missing values")

    if (df["sales"] < 0).any():
        raise ValueError("sales contains negative values")

    if (df["quantity"] <= 0).any():
        raise ValueError("quantity contains zero or negative values")
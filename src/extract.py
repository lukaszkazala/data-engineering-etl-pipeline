import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    load data sales from a CSV file.
    Parameters: file path(str)

    return: dataframe
    """
    df = pd.read_csv(file_path)
    
    return df


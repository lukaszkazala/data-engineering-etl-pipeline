import pandas as pd 

RAW_DATA_PATH = "data/raw/samplesuperstore.csv"


def load_data(file_path: str) -> pd.DataFrame:
    """
    load data sales from a CSV file.
    Parameters: pile path(str)

    return: dataframe
    """
    df = pd.read_csv(file_path)
    
    return df





def main() -> None:
    df = load_data(RAW_DATA_PATH)
    print(df.head())
    print(df.info())
    print(df.columns)
    print(df.isna().sum())


if __name__ =="__main__":
    main()





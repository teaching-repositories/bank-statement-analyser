import pandas as pd

def load_csv_file(file_path):
    """
    Load a CSV file and return its content as a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The CSV file content as a DataFrame.
    """
    data = pd.read_csv(file_path, parse_dates=['Date'], dtype={'Amount': float})
    return data

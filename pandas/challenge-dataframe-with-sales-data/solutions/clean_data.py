def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess the raw sales data.
    
    :param df: The input DataFrame containing raw sales data.
    :return: The cleaned and preprocessed DataFrame.
    """
    # Drop the rows with missing dataset
    df = df.dropna()
    df = df.reset_index(drop=True)
    
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Drop any duplicate rows
    df.drop_duplicates(inplace=True)
    
    return df
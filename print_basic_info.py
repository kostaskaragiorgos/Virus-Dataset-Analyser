def print_basic_info(dataframe):
    """prints basic info of the dataframe"""
    print("Types\n", dataframe.dtypes)
    print("\nShape:", dataframe.shape)
    print("\n Null Values\n", dataframe.isnull().sum())
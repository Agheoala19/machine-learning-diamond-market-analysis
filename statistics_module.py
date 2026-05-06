def basic_statistics(df):

    return df.describe()


def group_analysis(df):

    result = df.groupby("cut")["price"].mean()

    return result

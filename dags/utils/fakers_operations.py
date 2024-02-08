import pandas as pd
from faker import Faker


def profile_data_generator(df_range: int):
    sample = Faker()

    dataframe = pd.DataFrame([sample.profile() for profile in range(df_range)])

    return dataframe

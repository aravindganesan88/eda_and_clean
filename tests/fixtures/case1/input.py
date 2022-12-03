import pandas as pd
import numpy as np


def input_fixture():
    historical_df = [
        ("12-31-2019", "A", 5),
        ("03-31-2020", "A", 10),
        ("03-31-2020", "B", 20),
        ("03-31-2020", "C", 30),
        ("03-31-2020", "na", 40),
        ("06-30-2020", "A", np.nan),
        ("06-30-2020", "E", 17),
        ("06-30-2020", "B", 20),
        ("09-30-2020", "A", 10),
        ("09-30-2020", "F", 20),
        ("09-30-2020", "B", 20000000),
        ("09-30-2020", "C", 30),
        ("12-31-2020", "A", 10),
        ("12-31-2020", "B", 20),
        ("12-31-2020", "C", 30),
        ("12-31-2020", "G", 100),
    ]

    df = pd.DataFrame(
        data=[
            {
                "date": date,
                "id": uid,
                "value": value,
            }
            for date, uid, value in historical_df
        ]
    )

    # set data type
    cols = df.columns.tolist()
    dtypes = ["datetime64[ns]", "str", "float"]
    for col, dtype in zip(cols, dtypes):
        df[col] = df[col].astype(dtype)

    return df

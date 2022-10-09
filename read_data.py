import os
import time
from datetime import datetime as dt

import polars as pl

input_file_path = "Retail_Exercise_2022"
output_file_path = "consolidated.xlsx"


files = os.listdir(
    input_file_path,
)

# excel_file_list


# Run a for loop to loop through each file in the list
df_list = []
i = 0
tot_ = len(files)
times = []
for file_ in files:
    # check for .xlsx suffix files only
    start_time = time.perf_counter()
    if file_.endswith(".xlsx"):
        i += 1
        file_path = f"{input_file_path}/{file_}"
        file_df: pl.DataFrame = pl.read_excel(
            file=file_path, read_csv_options={"infer_schema_length": None}
        )
        date_string = " ".join(
            [item.strip().replace("-", "") for item in file_.split(".")[0].split()[-2:]]
        )

        try:
            date_ = dt.strptime(date_string, "%b %Y").date()
        except ValueError:
            date_ = dt.strptime(date_string, "%B %Y").date()

        file_df = file_df.select(
            [pl.lit(date_, dtype=pl.Datetime).alias("ID"), pl.all()]
        )
        # file_df.with_columns(pl.lit(date_, dtype=pl.Datetime).alias("ID"))
        df_list.append(file_df)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
        print(f"{i}. Finished {i} of {tot_} files.")
        print(f"Took {(end_time - start_time)} seconds for this file.")
        print(f"Approximately {(sum(times)/len(times)) * (tot_-i)} seconds left.")
        print("\n")

start_time = time.perf_counter()
df = pl.concat(df_list, rechunk=True, how="vertical", parallel=True)
end_time = time.perf_counter()
print(f"Took {end_time-start_time} seconds to concatenate all files.")

start_time = time.perf_counter()
df.write_csv("consolidated_data.csv", has_header=True)
end_time = time.perf_counter()
print(f"Took {end_time-start_time} seconds to write the df to disk.")
print("Done!")

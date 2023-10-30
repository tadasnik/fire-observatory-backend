import json
import pandas as pd
import numpy as np
from spatial_utils import get_UK_climate_region

data_file = "/Users/tadas/modFire/fire_lc_ndvi/data/cehlc/results/uk_fdi_all_vars_2002_2023_10_29.parquet"
dfr = pd.read_parquet(data_file)
dfr = get_UK_climate_region(dfr)

dfrg = (
    dfr.groupby(["Region", "time"])[["fwi", "ffmc", "dmc", "dc", "isi"]]
    .max()
    .reset_index()
)

dfrg["year"] = dfrg.time.dt.year
dfrg["month"] = dfrg.time.dt.month
dfrg["day"] = dfrg.time.dt.day
dfrg["date"] = pd.to_datetime(dfrg[["year", "month", "day"]])
dfrg["doy"] = dfrg.date.dt.dayofyear
dfrg["date"] = (dfrg["date"].astype(np.int64) / int(1e6)).astype(int)

columns = ["fwi", "ffmc", "dmc", "dc", "isi", "doy"]

for column in columns:
    dfrg[column] = dfrg[column].round(0).astype("uint8")

columns.insert(0, "date")

master_dict = {}
for region in dfrg.Region.unique():
    sub = dfrg[dfrg.Region == region]
    sub_dict = sub[columns].to_dict("records")
    master_dict[region] = sub_dict

with open("fire_weather_region_int.json", "w") as outfile:
    json.dump(master_dict, outfile)
#
# dfrg.to_json("fire_weather_UK_int_date_test.json", orient="records", date_unit="s")

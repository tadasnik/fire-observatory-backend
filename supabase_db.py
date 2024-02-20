import pandas as pd

from pathlib import Path
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions

class SupaDb:
    columns = [
            "id",
            "latitude",
            "longitude",
            "frp",
            "daynight",
            "timestamp",
            "lc",
            "country",
            "region",
            "event",
            "active",
        ]
    SQL_detections_dtypes = {
        "id": "int",
        "latitude": "float32",
        "longitude": "float32",
        "frp": "float32",
        "daynight": "int",
        "timestamp": object,
        "lc": "int",
        "country": object,
        "region": object,
        "event": "int",
        "active": bool,
    }


# Disable supabase connection timeout
    client_options = ClientOptions(postgrest_client_timeout=None)

    def __init__(self, url, key):
        self.client: Client | None = create_client(url, key, options=self.client_options)


if __name__ == "__main__":
    pass
    # dfr = pd.read_parquet(
    #     Path(Path.home(), "repos/activefire", "uk_viirs_fire_2024_1_30.parquet")
    # )
    # dfr["active"] = False
    # dfr["timestamp"] = pd.to_datetime(dfr["date"], unit="s", utc=True).astype(str)
    # dfr = dfr.rename({"Region": "region", "admin": "country"}, axis=1)
    # dfr = dfr[columns].astype(SQL_detections_dtypes)
    # data = supabase.table("detections").insert(dfr.to_dict(orient="records")).execute()

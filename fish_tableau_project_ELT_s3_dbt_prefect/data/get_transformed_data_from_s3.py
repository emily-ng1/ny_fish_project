import pandas as pd
import awswrangler as wr


def save_csv_from_s3_to_csv(name):
    url_path = f"s3://fish-project/mart/{name}_mart/{name}.csv"
    df = wr.s3.read_csv(url_path)
    df[0:3]

    save_to_filepath = f"/Users/emilyng/Data Engineering/Data Engineering BootCamp/Fish Project/fish_tableau_project_ELT_s3_dbt_prefect/data/{name}.csv"
    df.to_csv(save_to_filepath)

save_csv_from_s3_to_csv("dates")
save_csv_from_s3_to_csv("fishes")
save_csv_from_s3_to_csv("locations")
save_csv_from_s3_to_csv("waterbodies")




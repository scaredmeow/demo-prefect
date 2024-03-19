from tasks import extract_data, transform_data, load_data

from prefect import flow

@flow(name="Simple ETL Pipeline")
def etl_flow():
    raw_data = extract_data(source_config=None)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data, target_config=None)

if __name__ == "main":
    etl_flow()
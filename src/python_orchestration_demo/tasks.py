from prefect import task

# Sample task definitions for Extract, Transform, Load 
@task
def extract_data(source_config):
    # Simulating data extraction 
    data = {"raw_data": [1, 2, 3, 4, 5]}
    return data

@task
def transform_data(data):
    # Simulating transformation
    transformed_data = [x ** 2 for x in data["raw_data"]] 
    return transformed_data

@task
def load_data(data, target_config):
    # Simulating loading data
    print(f"Transformed data loaded: {data}")
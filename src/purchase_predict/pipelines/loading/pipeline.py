from kedro.pipeline import Pipeline, node

from .node import load_csv_from_bucket

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                load_csv_from_bucket,
                ["params:gcp_project_id", "params:gcs_primary_folder"],
                "primary",
            )
        ]
    )
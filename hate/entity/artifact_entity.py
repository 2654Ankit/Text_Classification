from dataclasses import dataclass



@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str

@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str
    
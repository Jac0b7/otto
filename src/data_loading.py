"""
------------------------------------------------------------------------------------------------------------------------

                                                    Data Loading:

------------------------------------------------------------------------------------------------------------------------
"""

# Environment Library's:
import pandas as pd
from pathlib import Path


class DataLoader:

    def __init__(self, file_path: Path, batch=None):
        self.path = file_path
        self.batch = batch

    # Loading process:
    def _batch(self):
        pass

    def _single(self):
        pass

    # Data Structures:
    def check_structure(self):
        suffix = self.path.suffix
        match suffix:
            case 'json':
                self._load_json()
            case 'parquet':
                pass
            case 'csv':
                pass

    @staticmethod
    def _load_json(file_path):
        pass

    @staticmethod
    def _load_parquet(file_path):
        pass

    @staticmethod
    def _load_csv(file_path):
        pass
    
    def structure_optimization(self):
        # Integer optimization:
        int_cols = self.data.slect_dtypes(include=int).columns
        self.data[int_cols] = pd.to_numeric(self.data[int_cols], downcast="integer")

        # Float optimization:
        int_cols = self.data.slect_dtypes(include=float).columns
        self.data[int_cols] = pd.to_numeric(self.data[int_cols], downcast="float")

        # Object - DateTime:

        # Object - Categorical:
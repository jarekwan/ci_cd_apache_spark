from pyspark.sql import DataFrame
from pyspark.sql import functions as F

from src.us_accidents_etl.config.settings import ETLConfig


def filter_high_severity(df: DataFrame, cfg: ETLConfig) -> DataFrame:
    return df.filter(F.col("Severity") >= cfg.min_severity)

"""
@TODO: Add more filters here as needed, e.g., filter by state, date range, etc.
"""


def apply_etl_filters(df: DataFrame, cfg: ETLConfig) -> DataFrame:
    return filter_high_severity(df, cfg)
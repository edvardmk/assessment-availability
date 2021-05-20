from datetime import datetime
from typing import Optional

import sqlite3
import pandas as pd
from pydantic import BaseModel


class Summary(BaseModel):
    """
    Summary return type
    """
    mean: float
    median: float
    sum: float
    max: float
    min: float


class Dataset():
    """
    A class to access an SQLite database and provide optionally filtered summaries

    Attributes:
        df (DataFrame): Database content as pandas dataframe

    Methods:
        get_summary (start_date=None, end_date=None)
    """

    def __init__(self):
        con = sqlite3.connect('availability.db')
        self.df = pd.read_sql_query(
            "SELECT * FROM service_availabilities", con, parse_dates=['date']
        )

    def get_summary(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Optional[Summary]:
        """
        Args:
            start_date (datetime or None): Earliest date of date range, inclusive
            end_date (datetime or None): Latest date of date range, inclusive

        Returns:
            summary (Summary or None): Summary of mean, median, sum, max and min availability within optionally provided date range
        """

        # filter for date range
        if start_date is not None and end_date is not None:
            df = self.df[(self.df['date'] >= start_date)
                         & (self.df['date'] <= end_date)]
        elif start_date is not None:
            df = self.df[self.df['date'] >= start_date]
        elif end_date is not None:
            df = self.df[self.df['date'] <= end_date]
        else:
            df = self.df

        ava = df.availability

        # generate and return summary or None if no data in range
        return None if df.empty else {
            "mean": ava.mean(),
            "median": ava.median(),
            "sum": ava.sum(),
            "max": ava.max(),
            "min": ava.min()
        }

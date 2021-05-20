from datetime import datetime
from typing import Optional

from fastapi import HTTPException, FastAPI, status

from availability import dataset, Summary

app = FastAPI()


def parse_date(date_string: Optional[str]) -> Optional[datetime]:
    """
    Tries to parse an incoming date string

    Args:
        date_string (str, optional): Date string to parse

    Raises:
        ValueError: Invalid input format

    Returns:
        parsed_date (datetime or None): Parsed date if date was provided 
    """

    if date_string is None:
        return

    return datetime.strptime(date_string, '%d.%m.%Y')


# response_model=Summary
@app.get("/summary", response_model=Summary,  status_code=200)
def get_summary(start_date: Optional[str] = None, end_date: Optional[str] = None):
    """
    Generates an summary for from data between the optionally provided dates

    Parameters:
        start_date (str, optional): Start date string of date range to parse, required format: dd.mm.yyyy
        end_date (str, optional): End date string of date range to parse, required format: dd.mm.yyyy
    """

    try:
        start_date = parse_date(start_date)
        end_date = parse_date(end_date)
    except ValueError:
        # raises 400 exception on invalid date string format
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid query parameter format.")

    if start_date is not None and end_date is not None and start_date > end_date:
        # raises 400 exception on invalid date range
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid date range.")

    # generates summary from the dataset module for the optionally provided dates
    summary = dataset.get_summary(start_date=start_date, end_date=end_date)

    if summary is None:
        # raises 404 if no data found within the provided bounds
        exxx = HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No data found."
        )
        print(exxx)
        print('aww man')
        print(exxx.status_code)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No data found."
        )

    # returns the generated summary
    return summary

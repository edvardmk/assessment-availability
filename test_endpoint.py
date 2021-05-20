import main

import pytest
from fastapi.exceptions import HTTPException


def test_returns_404_on_too_early_end_date():
    with pytest.raises(HTTPException) as excinfo:
        main.get_summary(end_date="01.01.1800")
    assert excinfo.value.status_code == 404


def test_returns_400_on_invalid_end_date_format():
    with pytest.raises(HTTPException) as excinfo:
        main.get_summary(end_date="01.01.18")
    assert excinfo.value.status_code == 400

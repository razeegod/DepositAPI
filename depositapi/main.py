from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from datetime import datetime
from dateutil.relativedelta import relativedelta


app = FastAPI()


class Deposit(BaseModel):
    date: str = Field(..., example="01.01.2000")
    periods: int = Field(..., ge=1, le=60)
    amount: int = Field(..., ge=10000, le=3000000)
    rate: float = Field(..., ge=1.0, le=8.0)


def validate_date(date):
    try:
        return datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")


def _calculate_deposit(deposit: Deposit, start_date: datetime):
    result = {}
    month_rate = deposit.rate / 100 / 12
    for i in range(deposit.periods):
        procent = deposit.amount * month_rate
        deposit.amount += procent
        result[(start_date + relativedelta(months=i)).strftime("%d.%m.%Y")] = round(deposit.amount, 2)
    return result


@app.get("/")
def root():
    return {'message': 'Hello world'}


@app.post("/calculate")
def calculate_deposit(request: Deposit):
    date = validate_date(request.date)
    return _calculate_deposit(request, date)

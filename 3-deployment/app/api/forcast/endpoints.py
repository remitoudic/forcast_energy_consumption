import base64
from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
from app.api.forcast.ingest import Data_preparation
from app.api.forcast.predict import Predict
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine

router = APIRouter()


@router.get("/")
def read_root():
    return {"": "welcome to me Mlops project"}


class Prediction(BaseModel):
    nb_day: int


@router.post("/predictions")
def forcasting(prediction: Prediction):
    if not prediction.nb_day:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    Data_preparation

    prediction = Predict.forcast(prediction.nb_day)

    return {"forcast": prediction}


@router.post("/graph_input_data")
def graph_current_input_data(prediction: Prediction):
    # Get database connection parameters from environment variables
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "postgres"
    POSTGRES_DB = "mlops_project"
    POSTGRES_HOST = "postgres"
    POSTGRES_PORT = "5432"

    # Create the database connection URL
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@ \
    {POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    engine = create_engine(DATABASE_URL)
    input_data = pd.read_sql("select * from energy_data", con=engine)
    input_data.set_index("date", inplace=True)
    predictions = Predict.forcast(prediction.nb_day)

    # Split train-test
    # ==============================================================
    steps = 30
    data_train = input_data[:-steps]
    data_test = input_data[-steps:]

    # Create plot
    fig, ax = plt.subplots(figsize=(15, 5))
    data_train["MWH"].plot(ax=ax, label="Train")
    data_test["MWH"].plot(ax=ax, label="Test")
    predictions.plot(ax=ax, label="predictions")
    ax.legend()
    ax.set_title("Train vs Test Data")
    ax.set_xlabel("date")
    ax.set_ylabel("MWH")

    # Save plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)  # Rewind the buffer to the beginning

    # Encode the image as base64
    img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    plt.close(fig)  # Close the plot to free up memory

    # Return the image data as a JSON response
    return JSONResponse(content={"image": img_base64})

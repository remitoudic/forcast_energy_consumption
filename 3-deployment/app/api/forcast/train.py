import joblib
from ingest import data
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import GradientBoostingRegressor

# Create and train forecaster
# ==============================================================================
forecaster = ForecasterAutoreg(
    regressor=GradientBoostingRegressor(random_state=10), lags=6
)

data_train = data["data_train"]
forecaster.fit(y=data_train["MWh"])
joblib.dump(forecaster, "models/forecaster_GradientBoostingRegressor.pkl")

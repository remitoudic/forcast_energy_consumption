import joblib
from app.api.forcast.ingest import data


class Predict:
    def forcast(nb_of_days_to_predict: int):
        # Load the saved model
        forecaster = joblib.load(
            "app/api/forcast/models/forecaster_GradientBoostingRegressor.pkl"
        )
        data_train = data["data_train"]
        forecaster.fit(y=data_train["MWh"])

        predictions = forecaster.predict(steps=nb_of_days_to_predict)
        # type(prediction = <class 'pandas.core.series.Series'>"
        return predictions


# # Plot predictions versus test data
# # ============================================================
# fig, ax = plt.subplots(figsize=(15, 5))
# data_train['MWh'].plot(ax=ax, label='train')
# data_test['MWh'].plot(ax=ax, label='test')
# predictions.plot(ax=ax, label='predictions')
# ax.legend()
# plt.show()

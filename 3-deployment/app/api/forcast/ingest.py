import pandas as pd


class Data_preparation:
    input_data = None
    years = [2022, 2023]

    def data_preparation(input_years: list[int]):
        def get_input_data(year: int):
            url_base = "https://github.com/remitoudic/mlops/raw/main/project"
            daily_cons = pd.read_excel(
                f"{url_base}/data%20/consumption/daily_{year}.xls",
                skiprows=17,
                usecols=lambda x: x if not x.startswith("Unnamed") else None,
            )

            daily_cons.dropna(inplace=True)
            daily_cons.reset_index(inplace=True, drop=True)
            daily_cons.drop(["Type de données"], inplace=True, axis=1)
            daily_cons.rename(
                columns={"Energie journalière (MWh)": "MWh"}, inplace=True
            )
            daily_cons.rename(columns={"Date": "date"}, inplace=True)
            daily_cons["date"] = pd.to_datetime(
                daily_cons["date"], format="%d/%m/%Y", errors="coerce"
            )
            return daily_cons

        def split_data(input_data, split_step: int):
            split_step = 30
            result = {
                "data_train": input_data[:-split_step],
                "data_test": input_data[-split_step:],
            }
            return result

        def data_preparation(years: list):
            all_years = None
            for year in years:
                this_year = get_input_data(year)
                assert (
                    this_year.shape[0] == 365
                ), f"Data issue => not 365 days in yer {year}"
                all_years = pd.concat([all_years, this_year])

            all_years.set_index("date", inplace=True)
            all_years.sort_index(inplace=True)
            all_years = all_years.asfreq("D", method="bfill")
            return all_years

        return split_data(data_preparation(input_years), 30)


data = Data_preparation.data_preparation(Data_preparation.years)


# print(data)
# assert int(data.shape[0]/len(Ingest.years))==365

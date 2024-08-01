import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def data_preparation():
    years=[2022,2023]
    all_years=None
    for year in years:
        this_year = get_input_data(year)
        assert this_year.shape[0]== 365, f"Data issue => not 365 days in yer {year}"
        all_years=  pd.concat([all_years, this_year])

    all_years.set_index('date', drop= False, inplace = True)
    all_years.sort_index(inplace = True)
    all_years = all_years.asfreq('D', method = 'bfill')
    return all_years

def get_input_data( year: int):

    daily_cons = pd.read_excel(f'https://github.com/remitoudic/mlops/raw/main/project/data%20/consumption/daily_{year}.xls', skiprows=17,  usecols=lambda x: x if not x.startswith('Unnamed') else None)
    daily_cons.dropna(inplace=True)
    daily_cons.reset_index(inplace=True,drop=True)
    daily_cons.drop(['Type de données'],inplace=True, axis=1)
    daily_cons.rename(columns={'Energie journalière (MWh)': "MWh"},inplace=True)
    daily_cons.rename(columns={'Date': "date"},inplace=True)
    daily_cons['date'] = pd.to_datetime(daily_cons['date'], format="%d/%m/%Y", errors='coerce')
    #daily_cons['date']=daily_cons['date'].dt.strftime('%m/%d/%Y')
    return daily_cons


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

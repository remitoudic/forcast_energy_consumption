import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # format and split data 
    #data['date'] = pd.to_datetime(data["date"].dt.strftime('%Y-%m'))
    #
    # split_step = 30
    # result ={ 'data_train': data[:-split_step],
    #          'data_test' :data[-split_step:]
    #         }
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products.melt(id_vars=['product_id'], 
                       var_name='store', 
                       value_name='price')
    return df.dropna(subset='price')
    
    
# df1 = (df.set_index(["location", "name"])
#          .stack()
#          .reset_index(name='Value')
#          .rename(columns={'level_2':'Date'}))
## DataFrame.dropna(*, axis=0, how=_NoDefault.no_default, thresh=_NoDefault.no_default, subset=None, inplace=False, ignore_index=False)

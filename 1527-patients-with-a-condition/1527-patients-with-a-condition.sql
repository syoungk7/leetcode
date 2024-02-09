import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    #print(patients.apply(lambda x:  patients.conditions.str.split() if i.str.startswith('DIAB1')))
    
    return patients[patients['conditions'].str.startswith('DIAB1') |
                    patients['conditions'].str.contains(' DIAB1')]

# Series.str.split(pat=None, *, n=-1, expand=False, regex=None): Split strings around given separator/delimiter.

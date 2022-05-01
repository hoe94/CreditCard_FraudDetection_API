import pandas as pd
import numpy as np

def downcast(df):
    cols = df.dtypes.index.tolist()
    types = df.dtypes.values.tolist()
    for i, t in enumerate(types):
        if 'int' in str(t):
            if (df[cols[i]].min() > np.iinfo(np.int8).min) and (df[cols[i]].max() < np.iinfo(np.int8).max):
                df[cols[i]] = df[cols[i]].astype(np.int8)
                
            elif (df[cols[i]].min() > np.iinfo(np.int16).min) and (df[cols[i]].max() < np.iinfo(np.int16).max):
                df[cols[i]] = df[cols[i]].astype(np.int16)
                
            elif (df[cols[i]].min() > np.iinfo(np.int32).min) and (df[cols[i]].max() < np.iinfo(np.int32).max):
                df[cols[i]] = df[cols[i]].astype(np.int32)
            
            else:
                df[cols[i]] = df[cols[i]].asypes(np.int64)
        elif 'float' in str(t):
            if (df[cols[i]].min() > np.finfo(np.float16).min) and (df[cols[i]].max() < np.finfo(np.float16).max):
                df[cols[i]] = df[cols[i]].astype(np.float16)
                
            elif (df[cols[i]].min() > np.finfo(np.float32).min) and (df[cols[i]].max() < np.finfo(np.float32).max):
                df[cols[i]] = df[cols[i]].astype(np.float32)
            
            else:
                df[cols[i]] = df[cols[i]].asypes(np.float64)
        elif t == object:
            if cols[i] == 'date':
                #df[cols[i]] = pd.to_datetime(df[cols[i]], format = '%Y-%m-%d')
                pass
            else:
                df[cols[i]] = df[cols[i]].astypes('category')
    return df

if __name__ == "__name__":
    downcast(df)
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = np.random.randint(0,100,(10,2))

# normalise the data using min max scalar
scaler_model = MinMaxScaler()

# fit the model to the data
scaler_model.fit(data)

# transform the data (this doesn't appear to work)
scaler_model.transform(data)
scaler_model.fit_transform(data)

# create an example of real data
myData = np.random.randint(0,101,(50,4))
df = pd.DataFrame(data=myData, columns = ['f1','f2','f3','label'])

X = data[['f1','f2','f3','label']]
y = df['label']

from sklearn.model_selection import train_test_split

# Run against test set
train_test_split(X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

print(df)
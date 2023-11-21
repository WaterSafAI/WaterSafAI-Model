import pandas as pd
import torch
from torch.utils.data import Dataset
from sklearn.preprocessing import StandardScaler


# Class for creating dataset from .csv file, where each column of the .csv file is a feature and
# each row is a data entry.
class FeatureDataset(Dataset):
    def __init__(self, file_name, is_labeled):
        # get row data from file
        file_out = pd.read_csv(file_name)
        print('Take a look at sample from the dataset:')
        print(file_out.head())
        print(file_out['Potability'].value_counts())

        input = file_out.iloc[:, 1:-1] if is_labeled else file_out.iloc[:, 0:-1]
        print('\nInput values are:')
        print(input.head())

        output = file_out.loc[:, 'Potability']
        print('\nThe output value is:')
        print(output.head())

        # Feature Scaling
        sc = StandardScaler()
        input = sc.fit_transform(input)
        input = torch.Tensor(input)
        print('\nInput format: ', input.shape, input.dtype)
        output = torch.tensor(output.to_numpy())  # Create tensor type torch.int64
        print('Output format: ', output.shape, output.dtype)

        # convert to torch tensors
        self.X_train = input
        self.y_train = output

    def __len__(self):
        return len(self.y_train)

    def __getitem__(self, idx):
        return self.X_train[idx], self.y_train[idx]

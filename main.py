import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from models import Network
from datasets import FeatureDataset
from train import train
from validate import test

if __name__ == '__main__':
    # The model is set up to work with the kaggle water quality dataset found in './data'
    # Kaggle dataset has 3276 entries with 9 features, and are labeled with a 1 if potable, 0 if not
    # input size is 9 and output size is 2
    num_features = 9
    num_entries = 3276
    num_outputs = 2
    learning_rate = 0.01
    num_epochs = 10
    batch_size = 1

    data_file = 'data/water_potability.csv'
    is_labeled = True

    print("Learning Rate: ", learning_rate)
    print("Batch size: ", batch_size)

    # check for CUDA availability
    use_cuda = torch.cuda.is_available()

    # set device for pytorch
    device = torch.device("cuda" if use_cuda else "cpu")
    print("Torch device selected: ", device)
    print("Cuda Version: ", torch.version.cuda)

    # initialize model
    model = Network(num_features, num_outputs).to(device)

    # initialize criterion for loss computation
    criterion = nn.CrossEntropyLoss(reduction='mean')

    # initialize optimizer
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=1e-7)

    # initialize dataset
    dataset = FeatureDataset(data_file, is_labeled)

    # generator for random dataset split
    generator = torch.Generator().manual_seed(5)

    # split dataset for training and validation
    train_set, val_set = torch.utils.data.random_split(dataset, [0.75, 0.25], generator=generator)

    # load dataset
    train_loader = DataLoader(train_set, batch_size=10, shuffle=True)
    test_loader = DataLoader(val_set, batch_size=1, shuffle=False)

    best_accuracy = 0.0

    for epoch in range(1, num_epochs + 1):
        print("\nEpoch: ", epoch)
        train_loss, train_accuracy = train(model, device, train_loader, optimizer, criterion, epoch, 10)
        test_loss, test_accuracy = test(model, device, test_loader)

        if test_accuracy > best_accuracy:
            best_accuracy = test_accuracy

    print("accuracy is {:2.2f}".format(best_accuracy))

    print("Training and evaluation finished")



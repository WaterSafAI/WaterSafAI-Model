import torch
import torch.nn as nn
import numpy as np

def train(model, device, train_loader, optimizer, criterion, epoch, batch_size):
    '''
    Trains the model for an epoch and optimizes it.
    model: The model to train. Should already be in correct device.
    device: 'cuda' or 'cpu'.
    train_loader: dataloader for training samples.
    optimizer: optimizer to use for model parameter updates.
    criterion: used to compute loss for prediction and target
    epoch: Current epoch to train for.
    batch_size: Batch size to be used.
    '''

    # Set model to train mode before each epoch
    model.train()

    # Empty list to store losses
    losses = []
    correct = 0

    # Iterate over entire training samples (1 epoch)
    for batch_idx, batch_sample in enumerate(train_loader):
        data, target = batch_sample

        # Push data/label to correct device
        data, target = data.to(device), target.to(device)
        # print(data.shape)
        # print(target.shape)
        # exit()

        # Reset optimizer gradients. Avoids grad accumulation (accumulation used in RNN).
        optimizer.zero_grad()

        # Do forward pass for current set of data
        output = model(data)

        # ======================================================================
        # Compute loss based on criterion
        criterion = nn.CrossEntropyLoss()

        # Remove NotImplementedError and assign correct loss function.
        loss = criterion(output, target)

        # Computes gradient based on final loss
        loss.backward()

        # Store loss
        losses.append(loss.item())

        # Optimize model parameters based on learning rate and gradient
        optimizer.step()

        # Get predicted index by selecting maximum log-probability
        pred = output.argmax(dim=1, keepdim=True)

        # ======================================================================
        # Count correct predictions overall
        correct += pred.eq(target.view_as(pred)).sum().item()

    train_loss = float(np.mean(losses))
    train_acc = correct / ((batch_idx + 1) * batch_size)
    print('Train set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)'.format(
        float(np.mean(losses)), correct, (batch_idx + 1) * batch_size,
                                         100. * correct / ((batch_idx + 1) * batch_size)))
    return train_loss, train_acc
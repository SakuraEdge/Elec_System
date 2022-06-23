import pickle
import numpy as np
import pandas as pd
import torch
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from torch.utils.data import DataLoader
from pageFrame.static.file.send_pkg.visualizer import train_log_curve
from pageFrame.static.file.send_pkg.model import Net


# tools
def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True


@torch.no_grad()
def get_test_acc(model, dataloader, num_test_sample, device):
    model.eval()
    running_loss = 0.0
    running_acc = 0.0
    for i, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        output = model(X)
        prob = torch.softmax(output, dim=1)
        pred = torch.argmax(prob, dim=1)
        loss = torch.nn.functional.cross_entropy(output, y)

        running_loss += loss.item()
        running_acc += torch.sum(pred == y).item()
    test_loss = running_loss / num_test_sample
    test_acc = running_acc / num_test_sample

    return test_loss, test_acc


# Hyperparameters
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
setup_seed(42)
split = 0.3
hidden_size = 20
batch_size = 20
learning_rate = 0.0005
epochs = 20

df = pd.read_csv('pageFrame\\static\\file\\send_pkg\\meidi\\merged_data.csv')
X = df.drop(['type'], axis=1).values
y = df['type'].values

encoder = LabelEncoder()
sc = StandardScaler()

y = encoder.fit_transform(y)
X = sc.fit_transform(X)

# split train/val and get dataset
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=split)
train_X = torch.from_numpy(train_X).float()
train_y = torch.from_numpy(train_y).long()
val_X = torch.from_numpy(val_X).float()
val_y = torch.from_numpy(val_y).long()

num_train_sample = train_X.shape[0]
num_val_sample = val_X.shape[0]

train_ds = torch.utils.data.TensorDataset(train_X, train_y)
val_ds = torch.utils.data.TensorDataset(val_X, val_y)
train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=False)
val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False)

# model definiation
model = Net(hidden_size)
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-5)
model.to(device)

train_loss_list = []
train_acc_list = []
val_loss_list = []
val_acc_list = []

best_acc = 0.0
# train model
for epoch in range(epochs):
    running_loss = 0.0
    running_acc = 0.0
    test_loss, test_acc = get_test_acc(model, val_loader, num_val_sample, device)
    model.train()
    for i, (X, y) in enumerate(train_loader):
        X, y = X.to(device), y.to(device)
        output = model(X)
        loss = loss_fn(output, y)
        prob = torch.softmax(output, dim=1)
        pred = torch.argmax(prob, dim=1)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        running_acc += torch.sum(pred == y).item()

    epoch_loss = running_loss / num_train_sample
    epoch_acc = running_acc / num_train_sample
    print(
        'Epoch: {}, Train Loss: {:.3f}, Train Acc: {:.3f}, Val Loss: {:.3f}, Val Acc: {:.3f}'.format(epoch, epoch_loss,
                                                                                                     epoch_acc,
                                                                                                     test_loss,
                                                                                                     test_acc))
    if test_acc > best_acc:
        best_acc = test_acc
        torch.save(model.state_dict(), 'pageFrame\\static\\file\\send_pkg\\model\\企业电力营销模型.mdl')
        print('Best model saved!')
    train_loss_list.append(epoch_loss)
    train_acc_list.append(epoch_acc)
    val_loss_list.append(test_loss)
    val_acc_list.append(test_acc)

train_log = {'train_loss': train_loss_list, 'train_acc': train_acc_list, 'val_loss': val_loss_list,
             'val_acc': val_acc_list}
with open('pageFrame\\static\\file\\send_pkg\\logs\\Task4TrainLog.pkl', 'wb') as f:
    f.write(pickle.dumps(train_log))




















def get_two_lines():
    train_loss = train_log['train_loss']
    train_acc = train_log['train_acc']
    val_loss = train_log['val_loss']
    val_acc = train_log['val_acc']
    loss_train_lst = []
    loss_val_lst = []
    acc_train_lst = []
    acc_val_lst = []
    for val1, val2, val3, val4 in zip(list(train_loss), list(val_loss), list(train_acc), list(val_acc)):
        loss_train_lst.append(val1)
        loss_val_lst.append(val2)
        acc_train_lst.append(val3)
        acc_val_lst.append(val4)
    return {
        'loss_train_lst': loss_train_lst,
        'loss_val_lst': loss_val_lst,
        'acc_train_lst': acc_train_lst,
        'acc_val_lst': acc_val_lst,
        'label': [item for item in range(1, len(loss_train_lst) + 1)]
    }

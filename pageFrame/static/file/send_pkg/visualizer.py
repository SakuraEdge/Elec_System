import pickle
from matplotlib import pyplot as plt


def train_log_curve(log_dict):
    train_loss = log_dict['train_loss']
    train_acc = log_dict['train_acc']
    val_loss = log_dict['val_loss']
    val_acc = log_dict['val_acc']
    figure = plt.figure(figsize=(3, 6), dpi=144)
    ax1 = figure.add_subplot(211)
    ax1.plot(train_loss, label='train_loss')
    ax1.plot(val_loss, label='val_loss')
    ax1.legend()
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.set_title('Task4 Loss Curve')
    ax2 = figure.add_subplot(212)
    ax2.plot(train_acc, label='train_acc')
    ax2.plot(val_acc, label='val_acc')
    ax2.legend()
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.set_title('Task4 Accuracy Curve')
    plt.tight_layout()
    plt.savefig('pageFrame\\static\\file\\send_pkg\\plot\\Task4TrainLog.png')




if __name__ == '__main__':
    train_log = 'logs/Task4TrainLog.pkl'
    with open(train_log, 'rb') as f:
        log_dict = pickle.loads(f.read())
    auc_log = 'logs/Task4AUCLog.pkl'

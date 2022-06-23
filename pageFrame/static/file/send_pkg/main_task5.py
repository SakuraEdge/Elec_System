import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import pickle
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.manifold import TSNE

df = pd.read_csv('pageFrame\\static\\file\\send_pkg\\meidi\\merged_data.csv')
X = df.drop(['type'], axis=1).values
y = df['type'].values

encoder = LabelEncoder()
sc = StandardScaler()

y = encoder.fit_transform(y).reshape(-1, 1)
X = np.concatenate((X, y), axis=1)
X = sc.fit_transform(X)

cluster = KMeans(n_clusters=3)

cluster.fit(X)
C_i = cluster.predict(X)

tsne = TSNE(init='pca')
X2 = tsne.fit_transform(X)
figure = plt.figure(figsize=(5, 5), dpi=144)
plt.scatter(X2[:, 0], X2[:, 1], c=C_i, s=50, cmap='viridis')
plt.axis('off')
plt.title('Task5 cluster')
plt.savefig('pageFrame\\static\\file\\send_pkg\\plot\\Task5cluster.png')

# save model
with open('pageFrame\\static\\file\\send_pkg\\model\\电力用电量集群分析模型.mdl', 'wb') as f:
    pickle.dump(cluster, f)
    f.close()

# save label
cluster_label = pd.DataFrame(columns=['cluster'])
cluster_label['cluster'] = C_i
cluster_label.to_csv('pageFrame\\static\\file\\send_pkg\\plot\\task5_label.csv', index=False)


def get_cla_echarts_data():
    lst = []
    new_C_i = []
    for val1, val2, val3 in zip(list(X2[:, 0]), list(X2[:, 1]), list(C_i)):
        lst.append([float(val1), float(val2)])
        new_C_i.append(float(val3))
    return {
        'cla_data': lst,
        'cla_flag': new_C_i,

        'line_data': {
            'type_cla': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 2.5, 2.5, 2.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 2.5, 2.5, 2.5, 1.5, 1.5],
            'time_lst': ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9', '9-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23', '23-24']
        }
    }


def get_result(elec_load, elec_pay):
    new_X = df.drop(['type'], axis=1).values
    new_y = df['type'].values
    new_y = encoder.fit_transform(new_y).reshape(-1, 1)
    cluster = KMeans(n_clusters=3)
    cluster.fit(new_X, new_y)
    loadx = np.array(elec_load)
    loadx = np.append(loadx, elec_pay)
    print(loadx)
    result_point = cluster.predict([loadx])
    if result_point == 0:
        return '当前时段用电量处于低谷状态'
    elif result_point == 1:
        return '当前时段用电量处于平段状态'
    else:
        return '当前时段用电量处于高峰状态'


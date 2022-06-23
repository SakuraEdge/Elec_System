import pandas as pd


def show_three_types():
    data = pd.read_csv('meidi/merged_data.csv')
    data.columns = ['power', 'money', 'type']

    low_num = 0
    center_num = 0
    high_num = 0

    high_power = 0
    low_power = 0
    center_power = 0

    high_money = 0
    low_money = 0
    center_money = 0

    for index in range(len(data)):
        if data['type'][index] == '高峰':
            high_money += data['money'][index]
            high_power += data['power'][index]
            high_num += 1
        elif data['type'][index] == '平段':
            center_money += data['money'][index]
            center_power += data['power'][index]
            center_num += 1
        else:
            low_money += data['money'][index]
            low_power += data['power'][index]
            low_num += 1

    avg_money = [low_money / low_num, center_money / center_num, high_money / high_num]
    avg_power = [low_power / low_num, center_power / center_num, high_power / high_num]
    num = [low_num, center_num, high_num]
    return avg_power, avg_money, num

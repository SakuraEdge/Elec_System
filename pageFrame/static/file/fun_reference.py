import pandas
from datetime import datetime
import re

# 导入测试数据
data = pandas.read_csv('pageFrame\\static\\file\\base_data.csv')

# 对测试数据属性定义
data.columns = ['uid', 'date', 'money']

# 对数据进行排序
data[['uid', 'money']].sort_values("uid")

# 统计每个用户的缴费次数与总缴费金额
uid_num = data['money'].groupby(data['uid']).count()
uid_money = data['money'].groupby(data['uid']).sum()

# 计算总体缴费金额与缴费次数
all_num = uid_num.count()
avg_num = uid_num.sum() / all_num
avg_money = uid_money.sum() / all_num

print(avg_num, avg_money)

# 判断客户属于哪种类别
pd = pandas.DataFrame({'pd': []})

pd.index = pd.index + 1
group_pd = pandas.DataFrame({'num': data['uid'].groupby(data['uid']).count(),
                             'money': data['money'].groupby(data['uid']).sum()}, columns=['num', 'money'])

group_pd.reset_index(inplace=True)
group_pd.index = group_pd.index + 1


def pd_moneys(user_money):
    if user_money >= avg_money:
        return True
    else:
        return False


def pd_nums(user_num):
    if user_num >= avg_num:
        return True
    else:
        return False


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False


def is_month(month):
    if month == '1' or month == '2' or month == '3' or month == '4' or month == '5' or month == '6':
        return False
    return True


def pd_center(num, money):
    if pd_nums(num):
        if pd_moneys(money):
            result = '高价值型客户'
        else:
            result = '大众型客户'
    else:
        if pd_moneys(money):
            result = '潜力型客户'
        else:
            result = '低价值型客户'
    return result


def switch_result(pd_result):
    return {
        '高价值型客户': 0,
        '大众型客户': 1,
        '潜力型客户': 2,
        '低价值型客户': 3
    }.get(pd_result)


def get_Avg():
    Load_Avg_to_csv()
    return avg_num, avg_money


def Load_Avg_to_csv():
    df = pandas.DataFrame({'平均缴费次数': [avg_num], '平均消费金额': [avg_money]})
    df.to_csv("pageFrame\\static\\file\\居民客户的用电缴费习惯分析 1.csv", encoding="utf-8-sig", index=False)


def get_Group_Num():
    pd_count = [0, 0, 0, 0]
    for i in range(1, group_pd.shape[0] + 1):
        temp_num = group_pd.loc[i].num
        temp_money = group_pd.loc[i].money
        pd_result = pd_center(temp_num, temp_money)
        pd.loc[i] = pd_result
        pd_count[switch_result(pd_result)] += 1
    return pd_count


def get_Group_to_csv():
    get_Group_Num()
    group_pd_2 = pandas.concat([group_pd, pd], axis=1)
    group_pd_2.columns = ['用户编号', '缴费次数', '缴费金额', '客户类型判断']
    group_pd_2.to_csv("pageFrame\\static\\file\\居民客户的用电缴费习惯分析 2.csv", encoding="utf-8-sig", index=False)


def top_Group(nowdate, input_month):
    """
    计算X个月缴费情况
    """
    # 时间返回X个月前
    year = int(nowdate / 10000)
    month = int(nowdate / 100 % 100)
    day = int(nowdate % 100)
    old_date = datetime(year, month, day)
    if input_month == 12:
        year = year - 1
    else:
        new_month = month - input_month
        if new_month <= 0:
            new_month = 12 + new_month
            year = year - 1
    new_date = datetime(year, new_month, day)
    old_date = old_date.strftime('%Y%m%d')
    new_date = new_date.strftime('%Y%m%d')

    # 计算六个月内的缴费次数与缴费金额
    get_Group_Num()
    data['counts'] = pandas.to_datetime(data['date'])
    data1 = data[(data['counts'] >= pandas.to_datetime(new_date)) & (data['counts'] <= pandas.to_datetime(old_date))]
    uid_data = data1['counts'].groupby(data1['uid']).count()
    uid_money = data1['money'].groupby(data1['uid']).sum()
    top_pd = pandas.concat([uid_data, uid_money], axis=1)
    top_pd = pandas.DataFrame(top_pd)
    top_pd.reset_index(inplace=True)
    top_pd.index = top_pd.index + 1
    top_pd = pandas.concat([top_pd, pd], axis=1)
    # 剔除高价值型用户
    top_pd = top_pd[~(top_pd['pd'] == '高价值型客户')]

    '''
    计算权重
    '''
    # 获取剔除后的平均值
    top_num = top_pd['counts']
    top_money = top_pd['money']
    top_all_num = top_num.count()
    top_avg_num = top_num.sum() / top_all_num
    top_avg_money = top_money.sum() / top_all_num
    top_pd.reset_index(inplace=True)
    top_pd.index = top_pd.index + 1
    del top_pd['index']
    # 计算权重
    tops = pandas.DataFrame({'weight': []})
    for i in range(1, top_pd.shape[0] + 1):
        temp_count = top_pd.loc[i].counts
        temp_money = top_pd.loc[i].money
        pd_result = (temp_count / top_avg_num + temp_money / top_avg_money) / 2
        tops.loc[i] = pd_result
    top_pd = pandas.concat([top_pd, tops], axis=1)

    top_pd.sort_values("weight", inplace=True, ascending=False)
    top_five = top_pd.iloc[:5, :]
    return top_five


def top_Group_to_csv(date, month):
    top_pd = top_Group(date, month)
    top_pd.to_csv("pageFrame\\static\\file\\居民客户的用电缴费习惯分析 3.csv", encoding="utf-8-sig", index=False)


def top_Group_to_view(date, month):
    top_pd = top_Group(date, month)
    top_pd.reset_index(inplace=True)
    top_pd.index = top_pd.index + 1
    del top_pd['index']
    top_list = []
    top_weight_list = []
    for i in range(1, 6):
        try:
            top_list.append(int(top_pd.loc[i].uid))
            top_weight_list.append(round(float(top_pd.loc[i].weight), 6))
        except ValueError:
            return ''
    return top_list, top_weight_list


def show_echarts_avg_data():
    dict = {}
    for item in range(1, 13):
        dict[str(item)] = []

    obj = re.compile(r".*?/(?P<month>.*?)/.*?", re.S)

    # print(data['date'][1])

    for index in range(len(data)):
        result = obj.finditer(data['date'][index])
        for item in result:
            if item.group('month'):
                # print(item.group('month'))
                dict[item.group('month')].append(int(data['money'][index]))
    # print(dict)
    date_lst = []
    money_lst = []
    times_lst = []
    for key, val in dict.items():
        sum = 0
        for item in val:
            sum += item
        date_lst.append(key + '月')
        money_lst.append(str(sum))
        times_lst.append(str(len(val)))
    print(money_lst)
    print(money_lst)
    return {'date_lst': date_lst, 'money_lst': money_lst, 'times_lst': times_lst}


def show_three_types():
    data = pandas.read_csv('pageFrame\\static\\file\\send_pkg\\meidi\\merged_data.csv')
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

    avg_money = [round(low_money / low_num, 2), round(center_money / center_num, 2), round(high_money / high_num, 2)]
    avg_power = [round(low_power / low_num, 2), round(center_power / center_num, 2), round(high_power / high_num, 2)]
    num = [low_num, center_num, high_num]
    return {
             'type_lst': ['低谷', '平断', '高峰'],
             'avg_power': avg_power,
             'avg_money': avg_money,
             'num': num
        }


# 注册
def is_reasonable(user, password, rep_password):
    if not user or not password or not rep_password:
        return '以上的信息不能为空！'
    if password != rep_password:
        return '两次输入密码不一致！'
    return ''


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from pageFrame.models import UserInfo
# Create your views here.


login_flag = False


def login(request):
    global login_flag
    if request.method == 'GET':
        return render(request, 'login.html')
    if 'login' in request.POST:
        act = request.POST['act']
        pwd = request.POST['pwd']
        if act == '' or pwd == '':
            return render(request, 'login.html', {'login_err_msg': '用户名或密码不能为空!'})
        if UserInfo.objects.filter(account=act, password=pwd):
            print(act, pwd)
            login_flag = True
            return redirect('/index/')
        return render(request, 'login.html', {'login_err_msg': '用户名或密码输入错误!'})


def register(request):
    return render(request, 'register.html')


def reg_result(request):
    from pageFrame.static.file.fun_reference import is_reasonable
    act = request.GET['act']
    pwd = request.GET['pwd']
    rep_pwd = request.GET['rep_pwd']
    if UserInfo.objects.filter(account=act):
        return HttpResponse('该用户名已被注册了！')
    if is_reasonable(act, pwd, rep_pwd) != '':
        return HttpResponse(is_reasonable(act, pwd, rep_pwd))
    UserInfo.objects.create(account=act, password=pwd)
    return HttpResponse(' ')


def index(request):
    if request.method == "GET":
        if not login_flag:
            return redirect('/login/')
        return render(request, 'index1.html', {'chart_data': '暂无数据'})
    return render(request, 'index1.html')


def index2(request):
    if request.method == "GET":
        if not login_flag:
            return redirect('/login/')
        return render(request, 'index2.html', {'chart_data': '暂无数据'})
    return render(request, 'index2.html')


def show_avg_data(request):
    from pageFrame.static.file.fun_reference import get_Avg, Load_Avg_to_csv

    avg_num, avg_money = get_Avg()
    Load_Avg_to_csv()
    return HttpResponse(str(avg_money) + ' ' + str(avg_num))


def show_four_classes(request):
    from pageFrame.static.file.fun_reference import get_Group_Num, get_Group_to_csv
    get_Group_to_csv()
    lst = get_Group_Num()
    data = ''.join(str(item) + ' ' for item in lst)
    return HttpResponse(data)


def show_pre_data(request):
    from pageFrame.static.file.fun_reference import pd_center, is_number
    print(request.GET)
    money_pre = request.GET['money_pre']
    times_pre = request.GET['times_pre']

    if not is_number(money_pre) or not is_number(times_pre):
        return HttpResponse('数据输入为空或有误！')
    res = pd_center(float(money_pre), float(times_pre))
    print(res)
    return HttpResponse(res)


def show_pre_top5(request):
    from pageFrame.static.file.fun_reference import top_Group_to_view, is_month, top_Group_to_csv
    now_date = request.GET['now_date']
    date = ''
    for item in now_date:
        if item == '-':
            continue
        date = date + item
    month = request.GET['month']
    if is_month(month):
        return HttpResponse('')
    print(date, month)
    uid, weight = (top_Group_to_view(int(date), int(month)))
    top_Group_to_csv(int(date), int(month))
    print(uid)
    print(weight)
    return JsonResponse({'uid': uid, 'weight': weight})


def show_avg_echarts(request):
    from pageFrame.static.file.fun_reference import show_echarts_avg_data
    return JsonResponse(show_echarts_avg_data())


def show_three_class(request):
    from pageFrame.static.file.fun_reference import show_three_types
    print(show_three_types())
    return JsonResponse(show_three_types())


def show_pre_user_type5(request):
    from pageFrame.static.file.send_pkg.main_task5 import get_result
    from pageFrame.static.file.fun_reference import is_number
    power_data = request.GET['power_data']
    money_data = request.GET['money_data']
    if not is_number(power_data) or not is_number(money_data):
        return HttpResponse('数据输入为空或有误！')
    return HttpResponse(get_result(float(power_data), float(money_data)))


def get_cla_echarts_data(request):
    from pageFrame.static.file.send_pkg.main_task5 import get_cla_echarts_data
    return JsonResponse(get_cla_echarts_data())


def get_two_line_echarts(request):
    from pageFrame.static.file.send_pkg.main_task4 import get_two_lines
    print(get_two_lines())
    return JsonResponse(get_two_lines())


def get_two_sketches(request):

    return JsonResponse({
        'T4': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp'
              ';本任务是根据当前时段的用电量和金额，推测出当前时段的分类。将表中每一行数据，每个时间点，每个时间，每个小时的数据作为一个样本，然后这个样本的特征就是用电量和缴费金额，标签就是这个时间点是高峰平段还是低谷。就这样的数据类型到一个多层的神经网络，通过四至五层的训练，在通过分类。形成三类分类。训练完成后利用测试集对模型性能进行评估。',
        'T5': '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp'
              ';本任务是对当前用电量进行聚类分析，不仅利用了用电量这一维度，还利用了欠费信息，当前时段的状态（高峰/平段/低谷），这一离散特征。利用这三个特征作为本次聚类的特征，同时利用KMeans'
              '算法对所有的数据进行了一个聚类，最后聚类的类数也可以作为一个超参来进行调整，最后可根据后续的分析需求取调整。 '
    })


def exit(request):
    global login_flag
    login_flag = False
    return redirect('/login/')
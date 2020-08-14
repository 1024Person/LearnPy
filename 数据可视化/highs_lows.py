import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)  # 用的是csv模块中的方法
    # print(reader)
    header = next(reader)  # 只是读取了一行，将文件头读出
    # 并没有全部读出
    lows, times, highs = [], [], []

    for row in reader:
        try:  # 检测异常
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing date')
        else:
            times.append(date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(1, dpi=128, figsize=(10, 5))
    plt.subplot(211)

    plt.plot(times, highs, '-r', times, lows, '-g')  # 将所有的数据都存放到缓冲区里面
    plt.fill_between(times, lows, highs, facecolor='blue', alpha=0.2)
    plt.title('Daily high Temperature   ', fontsize=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperatures', fontsize=12)
    fig.autofmt_xdate()  # 自动调整x轴的间距，并且指出x轴为时间轴
    # plt.plot(times, lows, c='blue')  # 再次向缓冲区中存放数据
    plt.fill_between(times, lows, highs, facecolor='blue', alpha=0.2)
    times, lows, highs = [], [], []
    with open(filename2) as f:
        reader = csv.reader(f)
        #
        header = next(reader)
        #
        for row in reader:
            #
            try:
                high = int(row[1])
                low = int(row[3])
                date = datetime.strptime(row[0], '%Y-%m-%d')
            #
            except Exception as r:
                print(r)
            #
            else:
                times.append(date)
                highs.append(high)
                lows.append(low)
    #
    plt.subplot(212)
    plt.plot(times, highs, '-y', times, lows)
    # plt.plot(times, lows, c='green', linewidth=3)
    plt.fill_between(times, lows, highs, facecolor='blue', alpha=0.2)
    # plt.title('Daily high Temperature   ', fontsize=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperatures', fontsize=12)
    fig.autofmt_xdate()  # 自动调整x轴的间距，并且指出x轴为时间轴

    plt.show()

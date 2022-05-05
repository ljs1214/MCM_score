import requests

import time


team_num = '22xxxxx'   # 填写自己的队伍号码
test_num = "2210000"  # 从第一个队伍编号开始访问，因为按往年来说都是按顺序出成绩, 如果周围有比你队伍号小的队出成绩了可以从他们的开始试
while True:
    url = 'https://www.comap-math.com/mcm/2022Certs/{}.pdf'.format(test_num)
    response = requests.get(url)
    if response.status_code == 200:
        if abs(int(test_num) - int(team_num)) >= 10:  # 以10为步长测试目前出到几号成绩了
            print("No.", test_num, "score has been published!")
            test_num = str(int(test_num)+10)
        else:  # 如果离自己队伍号小于10了就开始蹲自己的
            test_num = team_num
        if test_num == team_num:
            print("you team: ", team_num, "score has been published!")
            with open(team_num+".pdf", 'wb') as f:
                f.write(response.content)  # 下载到本地
            break
        print((abs(int(test_num) - int(team_num))), "teams left")
    else:
        print("newest: ", test_num)
    # time.sleep(5)
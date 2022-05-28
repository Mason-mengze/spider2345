# import pyttsx3 #导入
# #创建  初始化
# engine = pyttsx3.init()
# #说话
# engine.say('晋睿敏，你是我遥遥万里牵挂的猪，哈哈')
# #运行
# engine.runAndWait()


import csv
f = open('2.csv', 'a+')
we = csv.writer(f)
we.writerow('haojam')
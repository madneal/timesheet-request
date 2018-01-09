import requests
import json
import time

base_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&line='
line_num_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17]
result = []
filename = 'timesheet.json'

def crawler():
    for line_num in line_num_arr:
        print('request for line ' + str(line_num))
        make_request(base_url + str(line_num))
    print('request finished!')
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False)


def make_request(url):
    r = requests.get(url)
    result_arr = r.json()
    result.append(result_arr)



if __name__ == '__main__':
    crawler()
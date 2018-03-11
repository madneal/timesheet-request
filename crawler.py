import requests
import json

base_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&line='
station_info_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=stationInfo&stat_id='
station_timesheet_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&stat_id=111'

line_num_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17]
filename = 'timesheet.json'
station_file = 'station.json'


def read_json(filename):
    with open(filename, 'r', encoding='utf8') as f:
        return json.load(f);


def write_json(filename, data):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
        f.close()


def carwler_station_info():
    keys = read_json('key.json')
    result = []
    for key in keys:
        station_name = list(key.keys())[0]
        station_id = key[station_name]
        url = station_info_url + station_id
        station_info = make_request(url)
        result = result + station_info
    write_json('stationInfo.json', result)


def crawler():
    result = []
    for line_num in line_num_arr:
        print('request for line ' + str(line_num))
        make_request(base_url + str(line_num))
    print('request finished!')
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False)


def make_request(url):
    r = requests.get(url)
    return r.json()


def format_station_info():
    timesheet = read_json('timesheet1.json')
    data = []
    result = {}
    for arr in timesheet:
        data = data + arr
    print(data)
    for ele in data:
        name = ele['name']
        if not name in result.keys():
            result[name] = [ele]
        else:
            result[name].append(ele)
    print(result)
    print(timesheet)


if __name__ == '__main__':
    # crawler()
    # carwler_station_info()
    format_station_info()
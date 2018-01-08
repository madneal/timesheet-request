import requests

base_url = 'http://m.shmetro.com/interface/metromap/metromap.aspx?func=fltime&line='
line_num_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17]

def crawler():
    for line_num in line_num_arr:
        make_request(base_url + str(line_num))

def make_request(url):
    r = requests.get(url)
    result_arr = r.json()
    


if __name__ == '__main__':
    crawler()
import json

filename = 'timesheet.json'
result = []
key_arr = ['stat_id', 'station_code', 'first_time', 'first_time_desc', 'last_time', 'last_time_desc', 'direction', 'description']
# stat_id = 'stat_id'
# station_code = 'station_code'
# first_time = 'first_time'
# first_time_desc = 'first_time_desc'
# last_time = 'last_time'
# last_time_desc = 'last_time_desc'
# direction = 'direction'
# description = 'description'

def parse():
    with open(filename, 'r', encoding='utf8') as arr:
        line_arr = json.load(arr)
        for line in line_arr:
            # line_name = line + '号线'
            # line_data = {}
            # result[line_name] = line_data
            last_name = None
            for station in line:
                name = station['name']
                if last_name is None or name is not last_name:
                    name_obj = {
                        name: station['stat_id']
                    }
                    # name_obj[name] = station['stat_id']
                    result.append(name_obj)
                    last_name = name
    with open('key.json', 'w', encoding='utf8') as f:
        json.dump(result, f, ensure_ascii=False)


if __name__ == '__main__':
    parse()

import numpy as np

def get_usr_info(path):
    # convert gender，M-0， F-1
    def gender2num(gender):
        return 1 if gender == 'F' else 0
    
    with open(path, 'r') as f:
        data = f.readlines()
    # user info dict
    use_info = {}
    
    max_usr_id = 0
    for item in data:
        item = item.strip().split("::")
        usr_id = item[0]
        use_info[usr_id] = {'usr_id': int(usr_id),
                            'gender': gender2num(item[1]),
                            'age': int(item[2]),
                            'job': int(item[3])}
        max_usr_id = max(max_usr_id, int(usr_id))
    
    return use_info, max_usr_id


usr_file = "/Users/yuhaomao/Downloads/ml-1m/users.dat"
usr_info, max_usr_id = get_usr_info(usr_file)
print("user numbers:", len(usr_info))
print("max user ID:", max_usr_id)
print("first user info：", usr_info['1'])

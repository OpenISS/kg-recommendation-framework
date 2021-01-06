import numpy as np

data_path = "../../../data/"


def load_ratings_final(dataset):
    print('loading RATING_FINAL file ...')
    rating_final_path = data_path + dataset + '/ratings_final'
    rating_file = open(rating_final_path + '.txt', encoding="UTF-8")

    # user_set = set()
    item_set = set()
    for row in rating_file:
        user_id = row.split("\t")[0]
        item_id = row.split("\t")[4]
        # if user_id not in user_set:
        #     user_set.add(user_id)
        if item_id not in item_set:
            item_set.add(item_id)

    # user_number = len(user_set)
    item_number = len(item_set)

    train_data, eval_data, test_data = dataset_split(rating_final_path)

    return item_number, train_data, eval_data, test_data

def dataset_split(rating_final_path):
    # train:eval:test = 6:2:2
    print('splitting dataset ...')
    rating_final_np = np.loadtxt(rating_final_path + '.txt', dtype=np.int32)

    eval_ratio = 0.2
    test_ratio = 0.2
    ratings_number = rating_final_np.shape[0]

    current_ratings_number = range(ratings_number)
    eval_id = np.random.choice(list(current_ratings_number), size=int(ratings_number * eval_ratio), replace=False)
    current_ratings_number = set(range(ratings_number)) - set(eval_id)
    test_id = np.random.choice(list(current_ratings_number), size=int(ratings_number * test_ratio), replace=False)
    train_id = list(current_ratings_number - set(test_id))

    train_data = rating_final_np[train_id]
    eval_data = rating_final_np[eval_id]
    test_data = rating_final_np[test_id]

    return train_data, eval_data, test_data

def load_kg_final(dataset):
    print('loading KG_FINAL file ...')

    # reading kg file
    kg_final_file = data_path + dataset + '/kg_final'

    kg = np.loadtxt(kg_final_file + '.txt', dtype=np.int32)
    
    head_set = set(kg[:, 0])
    tail_set = set(kg[:, 2])
    relation_set = set(kg[:, 1])
    
    entity_number = len(head_set | tail_set)
    relation_number = len(relation_set)

    return entity_number, relation_number, kg


def load_user_infos(dataset):
    print('loading users.dat file ...')
    
    # reading users_info_final file
    users_final_path = data_path + dataset + '/users'
    user_file = open(users_final_path + '.dat', encoding="UTF-8")
    
    user_set = set()
    user_gender_set = set()
    user_age_set = set()
    use_job_set = set()
    
    for row in user_file:
        user_id = row.split("::")[0]
        user_gender = row.split("::")[1]
        user_age = row.split("::")[2]
        user_job = row.split("::")[3]
        
        if user_id not in user_set:
            user_set.add(user_id)
        if user_gender not in user_gender_set:
            user_gender_set.add(user_gender)
        if user_age not in user_age_set:
            user_age_set.add(user_age)
        if user_job not in use_job_set:
            use_job_set.add(user_job)
            
            
    user_numbers = len(user_set)
    user_gender_numbers = len(user_gender_set)
    user_age_numbers = len(user_age_set)
    user_job_numbers = len(use_job_set)

    return user_numbers, user_gender_numbers, user_age_numbers, user_job_numbers

        
def get_usr_info(dataset):
    # convert m/f to num，M-0， F-1
    def gender2num(gender):
        return 1 if gender == 'F' else 0
    user_info_path = data_path + dataset + '/users.dat'
    with open(user_info_path, 'r') as f:
        data = f.readlines()

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
    
    return use_info

def load_datas(args):
    
    user_number, user_gender_number, user_age_number, user_job_number = load_user_infos(args.dataset)
    
    item_number, train_data, eval_data, test_data = load_ratings_final(args.dataset)

    entity_number, relation_number, kg = load_kg_final(args.dataset)

    print("n_user")
    print(user_number)
    print(item_number)
    print(entity_number)
    print(relation_number)
    print(user_number, user_gender_number, user_age_number, user_job_number)
    return user_number, item_number, entity_number, relation_number, train_data, eval_data, test_data, kg, \
           user_gender_number, user_age_number, user_job_number

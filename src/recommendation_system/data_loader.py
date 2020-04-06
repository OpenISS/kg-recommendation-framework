import numpy as np

data_path = "../../data/"


def load_ratings_final(dataset):
    print('loading RATING_FINAL file ...')
    rating_final_path = data_path + dataset + '/ratings_final'
    rating_file = open(rating_final_path + '.txt', encoding="UTF-8")

    user_set = set()
    item_set = set()
    for row in rating_file:
        user_id = row.split("\t")[0]
        item_id = row.split("\t")[1]
        if user_id not in user_set:
            user_set.add(user_id)
        if item_id not in item_set:
            item_set.add(item_id)

    user_number = len(user_set)
    item_number = len(item_set)

    train_data, eval_data, test_data = dataset_split(rating_final_path)

    return user_number, item_number, train_data, eval_data, test_data

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


def load_datas(args):
    user_number, item_number, train_data, eval_data, test_data = load_ratings_final(args.dataset)

    entity_number, relation_number, kg = load_kg_final(args.dataset)

    return user_number, item_number, entity_number, relation_number, train_data, eval_data, test_data, kg

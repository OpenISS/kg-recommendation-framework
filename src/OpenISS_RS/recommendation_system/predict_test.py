import tensorflow as tf
import argparse
import os
import linecache
import datetime
import matplotlib.pyplot as plt

signature_key = "crt_scores"

def pre_scores(user_num,item_num):
    with tf.Session() as sess:
        meta_graph_def = tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING],
                                                    'model/' + DATASET + '/result/' + restore_path)
        signature = meta_graph_def.signature_def

        user_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_id"].name)
        item_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["item_id"].name)
        head_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["head_id"].name)
        user_age= sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_age"].name)
        user_gender = sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_gender"].name)
        user_job = sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_job"].name)
        is_dropout = sess.graph.get_tensor_by_name(signature[signature_key].inputs["is_dropout"].name)
        
        # user_age= sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_age"].name)

        pred_all = sess.graph.get_tensor_by_name(signature[signature_key].outputs["ctr_predict"].name)
        
        if user_num > 6040:
            user_num = 1
        user_id_data = [user_num]
        if item_num > 3883:
            item_num = 1
        item_id_data = head_id_data = [item_num]
        
        user_gender_data,user_age_data,user_job_data = get_user_infos(user_num)
        
        pre_score = sess.run([pred_all],
                             feed_dict={user_id: user_id_data,
                                        item_id: item_id_data,
                                        head_id: head_id_data,
                                        user_age: user_age_data,
                                        user_gender: user_gender_data,
                                        user_job: user_job_data,
                                        is_dropout: 0.0})[0]
        neg_item_index = list(zip(item_id_data, pre_score))
        print(pre_score)

        # print(neg_item_index)

def get_user_infos(user_id):
    theline = linecache.getline("../../data/movie/users_info_final.txt", user_id+1)
    infos = theline.split("\t")
    user_gender = [infos[1]]
    user_age = [infos[2]]
    user_job = [infos[3]]
    print(user_gender)
    print(type(user_gender))
    return user_gender,user_age,user_job
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dateset', type=str, default='movie', help='which dataset to preprocess')
    parser.add_argument('-result', type=str, default='result', help='model pd result path')
    parser.add_argument('-userid', type=int, default='100', help='which userid to preprocess')
    parser.add_argument('-movieid', type=int, default='100', help='which movieid to preprocess')

    args = parser.parse_args()
    DATASET = args.dateset
    # a = 0
    try:
        restore_path = max(os.listdir('model/' + DATASET + '/' + args.result))
    except:
        restore_path = None

    # begin = datetime.datetime.now()
    # print("begin time:",begin)
    pre_scores(args.userid,args.movieid)
    # end = datetime.datetime.now()
    # print("end time:",end)
    # a += ((end - begin).microseconds) # 29522
    # print(a)
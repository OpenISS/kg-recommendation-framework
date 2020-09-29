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
    return user_gender,user_age,user_job
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='movie', help='which dataset to preprocess')
    parser.add_argument('-result', '--result', type=str, default='result', help='model pd result path')
    parser.add_argument('-userid', type=int, default='100', help='which userid to preprocess')
    parser.add_argument('-movieid', type=int, default='100', help='which movieid to preprocess')

    args = parser.parse_args()
    DATASET = args.d
    a = 0
    try:
        restore_path = max(os.listdir('model/' + DATASET + '/' + args.result))
    except:
        restore_path = None
    for i in range(10):
        print(i)
        begin = datetime.datetime.now()
        print("begin time:",begin)
        pre_scores(args.userid,args.movieid)
        end = datetime.datetime.now()
        print("end time:",end)
        a += ((end - begin).microseconds) # 29522
    print(a)
    # a = [51.376, 86.281, 115.724, 151.608, 189.612, 226.363, 264.416, 297.671, 340.28, 375.505, 403.269, 447.551, 488.515,
    #  517.058, 546.436, 576.319, 608.231, 648.432, 692.271, 715.918, 764.781, 793.893, 828.72, 850.837, 899.278, 918.221,
    #  931.577, 961.427, 999.198, 27.97, 84.358, 113.675, 139.69, 191.435, 232.756, 264.241, 305.628, 320.764, 371.054,
    #  407.141, 454.024, 487.473, 483.215, 533.715, 563.676, 603.143, 635.772, 658.275, 662.939, 766.428, 778.5, 824.23,
    #  812.188, 936.287, 913.496, 895.634, 945.124, 7.106, 12.059, 59.473, 118.709, 133.863, 181.658, 207.763, 245.047,
    #  274.543, 365.753, 383.117, 387.031, 449.777, 450.174, 527.701, 558.042, 577.306, 564.886, 592.722, 599.835,
    #  704.716, 715.423, 758.088, 798.895, 794.553, 861.475, 866.397, 961.056, 932.136, 970.81, 58.933, 95.437, 84.609,
    #  101.569, 171.24, 184.855, 235.345, 217.068, 270.076, 268.686, 399.141, 362.604, 425.908]
    # y = []
    # for i in range(1,101):
    #     y.append(i)
    # plt.plot(y, a, color="r", linestyle="--", marker="*", linewidth=1.0)
    #
    # plt.show()
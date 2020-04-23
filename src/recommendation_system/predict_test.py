import tensorflow as tf
import argparse
import os

signature_key = "crt_scores"

def pre_scores(user_num,item_num):
    with tf.Session() as sess:
        meta_graph_def = tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING],
                                                    'model/' + DATASET + '/result/' + restore_path)
        signature = meta_graph_def.signature_def

        user_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_id"].name)
        item_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["item_id"].name)
        head_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["head_id"].name)
        is_dropout = sess.graph.get_tensor_by_name(signature[signature_key].inputs["is_dropout"].name)

        pred_all = sess.graph.get_tensor_by_name(signature[signature_key].outputs["ctr_predict"].name)

        user_id_data = [user_num]
        item_id_data = head_id_data = [item_num]

        pre_score = sess.run([pred_all],
                             feed_dict={user_id: user_id_data,
                                        item_id: item_id_data,
                                        head_id: head_id_data,
                                        is_dropout: 0.0})[0]
        neg_item_index = list(zip(item_id_data, pre_score))
        print(pre_score)

        # print(neg_item_index)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='movie', help='which dataset to preprocess')
    parser.add_argument('-result', '--result', type=str, default='result', help='model pd result path')
    parser.add_argument('-userid', type=int, default='100', help='which userid to preprocess')
    parser.add_argument('-movieid', type=int, default='100', help='which movieid to preprocess')


    args = parser.parse_args()
    DATASET = args.d

    try:
        restore_path = max(os.listdir('model/' + DATASET + '/' + args.result))
    except:
        restore_path = None

    pre_scores(args.userid,args.movieid)
import tensorflow as tf
from tensorflow.contrib import slim
import numpy as np
import os
import time
from model import MKR

def mkdir(path):
    folder = os.path.exists(path)
    
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        # open(filename, 'a')
        print("---  new folder...  ---")
    
    else:
        print("---  There is this folder!  ---")

     
def train(args, data, show_loss, show_topk):
    
    var_to_restore = ["user_emb_matrix", "item_emb_matrix", "relation_emb_matrix", "entity_emb_matrix"]
    user_number, item_number, entity_number, relation_number = data[0], data[1], data[2], data[3]
    train_data, eval_data, test_data, kg = data[4], data[5], data[6], data[7]

    train_record = get_user_record(train_data, True)
    test_record = get_user_record(test_data, False)
    
    train_user_set = set(train_record.keys())
    test_user_set = set(test_record.keys())
    
    user_list = list(train_user_set & test_user_set)
    
    user_limit = 100
    k_list = [1, 2, 5, 10, 20, 50, 100]
    output_folder = int(time.time())
    
    if len(user_list) > user_limit:
        user_list = np.random.choice(user_list, size=user_limit, replace=False)
    
    item_set = set(list(range(item_number)))
    
    try:
        # Load the latest model
        restore_path = max(os.listdir('model/' + args.dataset + '/' + args.restore))
    except:
        restore_path = None

    model = MKR(args, user_number, item_number, entity_number, relation_number, restore_path)
    
    with tf.Session() as sess:
        if restore_path is None:
            sess.run(tf.global_variables_initializer())
        else:
            sess.run(tf.global_variables_initializer())
            user_emb = np.loadtxt('model/' + args.dataset + '/vocab/user_emb_matrix.txt', dtype=np.float32)
            item_emb = np.loadtxt('model/' + args.dataset + '/vocab/item_emb_matrix.txt', dtype=np.float32)
            entity_emb = np.loadtxt('model/' + args.dataset + '/vocab/entity_emb_matrix.txt', dtype=np.float32)
            relation_emb = np.loadtxt('model/' + args.dataset + '/vocab/relation_emb_matrix.txt', dtype=np.float32)
    
            user_emb = np.vstack([user_emb, np.random.normal(size=[user_number - len(user_emb), args.dim])])
            item_emb = np.vstack([item_emb, np.random.normal(size=[item_number - len(item_emb), args.dim])])
            entity_emb = np.vstack([entity_emb, np.random.normal(size=[entity_number - len(entity_emb), args.dim])])
            relation_emb = np.vstack([relation_emb, np.random.normal(size=[relation_number - len(relation_emb), args.dim])])
    
            var_to_restore = slim.get_variables_to_restore(exclude=var_to_restore)
            saver = tf.train.Saver(var_to_restore)
            saver.restore(sess,
                          tf.train.latest_checkpoint('model/' + args.dataset + '/' + args.restore + '/' + restore_path))
            model.init_embeding(sess, {model.user_emb: user_emb,
                                       model.item_emb: item_emb,
                                       model.entity_emb: entity_emb,
                                       model.relation_emb: relation_emb})
        
        for step in range(args.n_epochs):
            # RS training
            np.random.shuffle(train_data)
            start = 0
            while start < train_data.shape[0]:
                _, loss = model.train_rs(sess, get_feed_dict_for_rs(model, train_data, start, start + args.batch_size))
                start += args.batch_size
                if show_loss:
                    print(loss)

            # KGE training
            if step % args.kge_interval == 0:
                np.random.shuffle(kg)
                start = 0
                while start < kg.shape[0]:
                    _, rmse = model.train_kge(sess, get_feed_dict_for_kge(model, kg, start, start + args.batch_size))
                    start += args.batch_size
                    if show_loss:
                        print(rmse)

            # CTR evaluation
            train_auc, train_acc = model.eval(sess, get_feed_dict_for_rs(model, train_data, 0, train_data.shape[0]))
            eval_auc, eval_acc = model.eval(sess, get_feed_dict_for_rs(model, eval_data, 0, eval_data.shape[0]))
            test_auc, test_acc = model.eval(sess, get_feed_dict_for_rs(model, test_data, 0, test_data.shape[0]))

            print(
                'epoch %d    train auc: %.4f  acc: %.4f    eval auc: %.4f  acc: %.4f     test auc: %.4f  acc: %.4f'
                % (step, train_auc, train_acc, eval_auc, eval_acc, test_auc, test_acc))

            # top-K evaluation
            if show_topk:
                precision, recall, f1 = topk_eval(
                    sess, model, user_list, train_record, test_record, item_set, k_list)
                print('precision: ', end='')
                for i in precision:
                    print('%.4f\t' % i, end='')
                print()
                print('recall: ', end='')
                for i in recall:
                    print('%.4f\t' % i, end='')
                print()
                print('f1: ', end='')
                for i in f1:
                    print('%.4f\t' % i, end='')
                print('\n')

        # save embedding
        file = 'model/' + args.dataset + '/vocab/'
        mkdir(file)

        np.savetxt('model/' + args.dataset + '/vocab/user_emb_matrix.txt', model.user_emb_matrix.eval())
        np.savetxt('model/' + args.dataset + '/vocab/item_emb_matrix.txt', model.item_emb_matrix.eval())
        np.savetxt('model/' + args.dataset + '/vocab/entity_emb_matrix.txt', model.entity_emb_matrix.eval())
        np.savetxt('model/' + args.dataset + '/vocab/relation_emb_matrix.txt', model.relation_emb_matrix.eval())

        # Model save recovery save/restore method
        saver = tf.train.Saver()
        wts_name = 'model/' + args.dataset + '/restore' + "/{}/mkr.ckpt".format(output_folder)
        ckpt_path = 'model/' + args.dataset + '/restore/' + str(output_folder) + "/"
        mkdir(ckpt_path)
        saver.save(sess, wts_name)

        # save .pd ,deploy with tensorFlow Serving
        inputs = {"user_id": model.user_indices,
                  "item_id": model.item_indices,
                  "head_id": model.head_indices,
                  "is_dropout": model.dropout_param}

        outputs = {"ctr_predict": model.scores_normalized}

        export_path = 'model/' + args.dataset + '/result'
        signature = tf.saved_model.signature_def_utils.predict_signature_def(
            inputs=inputs, outputs=outputs)

        export_path = os.path.join(
            tf.compat.as_bytes(export_path),
            tf.compat.as_bytes(str(output_folder)))
        builder = tf.saved_model.builder.SavedModelBuilder(export_path)
        legacy_init_op = tf.group(tf.tables_initializer(), name='legacy_init_op')
        builder.add_meta_graph_and_variables(
            sess=sess,
            tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'crt_scores': signature,
            },
            legacy_init_op=legacy_init_op)
        builder.save()
            
            

def get_feed_dict_for_rs(model, data, start, end, dropout=0.5):
    feed_dict = {model.user_indices: data[start:end, 0],
                 model.item_indices: data[start:end, 1],
                 model.labels: data[start:end, 2],
                 model.head_indices: data[start:end, 1],
                 model.dropout_param: dropout
                 }

    return feed_dict

def get_feed_dict_for_kge(model, kg, start, end, dropout=0.5):
    feed_dict = {model.item_indices: kg[start:end, 0],
                 model.head_indices: kg[start:end, 0],
                 model.relation_indices: kg[start:end, 1],
                 model.tail_indices: kg[start:end, 2],
                 model.dropout_param: dropout}
    return feed_dict

def topk_eval(sess, model, user_list, train_record, test_record, item_set, k_list):
    precision_list = {k: [] for k in k_list}
    recall_list = {k: [] for k in k_list}

    for user in user_list:
        test_item_list = list(item_set - train_record[user])
        item_score_map = dict()
        items, scores = model.get_scores(sess, {model.user_indices: [user] * len(test_item_list),
                                                model.item_indices: test_item_list,
                                                model.head_indices: test_item_list,
                                                model.dropout_param: 0.5})
        for item, score in zip(items, scores):
            item_score_map[item] = score
        item_score_pair_sorted = sorted(item_score_map.items(), key=lambda x: x[1], reverse=True)
        item_sorted = [i[0] for i in item_score_pair_sorted]

        for k in k_list:
            hit_num = len(set(item_sorted[:k]) & test_record[user])
            precision_list[k].append(hit_num / k)
            recall_list[k].append(hit_num / len(test_record[user]))

    precision = [np.mean(precision_list[k]) for k in k_list]
    recall = [np.mean(recall_list[k]) for k in k_list]
    f1 = [2 / (1 / precision[i] + 1 / recall[i]) for i in range(len(k_list))]

    return precision, recall, f1


def get_user_record(datas, train_label):
    
    user_history_dict = dict()
    for data in datas:
        user, item, label = data[0], data[1], data[2]

        if train_label or label == 1:
            if user not in user_history_dict:
                user_history_dict[user] = set()
            user_history_dict[user].add(item)

    return user_history_dict
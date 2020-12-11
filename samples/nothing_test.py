# import pandas as pd
# import matplotlib.pyplot as plt
# from lenskit.datasets import ML1M, MovieLens
# from lenskit.algorithms import basic, item_knn, user_knn, als, funksvd
# from lenskit.crossfold import partition_users, SampleFrac
# from lenskit.batch import MultiEval
# from lenskit.topn import RecListAnalysis, ndcg as NDCG
#
# EVAL_FOLDER = 'algos-eval'
#
# def eval_algorithms(dataset, algorithms):
#     eval = MultiEval(EVAL_FOLDER, recommend=50)
#     eval.add_datasets(dataset, name='Dataset-To-Eval')
#     eval.add_algorithms(algorithms)
#     eval.run()
#
# def display_runs():
#     runs = pd.read_csv(EVAL_FOLDER + '/runs.csv')
#     runs.set_index('RunId', inplace=True)
#     print('Algorithms runs table head:')
#     print(runs.head())
#     return runs
#
# def display_recommendations():
#     recs = pd.read_parquet(EVAL_FOLDER + '/recommendations.parquet')
#     print('Recommendations table head:')
#     print(recs.head())
#     return recs
#
# def check_recommendations(runs, recs, test):
#     rla = RecListAnalysis()
#     rla.add_metric(NDCG)
#     ndcg = rla.compute(recs, test)
#     print('Normalized Discounted Cumulative Gains table head:')
#     print(ndcg.head())
#     ndcg = ndcg.join(runs[['AlgoClass']], on='RunId')
#     return ndcg.groupby(['AlgoClass'])['ndcg'].mean()
#
# def plot_comparison(algorithm_means):
#     plt.bar(x=algorithm_means.index.values, height=list(algorithm_means))
#     plt.ylabel('NDCG mean')
#     plt.show()
#
# def test_alogrithms():
#     # data = MovieLens('ml-latest-small')
#     data = ML1M('ml-1m')
#     ratings = data.ratings
#     print('Initial ratings table head:')
#     print(ratings.head())
#     algorithms = [
#         basic.Bias(damping=5),
#         basic.Popular(),
#         item_knn.ItemItem(20),
#         user_knn.UserUser(20),
#         als.BiasedMF(50),
#         als.ImplicitMF(50),
#         funksvd.FunkSVD(50)
#     ]
#     pairs = list(partition_users(
#         ratings[['user', 'item', 'rating']], 5, SampleFrac(0.2)))
#     eval_algorithms(dataset=pairs, algorithms=algorithms)
#     runs = display_runs()
#     recs = display_recommendations()
#     truth = pd.concat((p.test for p in pairs), ignore_index=True)
#     ndcg_means = check_recommendations(runs, recs, truth)
#     print('NDCG means:')
#     print(ndcg_means)
#     plot_comparison(ndcg_means)
#
# if __name__ == '__main__':
#     test_alogrithms()
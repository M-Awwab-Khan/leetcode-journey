import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # x = scores.sort_values('score', ascending=False).score.values
    # prev = None
    # ind = 0
    # ids = []
    # for i in range(len(x)):
    #     if x[i] == prev:
    #         ids.append(ind)
    #     else:
    #         prev = x[i]
    #         ind += 1
    #         ids.append(ind)
    # return pd.DataFrame({'score': x, 'rank': ids})

    # Use the rank method to assign ranks to the scores in descending order with no gaps
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Drop id column & Sort the DataFrame by score in descending order
    result_df = scores.drop('id',axis=1).sort_values(by='score', ascending=False)
    
    return result_df

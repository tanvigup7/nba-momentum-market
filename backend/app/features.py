import pandas as pd

def compute_features(df, lookback=3):
    """
    Simple rolling features for momentum modeling.
    - recent_net_points: sum(points scored - opponent points) over last `lookback` possessions
    - score_margin: current score difference
    """
    df = df.copy()
    df['recent_net_points'] = 0
    for i in range(len(df)):
        start = max(0, i - lookback)
        df.loc[i, 'recent_net_points'] = (
            (df.loc[start:i, 'score'] - df.loc[start:i, 'opponent_score']).sum()
        )
    df['score_margin'] = df['score'] - df['opponent_score']
    return df

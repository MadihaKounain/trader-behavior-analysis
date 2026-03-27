import pandas as pd

def load_and_clean_data(trader_path, sentiment_path):
    # Load data
    trader_df = pd.read_csv(trader_path)
    sentiment_df = pd.read_csv(sentiment_path)

    # Clean column names
    trader_df.columns = trader_df.columns.str.strip().str.lower().str.replace(" ", "_")
    sentiment_df.columns = sentiment_df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Convert time
    trader_df['timestamp_ist'] = pd.to_datetime(trader_df['timestamp_ist'], errors='coerce')
    trader_df['date'] = trader_df['timestamp_ist'].dt.date

    sentiment_df['date'] = pd.to_datetime(sentiment_df['date'], errors='coerce')
    sentiment_df['date'] = sentiment_df['date'].dt.date

    # Drop null dates
    trader_df = trader_df.dropna(subset=['date'])
    sentiment_df = sentiment_df.dropna(subset=['date'])

    # Merge
    merged_df = pd.merge(trader_df, sentiment_df, on='date', how='inner')

    return merged_df
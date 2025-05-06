import json
from utils import Agent
from datetime import datetime, timedelta

def main():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
    except Exception as e:
        print(f"Error reading config.json: {e}")
        return

    agent = Agent(config)
    print("Agent initialized successfully.")
    print("\n")
    # print(config)
    today = datetime.today()
    start_date = today - timedelta(days=config['num_days'])
    end_date = today

    # agent.get_news(start_date, end_date)
    # agent.get_stock_data(start_date, end_date)
    # price = agent.predict(start_date, end_date)
    # print(f"Predicted price for {config['ticker']} on {start_date.strftime('%Y-%m-%d')}: {price}")
    agent.plotting(start_date, end_date)


if __name__ == '__main__':
    main()


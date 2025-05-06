Here's the raw markdown for the updated `README.md`:


# Financial Stock Prediction Using Generative AI

**Author**: Ethan Kaley  
**Course**: EGR 404 – Generative AI Tools  
**University**: University of Rhode Island

## Overview

This project explores the application of generative AI for predicting stock price movements by integrating financial data and news headlines. Utilizing OpenAI's language models, the system aims to provide insights into stock trends based on recent news and historical financial data.

## Features

- **Data Integration**: Combines historical stock data from Yahoo Finance with current news headlines from NewsAPI.
- **Generative AI Predictions**: Employs OpenAI's language models to generate stock price predictions.
- **Performance Metrics**: Calculates model accuracy using MSE, RMSE, MAE, R², and NDEI.
- **Visualization**: Visual comparison of predicted vs actual stock prices using Matplotlib.

## Technologies Used

- **Programming Language**: Python
- **APIs**:
  - [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)
  - [NewsAPI](https://newsapi.org)
  - [yFinance](https://github.com/ranaroussi/yfinance)
- **Libraries**:
  - NumPy
  - Matplotlib

## How to Run This Code

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/ekaley/egr404-project.git
cd egr404-project
```

### 2. Set Up a Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `config.json` File

Create a file named `config.json` in the project root with the following template:

```json
{
    "news_api_key": "YOUR_NEWSAPI_KEY_HERE",
    "ticker": "TICKER_SYMBOL",
    "num_days": 29,
    "openai_api_key": "YOUR_OPENAI_API_KEY_HERE"
}
```

- You can generate your News API key at [https://newsapi.org](https://newsapi.org).
- `ticker` should be a valid stock symbol (e.g., `MSFT`, `AAPL`) as seen on [Yahoo Finance](https://finance.yahoo.com).
- `num_days` should be between **1 and 29** to stay within the free tier limit of the NewsAPI.

### 5. Run the Script
```bash
python main.py
```

The script will:
- Pull stock price data and news headlines,
- Query the OpenAI API for predictions,
- Output prediction results and evaluation metrics,
- Display a plot comparing actual and predicted stock prices.

## Challenges Encountered

- **API Rate Limiting**: VPNs were used to avoid rate limiting issues with Yahoo Finance during development.
- **Non-numerical API Responses**: The OpenAI API often returned disclaimers or non-numeric outputs. Extra parsing logic was implemented to retry requests as needed.
- **NewsAPI Free Tier**: The API only allows access to news from the last 30 days, limiting historical analysis.

## Future Improvements

- Implement response chaining with OpenAI for multi-turn reasoning.
- Add OpenAI function calling to structure responses more effectively.
- Support more flexible data sources beyond the free tier limitations.
- Expand forecasting to multi-day predictions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

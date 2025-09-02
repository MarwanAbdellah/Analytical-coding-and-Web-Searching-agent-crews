```markdown
# Stock Price Analysis - 2025

## Introduction

This report analyzes the stock price performance of several companies in 2025. The data reflects the percentage change in stock prices from January to December.

## Data

The following data represents the percentage increase in stock prices for the year 2025:

*   AAPL: 12.49%
*   MSFT: 9.64%
*   AMZN: 19.45%
*   TSLA: 11.87%
*   GOOGL: 17.53%

## Code

```python
"""
Stock Price Analysis - 2025

This script analyzes the stock price performance of several companies in 2025.
It calculates and displays the percentage change in stock prices.
"""

class Stock:
    """
    Represents a stock with its ticker symbol and percentage change in price.
    """
    def __init__(self, ticker, percentage_change):
        """
        Initializes a Stock object.

        Args:
            ticker (str): The stock's ticker symbol (e.g., "AAPL").
            percentage_change (float): The percentage change in price.
        """
        self.ticker = ticker
        self.percentage_change = percentage_change

    def __repr__(self):
        """
        Returns a string representation of the Stock object.
        """
        return f"{self.ticker}: {self.percentage_change:.2f}%"

def analyze_stock_performance(stocks):
    """
    Analyzes the stock performance and identifies top performers.

    Args:
        stocks (list of Stock): A list of Stock objects.

    Returns:
        tuple: A tuple containing:
            - A list of Stock objects sorted by percentage change (descending).
            - The top performing stock.
    """
    # Sort stocks by percentage change in descending order
    sorted_stocks = sorted(stocks, key=lambda stock: stock.percentage_change, reverse=True)

    # Identify the top performer
    top_performer = sorted_stocks[0] if sorted_stocks else None

    return sorted_stocks, top_performer

def main():
    """
    Main function to execute the stock price analysis.
    """
    # Define stock data
    stocks = [
        Stock("AAPL", 12.49),
        Stock("MSFT", 9.64),
        Stock("AMZN", 19.45),
        Stock("TSLA", 11.87),
        Stock("GOOGL", 17.53),
    ]

    # Analyze stock performance
    sorted_stocks, top_performer = analyze_stock_performance(stocks)

    # Print the results
    print("Stock Performance in 2025:")
    for stock in sorted_stocks:
        print(f"- {stock}")

    if top_performer:
        print(f"\nTop Performing Stock: {top_performer.ticker} ({top_performer.percentage_change:.2f}%)")
    else:
        print("\nNo stock data available.")

if __name__ == "__main__":
    main()
```

## Data Analysis Findings

The code analyzes the provided stock data and presents the percentage change for each company. It also identifies the top-performing stock.

## Company-Specific Information

*   **AAPL (Apple):** Increased by approximately 12.49%.
*   **MSFT (Microsoft):** Increased by approximately 9.64%.
*   **AMZN (Amazon):** Increased by approximately 19.45%, showing strong growth.
*   **TSLA (Tesla):** Increased by approximately 11.87%.
*   **GOOGL (Google):** Increased by approximately 17.53%, demonstrating significant growth.

## Conclusion

AMZN and GOOGL experienced the most significant growth in 2025, based on the provided data. The code provides a clear and organized way to analyze and present this information.
```
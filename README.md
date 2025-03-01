# NSE_Stock_Tracker
Simple NSE stock tracker where a certain stock prices can be hit from the NSE website and we can get the data in our Datasheet. 

# NSE Stock Data Fetcher

This script fetches real-time stock data from the National Stock Exchange (NSE) for specified stock symbols, processes the data, and saves it to an Excel file.

## Features
- Fetches stock data from the NSE website
- Extracts relevant information such as last price, change, percent change, open, high, low, etc.
- Saves data to an Excel file (`stock_data.xlsx`), appending new data to existing records
- Uses session-based requests to handle NSE API cookies
- Implements delays to avoid rate limiting

## Prerequisites
Ensure you have Python installed on your system along with the required dependencies.

### Required Libraries:
Install dependencies using:
```bash
pip install requests pandas openpyxl
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nse-stock-fetcher.git
   cd nse-stock-fetcher
   ```

2. Run the script:
   ```bash
   python stock_fetcher.py
   ```

3. The script will fetch stock data for predefined stock symbols (`RELIANCE`, `TCS`, `INFY`, `HDFCBANK`, `TATAMOTORS`) and save it in `stock_data.xlsx`.

## Configuration
- To modify the list of stock symbols, update the `symbols` list in the `main()` function.
- You can change the output filename by modifying the `filename` variable in the `save_to_excel` function.

## File Structure
```
|-- stock_fetcher.py   # Main script for fetching and saving data
|-- stock_data.xlsx    # Output file (created after running the script)
|-- README.md          # Documentation
```

## Notes
- This script is dependent on NSE's API, which may change in the future. If the API structure is updated, modifications might be required.
- Ensure you have a stable internet connection to fetch data reliably.
- If the script fails due to an HTTP 403 error, try running it after some time, as NSE imposes rate limits.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



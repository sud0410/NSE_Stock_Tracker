#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
import time
from datetime import datetime
import os

def fetch_nse_stock_data(symbol):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.nseindia.com/'
    }
    
    session = requests.Session()
    session.get('https://www.nseindia.com/', headers=headers)
    
    time.sleep(1)
    
    quote_url = f'https://www.nseindia.com/api/quote-equity?symbol={symbol}'
    response = session.get(quote_url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}. Status code: {response.status_code}")
        return None

def process_stock_data(stock_data):
    
    if not stock_data:
        return None
    
    # kindly add volume if required by : 'volume': stock_data.get('securityWiseDP', {}).get('quantityTraded')
    processed_data = {
        'symbol': stock_data.get('info', {}).get('symbol'),
        'company_name': stock_data.get('info', {}).get('companyName'),
        'last_price': stock_data.get('priceInfo', {}).get('lastPrice'),
        'change': stock_data.get('priceInfo', {}).get('change'),
        'percent_change': stock_data.get('priceInfo', {}).get('pChange'),
        'open': stock_data.get('priceInfo', {}).get('open'),
        'high': stock_data.get('priceInfo', {}).get('intraDayHighLow', {}).get('max'),
        'low': stock_data.get('priceInfo', {}).get('intraDayHighLow', {}).get('min'),
        'date': datetime.now().strftime('%d-%m-%Y'),
        'time': datetime.now().strftime('%H:%M:%S'),
    }
    
    return processed_data

def save_to_excel(data_list, filename='stock_data.xlsx'):
    df = pd.DataFrame(data_list)
    
    
    if os.path.exists(filename):
        
        existing_df = pd.read_excel(filename)
        
        df = pd.concat([existing_df, df], ignore_index=True)
    
    # save as excel
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    
    symbols = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'TATAMOTORS']
    
    
    filename = 'stock_data.xlsx'
    
    stock_data_list = []
    
    # get stock symbol
    for symbol in symbols:
        print(f"Fetching data for {symbol}...")
        raw_data = fetch_nse_stock_data(symbol)
        processed_data = process_stock_data(raw_data)
        
        if processed_data:
            stock_data_list.append(processed_data)
            print(f"Data fetched for {symbol}")
        
        time.sleep(2)
    
    
    if stock_data_list:
        save_to_excel(stock_data_list, filename)
    else:
        print("No data to save")

if __name__ == "__main__":
    main()


# In[ ]:





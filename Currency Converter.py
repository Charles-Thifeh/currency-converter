import requests

def main():
    api_key = "989546699ab34ced88998dedc3e059f1"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

    exchangeRates = getExchangeRates(url)

    while True:
        getAvailableCurrencies(exchangeRates)
        

        fromCurrency = input("Enter the base currency: ").upper()
        toCurrency = input("Enter the target currency: ").upper()

        amount = float(input("Enter the amount to convert: "))

        convertCurrencies(exchangeRates, fromCurrency, toCurrency, amount)

        print("Do you want to convert another?")
        if not input('>>> ').lower().startswith('y'):
            break
    print('Thanks for using the application')
        

    

def getExchangeRates(url):
    response = requests.get(url)
    data = response.json()

    exchange_rates = data["rates"]

    return exchange_rates

def getAvailableCurrencies(exchangeRates):
    available_currencies = ""
    for currency in exchangeRates.keys():
        available_currencies += currency + ", "

    # Remove the trailing comma and space
    available_currencies = available_currencies[:-2] 

    print("Available currencies: " + available_currencies)

def convertCurrencies(exchangeRates, fromCurrency, toCurrency, amount):
    original_amount = amount / exchangeRates[fromCurrency]
    converted_amount = original_amount * exchangeRates[toCurrency]

    print(f"{amount} {fromCurrency} = {converted_amount} {toCurrency}")

if __name__ == "__main__":
    main()
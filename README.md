# CryptoDataCollector

## Description
CryptoDataCollector is a Python-based project that collects historical OHLC (Open, High, Low, Close) data for various cryptocurrencies using the CoinGecko API. The data is processed and stored in a pandas DataFrame for further analysis or reporting.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd CryptoDataCollector
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the `CryptoDataCollector.py` script to fetch and process cryptocurrency data:
```bash
python CryptoDataCollector.py
```

## Configuration
- Ensure you have an API key from CoinGecko and set it in your environment variables as `API_KEY`.
- Modify the `criptos` list in `CryptoDataCollector.py` to change the cryptocurrencies you want to track.

## API Reference
This project uses the CoinGecko API to fetch cryptocurrency data. More details can be found at [CoinGecko API Documentation](https://www.coingecko.com/en/api).

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact Information
For any inquiries or issues, please contact the project maintainer at [marcospslaine@gmail.com].

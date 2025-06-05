# Stock Analysis Dashboard with Local Vision Model

A **Streamlit** application for technical stock analysis, combining interactive visual indicators with AI-driven interpretation powered by a locally hosted vision model.

---

## Features

- **Historical Stock Data**  
  Fetches data directly from Yahoo Finance using [yfinance](https://github.com/ranaroussi/yfinance).

- **Interactive Technical Indicators**
  - Candlestick charts (via Plotly)
  - 20-Day Exponential Moving Average (EMA)
  - 20-Day Bollinger Bands

- **AI-Powered Chart Interpretation**
  - Captures the rendered chart as an image
  - Sends the image to a locally running [Ollama 3.2](https://ollama.com/) vision model
  - Receives a **Buy/Hold/Sell** recommendation and textual explanation

- **User-Friendly**
  - Select stock symbol and date range
  - Toggle technical indicators
  - Instantly view both chart and model analysis

---

## Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (UI)
- [Plotly](https://plotly.com/python/) (Charting)
- [yfinance](https://github.com/ranaroussi/yfinance) (Data)
- [ollama](https://ollama.com/) (Vision Model API)
- Temporary image generation and base64 encoding

---

## How It Works

1. **Select Stock & Range**  
   Choose a stock symbol and date range in the Streamlit UI.
   ![WhatsApp Image 2025-06-05 at 8 53 59 PM (1)](https://github.com/user-attachments/assets/196886a1-2d91-41df-bc74-9669b26aaeaf)


3. **Visualize Data**  
   The app fetches relevant historical data and displays an interactive candlestick chart. Optionally overlay 20-Day EMA and Bollinger Bands.

   ![WhatsApp Image 2025-06-05 at 8 55 15 PM](https://github.com/user-attachments/assets/50c11bd2-455d-4811-81a1-b30f44d10611)


5. **Model Analysis**  
   The chart is captured and encoded, then sent to the locally running Ollama vision model.  
   A prompt-based interaction asks the model for a trade recommendation based solely on the visual chart.

6. **Get Recommendation**  
   The model returns a **buy/hold/sell** suggestion and an explanation, shown alongside the chart.

   
![WhatsApp Image 2025-06-05 at 9 01 19 PM](https://github.com/user-attachments/assets/a25f24e1-42b7-4342-a98b-ea33cfbef089)

---

## Setup & Usage

### Requirements

- Python 3.8+
- Streamlit
- yfinance
- plotly
- ollama (with vision model, e.g., Ollama 3.2)

### Installation

```bash
# Clone this repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the App

1. **Start the Ollama Model**  
   Ensure Ollama is running locally and the vision model is loaded (e.g., `ollama run <vision-model-name>`).

2. **Launch Streamlit App**  
   ```bash
   streamlit run app.py
   ```

3. **Open in Browser**  
   Go to `http://localhost:8501` (or Streamlit's provided URL).

---

## Customization

- **Vision Model**: You can swap the vision model as needed, provided it is compatible with Ollama's API.
- **Indicators**: Add or remove technical indicators in the code as desired.

---

## Security & Privacy

- All AI analysis is performed **locally**; no images or chart data are sent to external servers.
- The app does not store or log user data.

---

## Disclaimer

This project is for educational and informational purposes only. It does **not** constitute financial advice. Use at your own risk.

---

## License

[MIT License](LICENSE)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [Ollama](https://ollama.com/)


# Unauthorized Sales Detector

## Description

This Flask application provides a REST API endpoint to detect unauthorized sales transactions. It processes POST requests containing product listings (including product ID and authorized seller ID) and actual sales transactions (including product ID and seller ID), identifying any transactions made by unauthorized sellers.

## Setup Instructions

### Prerequisites

- Python 
- Flask

### How To Run

1. Install Flask using pip install Flask.

2. Start the Flask application:
   ```
   python app.py
   ```
   This will run the server on `http://localhost:5000`.

3. Test the Endpoint

To test the `/detect_unauthorized_sales` endpoint, you can use the `curl` command with a JSON file containing example request data.(`data.json`)

### Sending a Request with `curl`

Use the following `curl` command to send the request:

```
curl -X POST http://localhost:5000/detect_unauthorized_sales \
-H "Content-Type: application/json" \
-d @data.json
```

This command sends the contents of `data.json` to the application, which then returns a response indicating any unauthorized sales transactions detected.

The API responds with a JSON object containing unauthorized sales transactions, formatted as follows:

```json
{
  "unauthorizedSales": [
    {"productID": "123", "unauthorizedSellerID": ["B2"]},A
  ]
}
```

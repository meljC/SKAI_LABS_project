
# Unauthorized Sales Detector

## Description

This Flask application provides a REST API endpoint to detect unauthorized sales transactions. It processes POST requests containing product listings (including product ID and authorized seller ID) and actual sales transactions (including product ID and seller ID), identifying any transactions made by unauthorized sellers.

## Setup Instructions

### Prerequisites

- Python 
- Flask

### Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```
2. Navigate into the repository's directory:
   ```
   cd unauthorized-sales-detector
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```
   This will run the server on `http://localhost:5000`.

## Testing the Endpoint

To test the `/detect_unauthorized_sales` endpoint, you can use the `curl` command with a JSON file containing example request data.

### Example Request Data (`data.json`)

Save the following JSON data to a file named `data.json`:

```json
{
  "productListings": [
    {"productID": "123", "authorizedSellerID": "A1"},
    {"productID": "124", "authorizedSellerID": "A2"},
    ...
  ],
  "salesTransactions": [
    {"productID": "123", "sellerID": "B2"},
    {"productID": "124", "sellerID": "A2"},
    ...
  ]
}
```

Replace `...` with additional product listings and sales transactions as needed.

### Sending a Request with `curl`

Use the following `curl` command to send the request:

```
curl -X POST http://localhost:5000/detect_unauthorized_sales \
-H "Content-Type: application/json" \
-d @data.json
```

This command sends the contents of `data.json` to the application, which then returns a response indicating any unauthorized sales transactions detected.

## Response Format

The API responds with a JSON object containing unauthorized sales transactions, formatted as follows:

```json
{
  "unauthorizedSales": [
    {"productID": "123", "unauthorizedSellerID": ["B2"]},
    ...
  ]
}
```

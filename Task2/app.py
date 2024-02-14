from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_unauthorized_sales', methods=['POST'])
def detect_unauthorized_sales():
    # Ensure the request contains JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.json
    productListings = data.get('productListings', [])
    salesTransactions = data.get('salesTransactions', [])
    
    # Check for required keys in the JSON data
    if not all(key in data for key in ['productListings', 'salesTransactions']):
        return jsonify({"error": "Missing productListings or salesTransactions in JSON data"}), 400
    
    unauthorized_sales = find_unauthorized_sales(productListings, salesTransactions)
    
    return jsonify({"unauthorizedSales": unauthorized_sales}), 200

def find_unauthorized_sales(productListings, salesTransactions):
    authorized_sellers = {listing['productID']: listing['authorizedSellerID'] for listing in productListings}
    unauthorized_sales = []

    for transaction in salesTransactions:
        productID = transaction['productID']
        sellerID = transaction['sellerID']
        if productID in authorized_sellers and authorized_sellers[productID] != sellerID:
            unauthorized_sales.append({"productID": productID, "unauthorizedSellerID": [sellerID]})

    return unauthorized_sales

if __name__ == '__main__':
    app.run(debug=True)

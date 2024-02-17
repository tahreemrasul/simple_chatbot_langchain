from flask import Flask, jsonify
from data_store import menu, special_offers, customer_reviews, customizations

app = Flask(__name__)


@app.route('/menu', methods=['GET'])
def get_menu():
    """
    Retrieves the menu data.

    Returns:
        A tuple containing the menu data as JSON and the HTTP status code.
    """
    return jsonify(menu), 200


@app.route('/special-offers', methods=['GET'])
def get_special_offers():
    """
    Retrieves the special offers data.

    Returns:
        A tuple containing the special offers data as JSON and the HTTP status code.
    """
    return jsonify(special_offers), 200


@app.route('/customer-reviews', methods=['GET'])
def get_customer_reviews():
    """
    Retrieves customer reviews data.

    Returns:
        A tuple containing the customer reviews data as JSON and the HTTP status code.
    """
    return jsonify(customer_reviews), 200


@app.route('/customizations', methods=['GET'])
def get_customizations():
    """
    Retrieves the customizations data.

    Returns:
        A tuple containing the customizations data as JSON and the HTTP status code.
    """
    return jsonify(customizations), 200


if __name__ == '__main__':
    app.run(debug=True)

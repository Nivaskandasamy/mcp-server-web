from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    try:
        # Get JSON data from the request
        data = request.get_json()
        num1 = data.get('num1')
        num2 = data.get('num2')

        # Validate input
        if num1 is None or num2 is None:
            return jsonify({'error': 'Both num1 and num2 are required'}), 400
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return jsonify({'error': 'num1 and num2 must be numbers'}), 400

        # Calculate sum
        result = num1 + num2
        return jsonify({'sum': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
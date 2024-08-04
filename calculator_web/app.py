from flask import Flask, request, jsonify, send_from_directory
import math

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        expression = data.get('expression', '')

        # Substitua 'sqrt(' por 'math.sqrt('
        expression = expression.replace('sqrt(', 'math.sqrt(')

        # Avalie a expressão e retorne o resultado
        result = eval(expression)
        
        if isinstance(result, (int, float)):
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Invalid result'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

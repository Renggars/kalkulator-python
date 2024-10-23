# src/app.py
from flask import Flask, render_template, request, jsonify # type: ignore
import math

app = Flask(__name__)

# Kelas abstrak untuk kalkulator
class AbstractCalculator:
    def calculate(self):
        pass

# Kelas dasar kalkulator
class Calculator(AbstractCalculator):
    def __init__(self, operand1, operand2=None):
        self.operand1 = operand1
        self.operand2 = operand2

    def calculate(self, operation):
        if operation == 'add':
            return self.operand1 + self.operand2
        elif operation == 'subtract':
            return self.operand1 - self.operand2
        elif operation == 'multiply':
            return self.operand1 * self.operand2
        elif operation == 'divide':
            return self.operand1 / self.operand2

# Kelas kalkulator scientific dengan polymorphism dan inheritance
class ScientificCalculator(Calculator):
    def calculate(self, operation):
        if operation == 'sin':
            return math.sin(self.operand1)
        elif operation == 'cos':
            return math.cos(self.operand1)
        elif operation == 'tan':
            return math.tan(self.operand1)
        elif operation == 'log':
            return math.log(self.operand1)
        elif operation == 'pow':
            return math.pow(self.operand1, self.operand2)
        else:
            return super().calculate(operation)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    operation = request.form.get('operation')
    operands = request.form.getlist('operands[]')
    operands = [float(op) for op in operands]

    # Menggunakan kalkulator scientific jika operasinya scientific
    calculator = ScientificCalculator(operands[0], operands[1] if len(operands) > 1 else None)
    result = calculator.calculate(operation)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

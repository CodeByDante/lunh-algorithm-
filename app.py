from flask import Flask, render_template, request

app = Flask(__name__)

# Función para verificar el algoritmo de Luhn
def luhn_verifier(card_number):
    total = 0
    reverse_digits = card_number[::-1]

    for i, digit in enumerate(reverse_digits):
        num = int(digit)
        if i % 2 == 1:  # Doble cada segundo dígito
            num *= 2
            if num > 9:  # Si el resultado es mayor que 9, resta 9
                num -= 9
        total += num
    
    return total % 10 == 0

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        card_number = request.form['card_number']
        if card_number.isdigit():
            is_valid = luhn_verifier(card_number)
            result = "Válida" if is_valid else "Inválida"
        else:
            result = "Por favor, ingresa solo números."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import os

app = Flask(__name__)

def verificar_luhn(numero_tarjeta):
    total = 0
    reverso = numero_tarjeta[::-1]
    for i, digito in enumerate(reverso):
        n = int(digito)
        if i % 2 == 1:  # Duplicar cada segundo dígito
            n *= 2
            if n > 9:  # Si el resultado es mayor que 9, restar 9
                n -= 9
        total += n
    return total % 10 == 0

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ''
    if request.method == 'POST':
        numero = request.form['numero']
        if verificar_luhn(numero):
            resultado = 'Tarjeta válida'
        else:
            resultado = 'Tarjeta inválida'
    return render_template('index.html', resultado=resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

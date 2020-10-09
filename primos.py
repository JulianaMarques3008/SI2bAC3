import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    fim = 100
    p = 0
    numero=3
    primos = "2, "

    while p < fim:
        primo = 1
        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
                break
        if (primo):
            primos = primos + str(numero)+','
            p += 1
            if (p % 10 == 0):
                primos = primos + "\n"
        numero += 1
    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


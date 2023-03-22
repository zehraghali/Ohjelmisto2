from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    """Tarkistaa, onko annettu luku alkuluku."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:n>')
def check_prime(n):
    """Palauttaa True, jos annettu luku on alkuluku, muuten False."""
    result = {"Number": n, "isPrime": is_prime(n)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=3000)

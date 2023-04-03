from flask import Flask, Reponse
import json

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def on_alkuluku(luku):
    luku = int(luku)
    alkuluku = True

    for i in range(2, luku, 1):
        if luku & i == 0:
            alkuluku = False
            break

    vastaus = {
        "Number": luku,
        "isPrime": alkuluku

    }

    jsonvast = json.dumps(vastaus)
    return Reponse (reponse=jsonvast, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"

    }
    jsonvast = json.dumps(vastaus)
    return Reponse(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)




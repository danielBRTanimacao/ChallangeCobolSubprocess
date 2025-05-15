from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.post("/api/deposit")
def deposit_value():
    data = request.get_json()

    if data and "deposit" in data: 
        subprocess.run(["cd ./subprocess && cobc -x backUrubu.cob"])
        # enviar para o backUrubu
        return jsonify({"message": f"Valor foi depositado R${data["deposit"]:.2f}"})

    return jsonify({"error": "Não foi possivel depositar o valor!"})

if __name__ == "__main__":
    app.run(debug=True)
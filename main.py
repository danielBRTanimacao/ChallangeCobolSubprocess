from flask import Flask, request, jsonify
import subprocess
from pathlib import Path

app = Flask(__name__)

@app.post("/api/deposit")
def deposit_value():
    data = request.get_json()

    if data and "deposit" in data: 
        try:
            float(data["deposit"])
            days = int(data["days"]) if "days" in data else 30
            if days < 0 or days > 30:
                return jsonify({"error": "O número de dias deve ser entre 0 e 30."}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Valores inválidos!"}), 400
        
        deposit_args = [str(data["deposit"]), str(days)]
        
        try:
            COBOL_DIR = Path(__file__).resolve().parent / "subprocess"

            compile_result = subprocess.run(
                ["cobc", "-x", "backUrubu.cob"],
                cwd=COBOL_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if compile_result.returncode != 0:
                return jsonify({
                    "erro": "Erro ao compilar o COBOL",
                    "detail": compile_result.stderr.strip()
                }), 500
            
            response_result = subprocess.run(
                ["./backUrubu", *deposit_args],
                cwd=COBOL_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if response_result.returncode != 0:
                return jsonify({
                    "erro": "Erro ao executar o COBOL",
                    "detail": response_result.stderr.strip()
                }), 500
            
            response_final = float(response_result.stdout.strip())

            return jsonify({
                "message": f"Após {days} dias, o valor que você vai receber é R${response_final:.2f}"
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Não foi possível processar os dados!"}), 400

if __name__ == "__main__":
    app.run(debug=True)

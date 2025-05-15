from flask import Flask, request, jsonify
import subprocess
from pathlib import Path

app = Flask(__name__)

@app.post("/api/deposit")
def deposit_value():
    data = request.get_json()

    if data and "deposit" in data and "days" in data: 
        try:
            float(data["deposit"])
            int(data["days"])
        except (ValueError, TypeError) as e:
            return jsonify({"error": "Valores invalidos!"})
        deposit = [str(data["deposit"]), str(data["days"])]
        
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
                return jsonify(
                    {   
                        "erro": "Erro ao compilar o COBOL",
                        "detail": compile_result.stderr.strip()
                    }
                ), 500
            
            response_result = subprocess.run(
                ["./backUrubu", *deposit],
                cwd=COBOL_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if response_result.returncode != 0:
                return jsonify(
                    {   
                        "erro": "Erro ao executr o COBOL",
                        "detail": compile_result.stderr.strip()
                    }
                ), 500
            
            response_final = float(response_result.stdout.strip())

            return jsonify({
                "message": f"Apos {data['days']} dias, o valor que você vai receber é R${response_final:.2f}"
            })
        except TypeError as e:
            return jsonify({"error": e})

    return jsonify({"error": "Não foi possivel depositar o valor!"})

if __name__ == "__main__":
    app.run(debug=True)
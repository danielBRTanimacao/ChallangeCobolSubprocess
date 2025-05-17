from flask import Flask, request, jsonify
import subprocess
from pathlib import Path

from utils.validators import result_validation

app = Flask(__name__)

@app.post("/api/deposit")
def deposit_value():
    CPF_TEST_VALIDATED: str = "39601449035"

    data = request.get_json()

    if data and "deposit" in data and "cpf" in data: 
        try:
            float(data["deposit"])
            days = int(data["days"]) if "days" in data else 30
            if days < 0 or days > 30:
                return jsonify({"error": "O número de dias deve ser entre 0 e 30."}), 400
            
            cpf_formated: str = data["cpf"].strip().replace(".","").replace("-","")
            if not cpf_formated.isnumeric():
                raise ValueError
            
        except (ValueError, TypeError):
            return jsonify({"error": "Valores inválidos!"}), 400
        
        deposit_args = [str(data["deposit"]), str(days), cpf_formated]
        
        try:
            COBOL_DIR = Path(__file__).resolve().parent / "subprocess"

            compile_result = subprocess.run(
                ["cobc", "-x", "backUrubu.cob"],
                cwd=COBOL_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            result_validation(compile_result, "Erro ao compilar o COBOL")
            
            response_result = subprocess.run(
                ["./backUrubu", *deposit_args],
                cwd=COBOL_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            result_validation(response_result, "Erro ao executar o COBOL")
            
            if response_result.stdout.strip() == "true":
                return jsonify({
                "error": f"Usuario CPF: {data["cpf"]} invalido!"
            })
            
            response_final = float(response_result.stdout.strip())
            

            return jsonify({
                "message": f"Usuario CPF: {data["cpf"]} após {days} dias, o valor que você vai receber é R${round(response_final):.2f}"
            })
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Não foi possível processar os dados!"}), 400

if __name__ == "__main__":
    app.run(debug=True)

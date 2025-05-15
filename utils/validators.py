from subprocess import CompletedProcess
from flask import Response, jsonify

def result_validation(process: CompletedProcess[str], name_error: str) -> Response:
    if process.returncode != 0:
        return jsonify({
            "erro": name_error,
            "detail": process.stderr.strip()
        }), 500
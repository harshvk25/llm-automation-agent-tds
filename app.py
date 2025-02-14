from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_task():
    task_description = request.args.get('task', '')
    if not task_description:
        return jsonify({'error': 'Task description is missing'}), 400

    try:
        result = execute_task(task_description)
        return jsonify({'status': 'success', 'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/read', methods=['GET'])
def read_file():
    file_path = request.args.get('path', '')
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404

    with open(file_path, 'r') as f:
        content = f.read()

    return jsonify({'status': 'success', 'content': content}), 200

def execute_task(task_description):
    
    return f"Executing task: {task_description}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


# app.py
from flask import Flask, render_template, request, jsonify
import subprocess
import os
import yaml

app = Flask(__name__)

PLAYBOOK_DIR = os.path.join(os.getcwd(), "playbooks")
INVENTORY_FILE = os.path.join(os.getcwd(), "inventory.yml")

TASKS = {
    "create_user": {
        "playbook": "create_user.yml",
        "params": ["username", "uid", "home", "shell", "create_home"],
    },
    "delete_user": {
        "playbook": "delete_user.yml",
        "params": ["username"],
    },
}

@app.route("/")
def index():
    return render_template("index.html", tasks=TASKS)

@app.route("/task/<task_name>")
def task_form(task_name):
    if task_name not in TASKS:
        return jsonify({"error": "Invalid task"}), 400
    return render_template("task_form.html", task_name=task_name, params=TASKS[task_name]["params"])

@app.route("/execute", methods=["POST"])
def execute_task():
    task_name = request.form.get("task_name")
    if task_name not in TASKS:
        return jsonify({"error": "Invalid task"}), 400

    params = {key: request.form.get(key) for key in TASKS[task_name]["params"]}
    for param, value in params.items():
        if not value and param != "create_home":
            return jsonify({"error": f"Missing parameter: {param}"}), 400

    extra_vars = params.copy()
    if task_name == "create_user":
        extra_vars["create_home"] = params.get("create_home", "yes")

    vars_file = "temp_vars.yml"
    with open(vars_file, "w") as f:
        yaml.dump(extra_vars, f)

    playbook_path = os.path.join(PLAYBOOK_DIR, TASKS[task_name]["playbook"])
    cmd = ["ansible-playbook", "-i", INVENTORY_FILE, playbook_path, "--extra-vars", f"@{vars_file}"]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = result.stdout + result.stderr
        os.remove(vars_file)
        return jsonify({"status": "success", "output": output})
    except subprocess.CalledProcessError as e:
        output = e.stdout + e.stderr
        if os.path.exists(vars_file):
            os.remove(vars_file)
        return jsonify({"status": "error", "output": output}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

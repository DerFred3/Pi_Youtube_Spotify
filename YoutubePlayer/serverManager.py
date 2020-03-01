from flask import Flask, render_template, request, redirect
import queueManager
class ServerManager:
    app = Flask(__name__)

    # def __init__(self):
        # self.app = Flask(__name__)
        # self.qManager = queueManager.QueueManager(queueManager.QueueManager.dbPath)

    def start(self):
        self.app.run(host="0.0.0.0")

    @app.route("/")        
    def index():
        return render_template("index.html")

    @app.route('/submit', methods=["POST"])
    def onSubmit():
        url = str(request.form.get("input_url"))
        queueManager.QueueManager(queueManager.QueueManager.dbPath).add(url)
        return redirect("/")
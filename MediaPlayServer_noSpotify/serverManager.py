from flask import Flask, render_template, request, redirect
import queueManager, inputCheck, flags
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
    
    @app.route("/admin")
    def admin():
        return render_template("admin.html")

    @app.route('/submit', methods=["POST"])
    def onSubmit():
        spotify_uri = ''
        youtube_url = str(request.form.get('youtube_url'))
        ctx_media = str(request.form.get('ctx_media'))
        ctx_button = str(request.form.get('ctx_button'))

        if not spotify_uri == '':
            url = str(spotify_uri)
            ctx = flags.ctx_spotify
        else:
            url = str(youtube_url)
            ctx = flags.ctx_youtube
        
        if ctx_button == 'submit_normal':
            queueManager.QueueManager(queueManager.QueueManager.dbPath).add(url, ctx)
        elif ctx_button == 'submit_firstQ':
            queueManager.QueueManager(queueManager.QueueManager.dbPath).addFirst(url, ctx)
            flags.doSkip = True
        
        return redirect("/")
    
    # Checken, ob es sich um einen Youtube oder Spotify Link handelt
    @app.route('/checkInput', methods=['POST'])
    def checkInput():
        spotify_uri = ''
        youtube_url = str(request.form.get('youtube_url'))
        _return = {'success': '', 'error': '', 'ctx_media': ''}

        if (not spotify_uri == '' and youtube_url == '') or (spotify_uri == '' and not youtube_url == ''):
            if inputCheck.checkSpotifyYoutube(spotify_uri) or inputCheck.checkSpotifyYoutube(youtube_url):
                _return['success'] = True

                if spotify_uri == '':
                    _return['ctx_media'] = flags.ctx_youtube
                else:
                    _return['ctx_media'] = flags.ctx_spotify
            else:
                _return['success'] = False
                _return['error'] = 'Eingabe war nicht korrekt! Bitte Eingabe prüfen'
        elif spotify_uri == '' and youtube_url == '':
            _return['success'] = False
            _return['error'] = 'Es muss mindestens ein Feld gefüllt werden'
        elif not spotify_uri == '' and not youtube_url == '':
            _return['success'] = False
            _return['error'] = 'Es darf nur ein Feld gefüllt werden'
        else:
            _return['success'] = False
            _return['error'] = 'Unbekannter Fehler bitte dem Benutzerservice bescheid geben ;)'
        
        if queueManager.QueueManager(queueManager.QueueManager.dbPath).getQueueLength() >= flags.max_queue_length:
            _return['success'] = False
            _return['error'] += '\nDie Maximale Queue-Länge von ' + flags.max_queue_length + ' darf nicht überschritten werden'

        return _return
    
    # Admin Optionen übernehmen
    @app.route('/adminOptions', methods=['POST'])
    def setAdminOptions():
        ctx_button = str(request.form.get('ctx_button'))
        
        if ctx_button == 'skip':
            flags.doSkip = True
        elif ctx_button == 'playpause':
            if flags.doPause != True:
                flags.doPause = True
            else:
                flags.doPause = False
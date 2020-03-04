import threading, serverManager, playerManager, queueManager, flags

threads = []
sm = serverManager.ServerManager()
pm = playerManager.PlayerManager()
qm = queueManager.QueueManager(queueManager.QueueManager.dbPath)
qm.resetQueue()

# Thread registieren, auf dem der Server läuft
serverThread = threading.Thread(target=sm.start)
threads.append(serverThread)

# Thread registieren, auf dem die Queue ausgelesen und abgespielt wird
playerThread = threading.Thread(target=pm.start)
threads.append(playerThread)

# Threads starten
serverThread.start()
playerThread.start()


# Auf Input über die Konsole warten
while True:
    _input = input()
    if _input == "skip":
        flags.setPause(False)
        flags.setSkip(True)
    if _input == "pause":
        flags.setPause(True)
    if _input == "resume":
        flags.setPause(False)
    

# TO-DOs
# * best/worst Video Qualität, je nach Flag (+ Änderung während Laufzeit)
#
# * Exception Handling
# * Framework für Website Handling

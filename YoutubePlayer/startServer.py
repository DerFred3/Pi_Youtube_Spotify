import threading, serverManager, playerManager, queueManager, flags

threads = []
sm = serverManager.ServerManager()
pm = playerManager.PlayerManager()
qm = queueManager.QueueManager(queueManager.QueueManager.dbPath)
qm.resetQueue()

# register the thread on which the server is running
serverThread = threading.Thread(target=sm.start)
threads.append(serverThread)

# register the thread on which the queue gets read and played
playerThread = threading.Thread(target=pm.start)
threads.append(playerThread)

# start the threads
serverThread.start()
playerThread.start()

# wait for user input
while True:
    _input = input()
    if _input == "skip":
        flags.setPause(False)
        flags.setSkip(True)
    if _input == "pause":
        flags.setPause(True)
    if _input == "resume":
        flags.setPause(False)
    

# max queue length

# proper exception handling

# proper framework for website handling

# best/worst quality decision
# - solution via only (best) audio
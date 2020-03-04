# Konstanten
ctx_spotify = 'spotify'
ctx_youtube = 'youtube'
max_queue_length = 30

# Flags
doSkip = False
doPause = False
appCtx = ctx_spotify

def setSkip(_bool):
    global doSkip
    doSkip = _bool

def setPause(_bool):
    global doPause
    doPause = _bool

def setContext(_context):
    global appCtx
    appCtx = _context
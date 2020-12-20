# whitelisted log lines that are mirrored to a discord channel: 

allowed_phrases = [
    # player chat
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:\s<.*>.*',
    # player joined game
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:.*joined\sthe\sgame.*',
    # player left game
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:.*left\sthe\sgame.*',
    # player completed challenge
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:.*has\scompleted\sthe\schallenge.*',
    # server starting
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:\sStarting\sminecraft\sserver\sversion.*',
    # server startup Done
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:\sDone(\d*.\d*)!\sFor\shelp,\stype\s"help".*',
]

allowed_phrases_combined = "(" + ")|(".join(allowed_phrases) + ")"

# this file was originally a blacklist:

excluded_phrases = [
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/WARN\]:\sCan\'t\skeep\sup!\sIs\sthe\sserver\soverloaded\?',
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:\s.*lost\sconnection:\sDisconnected',
    '\[\d\d:\d\d:\d*]\s\[Server\sthread/INFO\]:\s.*logged\sin\swith\sentity\sid\s\d*\sat.*',
    '\[\d\d:\d\d:\d*]\s\[User\sAuthenticator\s#\d*/INFO\]:\sUUID\sof\splayer\s.*is.*'
]
excluded_phrases_combined = "(" + ")|(".join(excluded_phrases) + ")"
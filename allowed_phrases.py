# whitelisted log lines that are mirrored to a discord channel: 

allowed_phrases = [
    # player chat
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:\s<.*>.*',
    # player joined game
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:.*joined\sthe\sgame.*',
    # player left game
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:.*left\sthe\sgame.*',
    # player completed challenge
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:.*has\scompleted\sthe\schallenge.*',
    # server starting
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:\sStarting\sminecraft\sserver\sversion.*',
    # server startup Done
    '\[\d\d:\d\d:\d*]\s\[Server\sthread\/INFO\]:\sDone\s\(\d*.\d*s\)!\sFor\shelp,\stype\s"help".*',
]

allowed_phrases_combined = "(" + ")|(".join(allowed_phrases) + ")"

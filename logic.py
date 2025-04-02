# All mud commands must have the syntax [command](user, options)
# ALL COMMANDS MUST RETURN A STRING
def fail(failee, input):
    return f"The input from {failee} failed:\n{input}"
def look(looker, lookee=None):
    if lookee:
        return f"You see a {lookee}"
    return "You look"
def say(sayer, phrase=None):
    if not phrase:
        return "Usage say <phrase> example: say Good, morning to you!"
    return f'{sayer} says, "{phrase}"'
def pose(poser, emote=None):
    if not emote:
        return "Usage pose <emote> example: pose strikes a pose!"
    return f'{poser} {emote}'
IMPLEMENTED = {
    "look":look,
    "say":say,
    "pose":pose,
}
def command_parse(input:str):
    user = "player" # Need to get the user here or pass it in.
    banana = input.split()
    command = banana[0]
    if command in IMPLEMENTED:
        if len(banana) == 1:
            parse = IMPLEMENTED[command](user)
        else: 
            parse = IMPLEMENTED[command](user, " ".join(banana[1:]))
    else:
        parse = fail(user, input)
    return parse

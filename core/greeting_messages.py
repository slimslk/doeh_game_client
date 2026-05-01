import random

GREETING_MESSAGES = [
    "You come to in silence. No memory follows you here. The world feels empty. Drained. Then your body reminds you. Hunger. It is already too late to ignore it.",
    "You awaken with no memory of who you are. The world around you feels distant… hollow. Then it comes. Hunger. Not a feeling — a command. You must eat. Or you will disappear.",
    "You wake without a past. Without a name. Something inside you is wrong. A void gnaws at your core. Hunger. It will not wait.",
    "There is no memory of arrival. No trace of what came before. Only this place. And the growing emptiness within you. Hunger. It demands to be answered.",
    "You open your eyes. The world does not recognize you. Your thoughts are scattered. Fading. But one remains, sharp and absolute. Hunger. Feed it. Or be consumed by it.",
    "You wake into something broken.No past. No meaning. Only a body already failing. Hunger tears through you. It is not a warning. It is a sentence.",
]


def get_greeting_message():
    return random.choice(GREETING_MESSAGES)

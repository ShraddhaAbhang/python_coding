import random

def sentence_generator():
    subject = ['The scientist','The astronaut','The engineer','The artist','The philosopher','Dogs','She','he','The big red bus','Swimming','To travel','What she said','Who','It','Those','Everybody']
    verbs = ['painting','walking','standing','running','created','found','bought', 'ate','built','wrote','brought','gave','showed','told','sent','baked']
    object = ['a new dress','the pizza','a sandcastle','a letter','a cup of coffee','a gift','the way','a secret','the package','cookies']
    preposition = ['on','under','in','toward','above','below','over','away','at','before', 'with','by','to','of']
    place = ['forest','desert','ocean','mountain','hotel','museum','home','stadium','villa','bedroom','swimmingpool','station','school','auditorium','hall','mall','theater']
    
    # Selecting random parts of the sentence
    chosen_subject = random.choice(subject)
    chosen_verb = random.choice(verbs)
    chosen_object = random.choice(object)
    chosen_preposition = random.choice(preposition)
    chosen_place = random.choice(place)
    
    # Constructing the sentence
    sentence = f"{chosen_subject} {chosen_verb} {chosen_object} {chosen_preposition} {chosen_place}."
    
    return sentence

# Example usage:
print(sentence_generator())

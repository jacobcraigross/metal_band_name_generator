import random

first_name = [
    'Poison', 'Blackened', 'Bestial', 'Ruptured', 'Nuclear', 'Wolflike', 'Wretched',
    'Punished', 'Hooded', 'Howling', 'Clandestine', 'Noxious', 'Infernal', 'Slaughtered'
]

last_name = [
    'Rites', 'Vengeance', 'Revenge', 'Tragedy', 'Scythe', 'Butchery', 'Contempt', 'Darkness',
    'Annihilation', 'Throne', 'Hellfire', 'Suffering', 'Pestilence', 'Genocide', 'Strife'
]

name_one = random.choice(first_name)
name_two = random.choice(last_name)

master_name = name_one + ' ' + name_two

print master_name

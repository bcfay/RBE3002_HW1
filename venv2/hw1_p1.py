
def alphabetize(list):
    if(len(list) > 0):
        list.sort()
        return list

pantheon = ["Notus", "Momus", "Nereus", "Glaucus", "Heracles", "Eurus", "Aether", "Phosphorus", "Zelus", "Tartarus"]
print(pantheon)
print(alphabetize(pantheon))
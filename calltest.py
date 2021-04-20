class Pokemon():
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name,level = 5):
        self.name = name
        self.level = level
        self.weak = "Normal"
        self.strong = "Normal"
	
    def opponent(self):
	if(self.p_type == 'Grass'):
		self.weak = 'Fire'
		self.strong = 'water'
		return (self.weak,self.strong)
   	
	if(self.p_type == 'Ghost'):
            self.weak = 'Dark'
            self.strong = 'Psychic'
            return (self.weak,self.strong)
        
        if(self.p_type == 'Fire'):
            self.weak = 'Water'
            self.strong = 'Grass'
            return (self.weak,self.strong)
        
        if(self.p_type == 'Flying'):
            self.weak = 'Electric'
            self.strong = 'Fighting'
            return (self.weak,self.strong)


    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

class Grass_Pokemon(Pokemon):
    p_type = "Grass"

    def opponent(self):
	Pokemon.opponent(self)
	print(self.weak,self.strong)

    
class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"
    def opponent(self):
	Pokemon.opponent(self)
	print(self.weak,self.strong)

   
class Fire_Pokemon(Pokemon):
    p_type = "Fire"
    def opponent(self):
	Pokemon.opponent(self)
	print(self.weak,self.strong)

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    def opponent(self):
	Pokemon.opponent(self)
	print(self.weak,self.strong)	

gras = Grass_Pokemon("Grass")
gras.opponent()

ghost = Ghost_Pokemon('Ghost')
ghost.opponent()

fire = Fire_Pokemon('Fire')
fire.opponent()

fly = Flying_Pokemon('Flying')
fly.opponent()


new_monster = lambda name:Monster(name,["","","","","",""],"","0","","","")

class Monster:
   
   def __init__(self,name,stats,AC,HP,speed,features,attacks):
      self.name = name
      self.features = features
      self.AC = AC
      self.HP = HP
      self.speed = speed
      self.attacks = attacks
      if isinstance(stats,list):
         self.stats = stats
      else:
         self.stats = stats.split("$")
      
   def info_str(self):
      acm = "Monster name: "+self.name + "\nAC: " + self.AC + "\nINIT: "+self.stats[1]+"\nSpeed: "+self.speed+"\n"
      acm += "STR DEX CON INT WIS CHA\n"
      for s in self.stats:
         acm += s
         for i in range(4-len(s)):
            acm += " "
      acm += "\nFeatures\n" + self.features + "\nAttacks\n" + self.attacks + "\n"
      return acm
   
   def __str__(self):
      return str(self.name)
   
   def get_dir(self):
      d = {"name":self.name,
              "stats":Monster.encode_stats(self.stats),
              "AC":self.AC,
              "HP":self.HP,
              "speed":self.speed,
              "features":self.features,
              "attacks":self.attacks}
      return d
   
   def get_unencoded_dir(self):
      d = {"name":self.name,
              "stats":self.stats,
              "AC":self.AC,
              "HP":self.HP,
              "speed":self.speed,
              "features":self.features,
              "attacks":self.attacks}
      return d
   
   def encode_stats(s):
      acm = ""
      for stat in s:
         acm += stat + "$"
      return acm[:-1]
   


def input_int(prompt):
   while 1:
      try:
         return int(input(prompt))
      except:
         print("invalid input need a interger")

def input_multi_line(prompt):
   print(prompt)
   acm = ""
   while("\\e" not in acm):
      acm += input("") + "\n"
   return acm[:-3] + "\n"
   
class Monster_tools:
   
   def create_monster():
      name = input("Monster name: ")
      AC = input("AC: ")
      stats = []
      if(input("Input stats>?").lower()[0] == "y"):
         for prompt in ("STR","DEX","CON","INT","WIS","CHA"):
            stats.append(input(prompt+": "))
      else:
         stats = ["0","0","0","0","0","0"]
      HP = str(input_int("HP: "))
      speed = input("Speed: ")
      features = input_multi_line("features")
      attacks = input_multi_line("attacks")
      return Monster(name,stats,AC,HP,speed,features,attacks)  
   
mt = Monster_tools


      
from Monsters import *
class dude:
   
   def __init__(self,name,monster,HP = None):
      self.name = name
      self.monster = None
      if monster != None:
         self.monster = monster
         self.HP = int(monster.HP)
      else:
         self.monster = new_monster("")
         self.HP = int(HP)
      self.Working_hp = self.HP
         
   def __str__(self):
      acm = self.name + " HP: " + self.Working_hp
              
   def mod_hp(self,amount):
      self.Working_hp = amount
      
   def get_dir(self):
      return {"name":self.name,
              "monster_name":self.monster.name,
             "HP":str(self.HP)}
      
class encounter:
   
   def __init__(self,name,dudes):
      self.name = name
      self.dudes = dudes
      
   def __str__(self):
      return str(self.name)
         
   def add_dude(self,d):
      self.dudes.append(d)
      
   def remove_dude(self,index):
      try:
         self.dudes.pop(index)
      except IndexError:
         print(index,"not found in encounter")
   
   def get_dude(self,dude_num):
      if dude_num >= len(self.dudes):
         return None
      return self.dudes[dude_num]
   
   def search_dude(self,name):
      for d in dudes:
         if d.name == name:
            return d
      return None
   
   def get_dir(self):
      return {"name":self.name}
   
   def get_dudes(self): return self.dudes
   
   def get_dude_hp(self):
      acm = []
      for d in self.dudes:
         acm.append(d.name + " HP: " + str(d.Working_hp))
      return acm
   
   def get_dude_list(self):
      acm = []
      for d in self.dudes:
         acm.append(d.name)
      return acm
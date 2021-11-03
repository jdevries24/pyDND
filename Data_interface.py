import xml.etree.ElementTree as ET
from Monsters import *
from Encounters import *

build_monster = lambda md:Monster(md["name"],md["stats"],md["AC"],md["HP"],md["speed"],md["features"],md["attacks"])
class DND_DB:
   
   def __init__(self):
      self.monsters = []
      self.encounters = []
      
   def get_encounter_list(self):
      acm = []
      for e in self.encounters:
         acm.append(e.name)
      return acm
   
   def get_monster_list(self):
      acm = []
      for m in self.monsters:
         acm.append(m.name)
      return acm
   
   def get_monster(self,index):
      if index >= len(self.monsters):
         return None
      return self.monsters[index]
   
   def get_encounter(self,index):
      if index >= len(self.encounters):
         return None
      return self.encounters[index]
   
   def append_monster(self,monst):self.monsters.append(monst)

   def append_encounter(self,encount):self.encounters.append(encount)
      
   def remove_monster(self,index):
      try:
         self.monsters.pop(index)
      except IndexError:
         print(index,"is out of range")

   def remove_encounter(self,index):
      try:
         self.encounters.pop(index)
      except IndexError:
         print(index,"is out of range")
   
   def search_monsters(self,name):
      for i in range(len(self.monsters)):
         if str(self.monsters[i]) == name:
            return i
      return -1
   
   def search_encounters(self,name):
      for i in range(len(self.encounters)):
         if str(self.encounters[i]) == name:
            return i
      return -1
   
   def save_db(self,db_file):
      root = ET.Element("Data")
      for monst in self.monsters:
         ET.SubElement(root,"monster",monst.get_dir())
      for enc in self.encounters:
         encount = ET.Element("encounter",enc.get_dir())
         for dude in enc.get_dudes():
            ET.SubElement(encount,"dude",dude.get_dir())
         root.append(encount)
      t = ET.ElementTree(root)
      t.write(db_file)
   
   def load_db(self,db_file):
      t = ET.parse(db_file)
      root = t.getroot()
      for monst in root.iter("monster"):
         self.monsters.append(build_monster(monst.attrib))
      for enc in root.iter("encounter"):
         dudes = []
         for d in enc.iter("dude"):
            dudes.append(self.build_dude(d.attrib))
         self.encounters.append(encounter(enc.attrib["name"],dudes))

   def build_dude(self,d):
      if(d["monster_name"] == "EMPTY"):
         return dude(d["name"],None,d["HP"])
      monst_index = self.search_monsters(d["monster_name"])
      monst = self.get_monster(monst_index)
      if monst != None:
         return dude(d["name"],monst)
      print("Cannot find monster " + d["monster_name"] + "using empty monster")
      return dude(d["name"],None,0)
      

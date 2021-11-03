from Encounters import *
from Monster_Creator import *
from DATA_ENG import *

def get_selection(prompt):
   try:
      return input(prompt)[0].lower()
   except:
      return ""
   
def select_monster(DB):
   m = DB.get_monster(input_int("Monster number: "))
   if m != None:
      return m
   print("monster not found")
   return None

def select_encounter(DB):
   e = DB.get_encounter(input_int("Encounter number: "))
   if e != None:
      return e
   print("encounter not found")
   return None
   
def monster_menu(DB):
   select = ""
   while(select != "e"):
      print("0.list monsters\n1.add monster\n2.see monster\nr.remove monster\ne.exit")
      select = get_selection(">?")
      print("")
      if select == "0":
         print(DB.get_monster_list())
      elif select == "1":
         DB.append_monster(mt.create_monster())
         print("")
      elif select == "2":
         m = select_monster(DB)
         if m != None:
            print(m)
            print("")
      elif select == "r":
         index = input_int("monster number: ")
         DB.remove_monster(index)
         print("")

def encounter_menu(DB):
   select = ""
   while(select != "e"):
      print("0.list encounters\n1.add encounter\n2.edit encounter\n3.run encounter\nr.remove encounter\ne.exit")
      select = get_selection(">?")
      print("")
      if select == "0":
         print(DB.get_encounter_list())
      elif select == "1":
         DB.append_encounter(create_enocunter(DB))
         print("")
      elif select == "2":
         e = select_encounter(DB)
         if e != None:
            edit_encounter(e,DB)
         print("")
      elif select == "3":
         e = select_encounter(DB)
         if e != None:
            run_encounter(e)
         print("")
      elif select == "r":
         DB.remove_encounter(input_int("encounter number: "))
         print("")

def create_enocunter(DB):
   name = input("name: ")
   e = encounter(name,[])
   return e
   
def edit_encounter(encount,DB):
   select = ""
   while(select != "e"):
      print("0.list fighters")
      print("1.Add fighter")
      print("2.fighter detail")
      print("r.remove fighter")
      print("e.exit")
      select = get_selection(">?")
      print("")
      if select == "0":
         print(encount.list_dudes())
      elif select == "1":
         name = input("fighter name: ")
         gf = get_selection("use generic?")
         if (gf == "y"):
            HP = input_int("HP: ")
            encount.add_dude(dude(name,None,HP))
         else:
            print(DB.get_monster_list())
            m = select_monster(DB)
            if m != None:
               encount.add_dude(dude(name,m))
         print("")
      elif select == "r":
         encount.remove_dude(input_int("fighter number"))
         print("")
      elif select == "2":
         f = encount.get_dude(input_int("fighter number"))
         if f != None:
            print(f)
         print("")

def run_encounter(encount):
   select = ""
   while(select != "e"):
      print("0.list fighters")
      print("1.select fighter")
      print("e.exit")
      select = get_selection(">?")
      print("")
      if select == "0":
         print(encount.list_dudes())
      if select == "1":
         f = encount.get_dude(input_int("fighter number"))
         if f != None:
            print(f)
            f.mod_hp()
            
def main(Database_fname):
   DB = DND_DB()
   DB.load_db(Database_fname)
   select = ""
   try:
      while(select != "e"):
         print("0.monsters")
         print("1.encounters")
         print("e.exit")
         select = get_selection(">?")
         print("")
         if select == "0":
            monster_menu(DB)
         elif select == "1":
            encounter_menu(DB)
   except KeyboardInterrupt:
      pass
   DB.save_db(Database_fname)

main("DND_STUFF")
            
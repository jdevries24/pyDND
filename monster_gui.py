import tkinter as tk
from Monsters import *
from Encounters import *

class monster_gui(tk.Frame):
   
   def __init__(self,root,monst):
      #takes in a valid tkroot and monster class
      tk.Frame.__init__(self,master = root,bg = "white",pady = 10)
      self.monst = monst
      self.build_top_frame()
      self.build_stat_frame()
      self.build_bottom_frame()
      self.top_frame.grid(row = 0,sticky = tk.W)
      self.stat_frame.grid(row = 1,sticky = tk.W)
      self.bottom_frame.grid(row = 2,sticky = tk.W)
      self.update_monster(self.monst)
      
   def update_monster(self,new_monst):
      m = new_monst
      self.monster_name.delete('1.0',tk.END)
      self.monster_name.insert(tk.END,m.name)
      self.AC.delete('1.0',tk.END)
      self.AC.insert(tk.END,m.AC)
      self.HP.delete(0,tk.END)
      self.HP.insert(tk.END,m.HP)
      self.speed.delete('1.0',tk.END)
      self.speed.insert(tk.END,m.speed)
      self.attacks.delete('1.0',tk.END)
      self.attacks.insert(tk.END,m.attacks)
      self.features.delete('1.0',tk.END)
      self.features.insert(tk.END,m.features)
      for i in range(6):
         self.stat_vals[i].delete('1.0',tk.END)
         self.stat_vals[i].insert(tk.END,m.stats[i])
      self.monst = m
      
   def build_top_frame(self):
      self.top_frame = tk.Frame(self,bg = "white",padx = 5,pady = 10)
      self.monster_name_label = tk.Label(self.top_frame,bg = "white",justify = tk.LEFT,text = "Name: ")
      self.ac_label = tk.Label(self.top_frame,bg = "white",justify = tk.LEFT,text = "AC:")
      self.HP_label = tk.Label(self.top_frame,bg = "white",justify = tk.LEFT,text = "HP:")
      self.Speed_label = tk.Label(self.top_frame,bg = "white",justify = tk.LEFT,text = "Speed:")
      self.monster_name = tk.Text(self.top_frame,height = 1,width = 20)
      self.AC = tk.Text(self.top_frame,height = 1,width = 20)
      self.HP = tk.Spinbox(self.top_frame,from_ = 0,to_ = 999,increment = 1,width = 20)
      self.speed = tk.Text(self.top_frame,height = 1,width = 20)
      self.monster_name_label.grid(column = 0,row = 1,sticky = tk.W)
      self.ac_label.grid(column = 0,row = 2,sticky = tk.W)
      self.HP_label.grid(column = 0,row = 3,sticky = tk.W)
      self.Speed_label.grid(column = 0,row = 4,sticky = tk.W)
      self.monster_name.grid(column = 1,row = 1)
      self.AC.grid(column = 1,row = 2)
      self.HP.grid(column = 1,row = 3)
      self.speed.grid(column = 1,row = 4)

   def build_stat_frame(self):
      self.stat_frame = tk.Frame(self,bg = "white",padx = 5,pady = 10)
      self.stat_labels = []
      stats = ("STR","DEX","CON","INT","WIS","CHA")
      for i in range(6):
         new_label = tk.Label(self.stat_frame,bg = "white",text = stats[i],padx = 4)
         new_label.grid(column = i,row = 0)
         self.stat_labels.append(new_label)
      self.stat_vals = []
      for i in range(6):
         new_text = tk.Text(self.stat_frame,height = 1,width = 3)
         new_text.grid(column = i,row = 1)
         self.stat_vals.append(new_text)
         
   def build_bottom_frame(self):
      self.bottom_frame = tk.Frame(self,bg = "white",padx = 5,pady = 10)
      self.feature_label = tk.Label(self.bottom_frame,bg = "white",text = "featuers")
      self.attacks_label = tk.Label(self.bottom_frame,bg = "white",text = "attacks")
      self.features = tk.Text(self.bottom_frame,bg = "white",height = 10,width = 40)
      self.attacks = tk.Text(self.bottom_frame,bg = "white",height = 10,width = 40)
      self.feature_label.grid(row = 0,sticky = tk.W)
      self.features.grid(row = 1)
      self.attacks_label.grid(row = 2,sticky = tk.W)
      self.attacks.grid(row = 3)
   
   def save_monster(self):
      m = self.monst
      m.name = self.monster_name.get("1.0","1.end")
      m.AC = self.AC.get("1.0","1.end")
      m.HP = self.HP.get()
      m.speed = self.speed.get("1.0","1.end")
      m.features = self.features.get("1.0",tk.END)
      m.attacks = self.attacks.get("1.0",tk.END)
      for i in range(6):
         m.stats[i] = self.stat_vals[i].get("1.0","1.end")
         

class dude_gui(monster_gui):
   
   def __init__(self,root,guy):
      super().__init__(root,guy.monster)
      self.guy = guy
      self.build_dude()
      self.update_dude(self.guy)
      
   def build_dude(self):
      self.name_label = tk.Label(self.top_frame,bg = "white",justify = tk.LEFT,text = "Name: ")
      self.name = tk.Text(self.top_frame,height = 1,width = 20)
      self.monster_name_label.config(text = "Monster_name: ")
      self.name.delete("1.0",tk.END)
      self.name.insert(tk.END,self.guy.name)
      self.name_label.grid(row = 0,column = 0)
      self.name.grid(row = 0,column = 1)
      
   def update_dude(self,new):
      self.guy = new
      self.enable()
      super().update_monster(self.guy.monster)
      self.name.delete("1.0",tk.END)
      self.name.insert(tk.END,self.guy.name)
      self.HP.delete(0,tk.END)
      self.HP.insert(tk.END,self.guy.Working_hp)
      self.disable()
      
   def save_dude(self):
      self.guy.Working_hp = self.HP.get()

         
   def disable(self):
      self.name.config(state = tk.DISABLED)
      self.monster_name.config(state = tk.DISABLED)
      self.AC.config(state = tk.DISABLED)
      self.speed.config(state = tk.DISABLED)
      self.features.config(state = tk.DISABLED)
      self.attacks.config(state = tk.DISABLED)
      for val in self.stat_vals:
         val.config(state = tk.DISABLED)
         
   def enable(self):
      self.name.config(state = tk.NORMAL)
      self.monster_name.config(state = tk.NORMAL)
      self.AC.config(state = tk.NORMAL)
      self.speed.config(state = tk.NORMAL)
      self.features.config(state = tk.NORMAL)
      self.attacks.config(state = tk.NORMAL)
      for val in self.stat_vals:
         val.config(state = tk.NORMAL)
      

         
if __name__ == "__main__":
   
   def test_gui():
      empty_monst = Monster("Jeff",["","","","","",""],"13","12","30","","")
      r = tk.Tk()
      mgui = monster_gui(r,empty_monst)
      mgui.pack()
      mgui.mainloop()

   test_gui()
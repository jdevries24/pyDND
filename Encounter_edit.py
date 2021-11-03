import tkinter as tk
from Data_interface import *
from Encounters import *
from Monsters import *
from tkinter import messagebox


class Encounter_edit(tk.Frame):
   
   def __init__(self,root,DB,encounter):
      super().__init__(master = root,bg = "white",padx = 5,pady = 5)
      self.root = root
      self.DB = DB
      self.enc = encounter
      self.init_list()
      self.init_button()
      self.pack()
      
   def init_list(self):
      self.yScroll = tk.Scrollbar(self,orient=tk.VERTICAL)
      self.yScroll.grid(row=0,column = 1,sticky=tk.N+tk.S)
      self.dude_list = tk.Listbox(self,bg = "white",height = 33,selectmode = tk.SINGLE,yscrollcommand=self.yScroll.set)
      self.dude_list.grid(row = 0,column = 2,sticky = tk.E)
      self.yScroll['command'] = self.dude_list.yview
      self.build_list()
      
   def init_button(self):
      self.button_frame = tk.Frame(self,bg = "white",padx = 5,pady = 5)
      self.add_button = tk.Button(self.button_frame,bg = "white",command = self.add,text = "Add")
      self.remove_button = tk.Button(self.button_frame,bg = "white",command = self.remove,text = "remove")
      self.done_button = tk.Button(self,bg = "white",command = self.done,text = "done")
      self.name_label = tk.Label(self.button_frame,bg = "white",justify = tk.LEFT,text = "name")
      self.name_box = tk.Text(self.button_frame,height = 1,width = 20)
      self.name_box.delete("1.0",tk.END)
      self.name_box.insert(tk.END,self.enc.name)
      self.name_label.grid(row = 0,column = 0)
      self.name_box.grid(row = 0,column = 1)
      self.add_button.grid(row = 2,column = 1,sticky = tk.W)
      self.remove_button.grid(row = 3,column = 1,sticky = tk.W)
      self.done_button.grid(row = 1,column = 0,sticky = tk.S)
      self.button_frame.grid(row = 0,column = 0,sticky = tk.N)
   
   def build_list(self):
      self.dude_list.delete(0,tk.END)
      for d in self.enc.get_dude_list():
         self.dude_list.insert(tk.END,d)
   
   def add(self):
      t = tk.Tk()
      d_gui = Dude_edit(t,self.DB)
      d_gui.root.mainloop()
      if d_gui.name == "":
         return
      d_gui.root.destroy()
      monster_index = self.DB.search_monsters(d_gui.monster)
      monst = self.DB.get_monster(monster_index)
      if monster_index != None:
         new_dude = dude(d_gui.name,monst)
      else:
         new_dude = dude(d_gui.name,None,d_gui.temp_hp)
      self.enc.add_dude(new_dude)
      self.build_list()
      
   def done(self):
      self.enc.name = self.name_box.get("1.0","1.end")
      self.root.quit()
   
   def remove(self):
      s = self.dude_list.curselection()
      if len(s) == 0:
         return
      dude_name = self.enc.get_dude(s[0]).name
      sure = tk.messagebox.askyesno("Question","Do you want to remove "+dude_name+" ?")
      if sure:
         self.enc.remove_dude(s[0])
         self.build_list()
   
class Dude_edit(tk.Frame):
   
   def __init__(self,root,DB):
      super().__init__(master = root,bg = "white",padx = 5,pady = 5)
      self.DB = DB
      self.root = root
      self.init_list()
      self.init_side()
      self.name = ""
      self.monster = ""
      self.temp_hp = None
      self.pack()
      
   def init_list(self):
      self.yScroll = tk.Scrollbar(self,orient=tk.VERTICAL)
      self.yScroll.grid(row=0,column = 1,sticky=tk.N+tk.S)
      self.monster_list = tk.Listbox(self,bg = "white",height = 33,selectmode = tk.SINGLE,yscrollcommand=self.yScroll.set)
      self.monster_list.grid(row = 0,column = 2,sticky = tk.N)
      self.yScroll['command'] = self.monster_list.yview
      self.build_list()
      
   def build_list(self):
      self.monster_list.delete(0,tk.END)
      for m in self.DB.get_monster_list():
         self.monster_list.insert(tk.END,m)
      
   def init_side(self):
      self.side_box = tk.Frame(self,bg = "white",padx = 5,pady = 5)
      self.name_label = tk.Label(self.side_box,bg = "white",justify = tk.LEFT,text = "name")
      self.name_box = tk.Text(self.side_box,height = 1,width = 20)
      self.add_button = tk.Button(self.side_box,bg = "white",command = self.add,text = "add")
      self.empty_button = tk.Button(self.side_box,bg = "white",command = self.empty,text = "add empty")
      self.HP_label = tk.Label(self.side_box,bg = "white",justify = tk.LEFT,text = "Working_HP: ")
      self.HP_box = tk.Spinbox(self.side_box,from_ = 0,to_ = 999,increment = 1,width = 20)
      self.name_label.grid(row = 0,column = 0,sticky = tk.W)
      self.name_box.grid(row = 0,column = 1,sticky = tk.W)
      self.add_button.grid(row = 2,column = 1,sticky = tk.W)
      self.empty_button.grid(row = 3,column = 1,sticky = tk.W)
      self.HP_label.grid(row = 1,column = 0)
      self.HP_box.grid(row = 1,column = 1)
      self.side_box.grid(row = 0,column = 0,stick = tk.N)
      
   def add(self):
      self.name = self.name_box.get("1.0","1.end")
      s = self.monster_list.curselection()
      if len(s) == 0:
         self.monster = "EMPTY"
         self.temp_hp = self.HP_box.get()
      else:
         self.monster = self.DB.get_monster(s[0]).name
      self.root.quit()
   
   def empty(self):
      self.name = self.name_box.get("1.0","1.end")
      self.monster = "EMPTY"
      self.root.quit()
   
if __name__ == "__main__":
   
   def main():
      R = tk.Tk()
      test_enc = encounter("test",[])
      DB = DND_DB()
      DB.load_db("DND_STUFF")
      E_gui = Encounter_edit(R,DB,test_enc)
      E_gui.mainloop()
      
   main()
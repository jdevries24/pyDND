import tkinter as tk
from Encounters import *
from Monsters import *
from monster_gui import *

class Run_gui(tk.Frame):
   
   def __init__(self,root,enc):
      super().__init__(master = root,bg = "white",padx = 5,pady = 5)
      self.enc = enc
      self.d_gui = dude_gui(self,dude("",None,0))
      self.init_list()
      self.d_gui.grid(row = 0,column = 3)
      self.dude_list.grid(row = 0,column = 0)
      self.pack()
      
   def init_list(self):
      self.yScroll = tk.Scrollbar(self,orient=tk.VERTICAL)
      self.yScroll.grid(row=0,column = 1,sticky=tk.N+tk.S)
      self.dude_list = tk.Listbox(self,bg = "white",height = 33,selectmode = tk.SINGLE,yscrollcommand=self.yScroll.set)
      self.dude_list.grid(row = 0,column = 2,sticky = tk.N)
      self.yScroll['command'] = self.dude_list.yview
      self.dude_list.bind('<<ListboxSelect>>',self.list_selection)
      self.build_list()
      
   def build_list(self):
      self.dude_list.delete(0,tk.END)
      for d in self.enc.get_dude_hp():
         self.dude_list.insert(tk.END,d)
      
   def list_selection(self,evnt):
      self.d_gui.save_dude()
      s = self.dude_list.curselection()
      if len(s) == 0:
         return
      new_guy = self.enc.get_dude(s[0])
      self.d_gui.update_dude(new_guy)
      self.build_list()
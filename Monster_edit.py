import tkinter as tk 
from monster_gui import*
from Data_interface import *
from tkinter import messagebox

class monster_edit_program(tk.Frame):
   
   def __init__(self,root,DB):
      super().__init__(master = root,bg = "white",padx = 5,pady = 5)
      self.DB = DB
      self.mgui = monster_gui(self,new_monster(""))
      self.mgui.grid(row = 0,column = 3)
      self.build_buttons()
      self.init_list()
      self.build_list()
      self.old_name = ""
      self.pack()
      
   def init_list(self):
      self.yScroll = tk.Scrollbar(self,orient=tk.VERTICAL)
      self.yScroll.grid(row=0,column = 1,sticky=tk.N+tk.S)
      self.monster_list = tk.Listbox(self,bg = "white",height = 33,selectmode = tk.SINGLE,yscrollcommand=self.yScroll.set)
      self.monster_list.grid(row = 0,column = 2,sticky = tk.N)
      self.yScroll['command'] = self.monster_list.yview
      self.monster_list.bind('<<ListboxSelect>>',self.list_selection)
        
   def build_buttons(self):
      self.bframe = tk.Frame(self,bg = "white",pady = 5,padx = 5)
      self.new_button = tk.Button(self.bframe,bg = "white",command = self.new_monster,text = "new")
      self.remove_button = tk.Button(self.bframe,bg = "red",command = self.remove_monster,text = "remove")
      self.new_button.grid(row = 0,sticky = tk.W)
      self.remove_button.grid(row = 1,sticky = tk.W)
      self.bframe.grid(column = 0,row = 0,sticky = tk.N)
      
   def build_list(self):
      self.monster_list.delete(0,tk.END)
      for m in self.DB.get_monster_list():
         self.monster_list.insert(tk.END,m)
         
   def update_monster(self):
      s = self.monster_list.curselection()
      if len(s) == 0:
         return
      m = self.DB.get_monster(s[0])
      if m != None:
         self.old_name = m.name
         self.mgui.update_monster(m)
         
   def list_selection(self,evt):
      expected_value = self.old_name
      self.mgui.save_monster()
      actual_value = self.mgui.monst.name
      self.update_monster()
      if expected_value != actual_value:
         self.build_list()
         
   def new_monster(self):
      self.DB.append_monster(new_monster("new monster"))
      self.build_list()
      
   def remove_monster(self):
      s = self.monster_list.curselection()
      if len(s) == 0:
         return
      m = self.DB.get_monster(s[0])
      sure = tk.messagebox.askyesno("Question","Do you want to remove "+m.name+" ?")
      if sure:
         self.DB.remove_monster(s[0])
         self.build_list()
      
      
      

if __name__ == "__main__":
   def main():
      r = tk.Tk()
      DB = DND_DB()
      DB.load_db("DND_STUFF")
      mep = monster_edit_program(r,DB)
      mep.mainloop()
      DB.save_db("DND_STUFF")

   main()
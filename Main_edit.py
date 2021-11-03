from Encounter_edit import *
from Data_interface import *
from Run_encounter import *
import tkinter as tk


class encounter_list(tk.Frame):
   
   def __init__(self,root,DB):
      super().__init__(master = root,bg = "white",padx = 5,pady = 5)
      self.DB = DB
      self.root = root
      self.init_buttons()
      self.init_list()
      self.pack()
      
   def init_buttons(self):
      self.button_frame = tk.Frame(self,bg = "white",padx = 5,pady = 5)
      self.new_button = tk.Button(self.button_frame,bg = "white",command = self.new,text = "New Encounter")
      self.edit_button = tk.Button(self.button_frame,bg = "white",command = self.edit,text = "Edit Encounter")
      self.run_button = tk.Button(self.button_frame,bg = "white",command = self.run,text = "Run Encounter")
      self.remove_button = tk.Button(self.button_frame,bg = "white",command = self.remove,text = "Remove")
      self.new_button.grid(row = 0,column = 0,sticky = tk.E)
      self.edit_button.grid(row = 1,column = 0,sticky = tk.E)
      self.run_button.grid(row = 2,column = 0,sticky = tk.E)
      self.remove_button.grid(row = 3,column = 0,sticky = tk.E)
      self.button_frame.grid(column = 0,sticky = tk.N)
      
   def init_list(self):
      self.yScroll = tk.Scrollbar(self,orient=tk.VERTICAL)
      self.yScroll.grid(row=0,column = 1,sticky=tk.N+tk.S)
      self.enc_list = tk.Listbox(self,bg = "white",height = 33,selectmode = tk.SINGLE,yscrollcommand=self.yScroll.set)
      self.enc_list.grid(row = 0,column = 2,sticky = tk.N)
      self.yScroll['command'] = self.enc_list.yview
      self.build_list()

   def build_list(self):
      self.enc_list.delete(0,tk.END)
      for e in self.DB.get_encounter_list():
         self.enc_list.insert(tk.END,e)
   
   def new(self):
      enc = encounter("new encounter",[])
      self.DB.append_encounter(enc)
      self.build_list()
      t = tk.Tk()
      e_gui = Encounter_edit(t,self.DB,enc)
      e_gui.root.mainloop()
      self.build_list()
      e_gui.root.destroy()
   
   def edit(self):
      enc = self.get_list_enc()
      if enc == None:
         return
      t = tk.Tk()
      e_gui = Encounter_edit(t,self.DB,enc)
      e_gui.root.mainloop()
      self.build_list()
      e_gui.root.destroy()
   
   def run(self):
      enc = self.get_list_enc()
      if enc == None: return
      t = tk.Tk()
      r_gui = Run_gui(t,enc)
      r_gui.mainloop()
   
   def remove(self):
      s = self.enc_list.curselection()
      if len(s) == 0:
         return
      enc_name = self.DB.get_encounter(s[0]).name
      sure = tk.messagebox.askyesno("Question","Do you want to remove "+enc_name+" ?")
      if sure:
         self.DB.remove_encounter(s[0])
         self.build_list()
   
   def get_list_enc(self):
      s = self.enc_list.curselection()
      if len(s) == 0:
         return None
      return self.DB.get_encounter(s[0])
   
if __name__ == "__main__":
   
   def main():
      R = tk.Tk()
      DB = DND_DB()
      DB.load_db("DND_STUFF")
      e_gui = encounter_list(R,DB)
      e_gui.mainloop()
      DB.save_db("DND_STUFF")
      
   main()
      
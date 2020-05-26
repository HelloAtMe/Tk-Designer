import json
import os
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

# one more thing:
# 0. check all widget attributes update json
# 00. write the code about treeview
# 1. generate code 
# 2. improve the code style and add some example to show 
#   how to create them in form of tips (treeview listbox scrollbar radiobutton
#   checkbutton notebook spinbox progressbar) (update json more carefully)

# About Version 2.0
# split all widget in defferent class and put them in a single .py file 

class SuperWidget():
    def __init__(self, widget_id=0, widget_class_id=0, widget_parent=None, widget_type=""):
        self.widget_id = widget_id
        self.widget_class_id = widget_class_id
        self.widget_parent = widget_parent
        self.widget_type = widget_type

        self.new_widget_parent = None
        # for widget that parent not top

        self.init_widget_configs()
        self.widget_apply()
        self.configs_apply()
        
    def init_widget_configs(self):
# ##################################################################################################################
# #  init_all_widgets_configs
#########################################################################################################
        if self.widget_type == "Label":
            self.widget_configs = {
                "widget_label":self.widget_type+str(self.widget_class_id),
                "relief":"groove",   
                "bg":"#F0F0F0",
                "x":"0",
                "y":"0",
                "w":"150",
                "h":"25",
            
                "family":font.nametofont("TkDefaultFont").cget("family"),
                "size":font.nametofont("TkDefaultFont").cget("size"),
                "weight":font.nametofont("TkDefaultFont").cget("weight"),
                "fg":"#000000",
                "font_anchor":"center",
            
                "widget_name":self.widget_type+str(self.widget_class_id),
                "master":"top",
                "bind_key":"",
                "bind_func":""
            }
        elif self.widget_type == "Entry":
            self.widget_configs = {
                
                    "relief":"flat",   
                    "x":"0",
                    "y":"0",
                    "w":"150",
                    "h":"25",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "show":"",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Button":
            self.widget_configs = {
                
                    "widget_label":self.widget_type+str(self.widget_class_id),
                    "relief":"flat",   
                    "x":"0",
                    "y":"0",
                    "w":"87",
                    "h":"25",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "cmd_func":self.widget_type+str(self.widget_class_id)+"_cmd"
                
            }
        elif self.widget_type == "Radiobutton":
            self.widget_configs = {
                
                    "widget_label":self.widget_type+str(self.widget_class_id),
                    "relief":"flat",   
                    "x":"0",
                    "y":"0",
                    "w":"110",
                    "h":"25",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "value":"",
                    "cmd_func":self.widget_type+str(self.widget_class_id)+"_cmd"
                
            }
        elif self.widget_type == "Checkbutton":
            self.widget_configs = {
                
                    "widget_label":self.widget_type+str(self.widget_class_id),
                    "relief":"flat",   
                    "x":"0",
                    "y":"0",
                    "w":"110",
                    "h":"25",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "cmd_func":self.widget_type+str(self.widget_class_id)+"_cmd"
                
            }
        elif self.widget_type == "Labelframe":
            self.widget_configs = {
                
                    "widget_label":self.widget_type+str(self.widget_class_id),
                    "relief":"groove", 
                    "lb_anchor":"nw",
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                
            }
        elif self.widget_type == "Notebook":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                
            }
        elif self.widget_type == "Combobox":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"150",
                    "h":"25",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
               
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Spinbox":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"150",
                    "h":"25",
               
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "from":"",
                    "to":"",
                    "increment":"",
                    "values":"",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Treeview_tree":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
               
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "selectmode":"",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Treeview_headings":
            self.widget_configs = {
            
                    "relief":"flat", 
                    "bg":"#F0F0F0",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "selectmode":"",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Progressbar_v":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#F0F0F0",
                    "x":"0",
                    "y":"0",
                    "w":"20",
                    "h":"200",
                
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "mode":"",
                    "maximum":""
                
            }
        elif self.widget_type == "Progressbar_h":
            self.widget_configs = {

                    "relief":"flat", 
                    "bg":"#F0F0F0",
                    "x":"0",
                    "y":"0",
                    "w":"200",
                    "h":"20",
               
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "mode":"",
                    "maximum":""
                
            }
        elif self.widget_type == "Scrollbar_v":
            self.widget_configs = {
            
                    "relief":"flat",
                    "bg":"#F0F0F0",
                    "x":"0",
                    "y":"0",
                    "w":"20",
                    "h":"200",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                
            }
        elif self.widget_type == "Scrollbar_h":
            self.widget_configs = {
                    "relief":"flat",
                    "bg":"#F0F0F0",
                    "x":"0",
                    "y":"0",
                    "w":"200",
                    "h":"20",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
            }
        elif self.widget_type == "Text":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#FFFFFF",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
                
                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",
                    "font_anchor":"center",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top"
                
            }
        elif self.widget_type == "Listbox":
            self.widget_configs = {
                    # "relief":"flat", 
                    "bg":"#FFFFFF",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",

                    "family":font.nametofont("TkDefaultFont").cget("family"),
                    "size":font.nametofont("TkDefaultFont").cget("size"),
                    "weight":font.nametofont("TkDefaultFont").cget("weight"),
                    "fg":"#000000",

                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top",
                    "selectmode":"",
                    "bind_key":"",
                    "bind_func":""
                
            }
        elif self.widget_type == "Canvas":
            self.widget_configs = {
                
                    "relief":"flat", 
                    "bg":"#FFFFFF",  
                    "x":"0",
                    "y":"0",
                    "w":"300",
                    "h":"200",
                
                    "widget_name":self.widget_type+str(self.widget_class_id),
                    "master":"top"
                
            }
# ##################################################################################################################
# #  init_all_widgets_configs
#########################################################################################################

    def widget_apply(self):
        self.style = Style()
        if self.widget_type == "Label":
            self.widget = Label(self.widget_parent, style=str(self.widget_id)+".TLabel")
        elif self.widget_type == "Entry":
            self.widget = Entry(self.widget_parent, style=str(self.widget_id)+".TEntry")
        elif self.widget_type == "Button":
            self.widget = Button(self.widget_parent, style=str(self.widget_id)+".TButton")
        elif self.widget_type == "Radiobutton":
            self.widget = Radiobutton(self.widget_parent, style=str(self.widget_id)+".TRadiobutton")
        elif self.widget_type == "Checkbutton":
            self.widget = Checkbutton(self.widget_parent, style=str(self.widget_id)+".TCheckbutton")
        elif self.widget_type == "Labelframe":
            self.widget = Labelframe(self.widget_parent, style=str(self.widget_id)+".TLabelframe")
        elif self.widget_type == "Notebook":
            self.widget = Notebook(self.widget_parent, style=str(self.widget_id)+".TNotebook")
            self.tab1 = Frame(self.widget_parent)
            self.tab2 = Frame(self.widget_parent)
            self.widget.add(self.tab1, text="tab1")
            self.widget.add(self.tab2, text="tab2")
        elif self.widget_type == "Combobox":
            self.widget = Combobox(self.widget_parent, style=str(self.widget_id)+".TCombobox")
        elif self.widget_type == "Spinbox":
            self.widget = Spinbox(self.widget_parent, style=str(self.widget_id)+".TSpinbox")
        elif self.widget_type == "Treeview_tree":
            self.widget = Treeview(self.widget_parent, show="tree", style=str(self.widget_id)+".Treeview")
            idx_ = self.widget.insert("", 0, "1", text="00", values=("1"))
            idx_1 = self.widget.insert(idx_, 0, "2", text="01", values=("2"))
            idx_2 = self.widget.insert(idx_, 1, "3", text="02", values=("3"))
            idy_ = self.widget.insert("", 1, "4", text="10", values=("4"))
            idy_1 = self.widget.insert(idy_, 0, "5", text="11", values=("5"))
            idy_2 = self.widget.insert(idy_, 1, "6", text="12", values=("6"))

        elif self.widget_type == "Treeview_headings":
            columns = ("1", "2", "3")
            self.widget = Treeview(self.widget_parent, show="headings", columns=columns, style=str(self.widget_id)+".Treeview")
            self.widget.column("1", width=50, anchor="center")
            self.widget.column("2", width=50, anchor="center")
            self.widget.column("3", width=50, anchor="center")
            self.widget.heading("1", text="col1")
            self.widget.heading("2", text="col2")
            self.widget.heading("3", text="col3")
            init_value = [("", "", ""), ("", "", "")]
            i = 0 
            for v in init_value:
                self.widget.insert("", i, values=v)
                i += 1               
        elif self.widget_type == "Progressbar_v":
            self.widget = Progressbar(self.widget_parent, orient='vertical')
        elif self.widget_type == "Progressbar_h":
            self.widget = Progressbar(self.widget_parent, orient='horizontal')
        elif self.widget_type == "Scrollbar_v":
            self.widget = Scrollbar(self.widget_parent, orient='vertical')
        elif self.widget_type == "Scrollbar_h":
            self.widget = Scrollbar(self.widget_parent, orient='horizontal')
        elif self.widget_type == "Text":
            self.widget = Text(self.widget_parent)
        elif self.widget_type == "Listbox":
            self.widget = Listbox(self.widget_parent, justify="center")
            for i in ("1", "2", "3"):
                self.widget.insert("end", i)
        elif self.widget_type == "Canvas":
            self.widget = Canvas(self.widget_parent)
        self.widget.topclass = self
            
    def configs_apply(self):
# ##################################################################################################################
# #  init_all_widgets_configs
#########################################################################################################
        if self.widget_type == "Label":
            self.widget["text"]=self.widget_configs["widget_label"]
            self.style.configure(str(self.widget_id)+".TLabel", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Entry":
            self.style.configure(str(self.widget_id)+".TEntry", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    # background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Button":
            self.widget["text"]=self.widget_configs["widget_label"]
            self.style.configure(str(self.widget_id)+".TButton", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    # background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
            # self.widget["relief"] = self.widget_configs["relief"]
            # self.widget["fg"] = self.widget_configs["fg"]
            # self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Radiobutton":
            self.style.configure(str(self.widget_id)+".TRadiobutton", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    # background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))     
            self.widget["text"]=self.widget_configs["widget_label"]
            # self.widget["relief"] = self.widget_configs["relief"]
            # self.widget["fg"] = self.widget_configs["fg"]
            # self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Checkbutton":
            self.widget["text"]=self.widget_configs["widget_label"]
            self.style.configure(str(self.widget_id)+".TCheckbutton", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    # background=self.widget_configs["bg"],
                    # anchor=self.widget_configs["font_anchor"], 
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
            
            # self.widget["relief"] = self.widget_configs["relief"]
            # self.widget["fg"] = self.widget_configs["fg"]
            # self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Labelframe":
            self.widget["text"]=self.widget_configs["widget_label"]
            self.widget["labelanchor"]=self.widget_configs["lb_anchor"]
            self.style.configure(str(self.widget_id)+".TLabelframe", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"],
                    # labelanchor=self.widget_configs["labelanchor"],
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
            
            # self.widget["relief"] = self.widget_configs["relief"]
            # self.widget["fg"] = self.widget_configs["fg"]
            # self.widget["bg"] = self.widget_configs["bg"]
            # self.widget["labelanchor"] = self.widget_configs["labelanchor"]
            # self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Notebook":
            self.style.configure(str(self.widget_id)+".TNotebook", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Combobox":
            self.style.configure(str(self.widget_id)+".TCombobox", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Spinbox":
            self.style.configure(str(self.widget_id)+".TSpinbox", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))            
        elif self.widget_type == "Treeview_tree":
            self.style.configure(str(self.widget_id)+".Treeview", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Treeview_headings":
            self.style.configure(str(self.widget_id)+".Treeview", 
                    relief=self.widget_configs["relief"],
                    foreground=self.widget_configs["fg"],
                    background=self.widget_configs["bg"], 
                    anchor=self.widget_configs["font_anchor"],
                    font=(self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"]))
        elif self.widget_type == "Progressbar_v":
            self.style.configure("TProgressbar", 
                    relief=self.widget_configs["relief"],
                    background=self.widget_configs["bg"])
        elif self.widget_type == "Progressbar_h":
            self.style.configure("TProgressbar", 
                    relief=self.widget_configs["relief"],
                    background=self.widget_configs["bg"])           
        elif self.widget_type == "Scrollbar_v":
            self.style.configure("TScrollbar", 
                    relief=self.widget_configs["relief"],
                    background=self.widget_configs["bg"])      
            # self.widget["bg"] = self.widget_configs["bg"]
            # self.widget["relief"] = self.widget_configs["relief"]
        elif self.widget_type == "Scrollbar_h":
            self.style.configure("TScrollbar", 
                    relief=self.widget_configs["relief"],
                    background=self.widget_configs["bg"])
            # self.widget["bg"] = self.widget_configs["bg"]
            # self.widget["relief"] = self.widget_configs["relief"]
        elif self.widget_type == "Text":
            self.widget["relief"] = self.widget_configs["relief"]
            self.widget["bg"] = self.widget_configs["bg"]
            self.widget["fg"] = self.widget_configs["fg"]
            self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Listbox":
            self.widget["bg"] = self.widget_configs["bg"]
            self.widget["fg"] = self.widget_configs["fg"]
            self.widget["font"] = (self.widget_configs["family"], int(self.widget_configs["size"]), self.widget_configs["weight"])
        elif self.widget_type == "Canvas":
            self.widget["relief"] = self.widget_configs["relief"]
            self.widget["bg"] = self.widget_configs["bg"]

        if self.widget_configs["master"] == "top":
            widget_px = 0
            widget_py = 0
            widget_pwidth = self.widget_parent.winfo_width()
            widget_pheight = self.widget_parent.winfo_height()
        else:
            widget_px = self.new_widget_parent.winfo_x()
            widget_py = self.new_widget_parent.winfo_y()
            widget_pwidth = self.new_widget_parent.winfo_width()
            widget_pheight = self.new_widget_parent.winfo_height()
        
        widget_x = int(self.widget_configs["x"])
        widget_y = int(self.widget_configs["y"])
        widget_width = int(self.widget_configs["w"])
        widget_height = int(self.widget_configs["h"])

        if int(self.widget_configs["x"]) < widget_px:
            widget_x = widget_px
        if int(self.widget_configs["y"]) < widget_py:
            widget_y = widget_py
        if ((widget_x + int(self.widget_configs["w"])) > 
            widget_px + widget_pwidth):
            widget_width = widget_px + widget_pwidth - widget_x
        if ((widget_y + int(self.widget_configs["h"])) > 
            widget_py + widget_pheight):
            widget_height = widget_py + widget_pheight - widget_y

        self.widget_configs["x"] = str(widget_x)
        self.widget_configs["y"] = str(widget_y)
        self.widget_configs["w"] = str(widget_width)
        self.widget_configs["h"] = str(widget_height)

        self.widget.place(x=widget_x, y=widget_y, 
                width=widget_width, height=widget_height, anchor="nw")
# ##################################################################################################################
# #  init_all_widgets_configs
#########################################################################################################
    
    def move_widget_pos(self, deltax=0, deltay=0):
        widget_x = self.widget.winfo_x()+deltax
        widget_y = self.widget.winfo_y()+deltay
        widget_width = self.widget.winfo_width()
        widget_height = self.widget.winfo_height()

        if self.widget_configs["master"] == "top":
            widget_px = 0
            widget_py = 0
            widget_pwidth = self.widget_parent.winfo_width()
            widget_pheight = self.widget_parent.winfo_height()   
        else:
            widget_px = self.new_widget_parent.winfo_x()
            widget_py = self.new_widget_parent.winfo_y()
            widget_pwidth = self.new_widget_parent.winfo_width()
            widget_pheight = self.new_widget_parent.winfo_height()
        
        if widget_pwidth < widget_width:
            widget_width = widget_pwidth
            widget_x = widget_px
        elif widget_x < widget_px:
            widget_x = widget_px
        elif widget_x > (widget_pwidth - widget_width + widget_px):
            widget_x = (widget_pwidth - widget_width + widget_px)

        if widget_pheight < widget_height:
            widget_height = widget_pheight
            widget_y = widget_py
        elif widget_y < widget_py:
            widget_y = widget_py
        elif widget_y > (widget_pheight - widget_height + widget_py):
            widget_y = (widget_pheight - widget_height + widget_py)

        self.widget_configs["x"] = str(widget_x)
        self.widget_configs["y"] = str(widget_y)
        self.widget_configs["w"] = str(widget_width)
        self.widget_configs["h"] = str(widget_height)
        self.configs_apply()
        
    def resize_widget_size(self, deltawidth=0, deltaheight=0):
        if self.widget_configs["master"] == "top":
            widget_px = 0
            widget_py = 0
            widget_pwidth = self.widget_parent.winfo_width()
            widget_pheight = self.widget_parent.winfo_height()
        else:
            widget_px = self.new_widget_parent.winfo_x()
            widget_py = self.new_widget_parent.winfo_y()
            widget_pwidth = self.new_widget_parent.winfo_width()
            widget_pheight = self.new_widget_parent.winfo_height()

        widget_width = self.widget.winfo_width() + deltawidth
        widget_height = self.widget.winfo_height() + deltaheight
        widget_x = self.widget.winfo_x()
        widget_y = self.widget.winfo_y()

        if (widget_width + widget_x) > (widget_px + widget_pwidth):
            widget_width = widget_px + widget_pwidth - widget_x
        if (widget_height + widget_y) > (widget_py + widget_pheight):
            widget_height = widget_py + widget_pheight - widget_y

        self.widget_configs["x"] = str(widget_x)
        self.widget_configs["y"] = str(widget_y)
        self.widget_configs["w"] = str(widget_width)
        self.widget_configs["h"] = str(widget_height)

        self.configs_apply()


class ShowPanel():
    def __init__(self, master=None):
        self.top = Toplevel(master)        
        self.top.geometry("800x600+300+100")
        self.top.title("Show")

        self.style = Style()
        # self.topf = Frame(self.top)
        # self.topf.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")
        # self.top.bind("<Delete>", self.remove_widget)
        self.top.bind("<Double-Button-1>", lambda event : self.show_top_config())
        self.top.bind("<BackSpace>", self.del_superwidget)

        # self.top.bind("<Button-1>", self.get_cursor_current_position)
        # self.top.bind("<ButtonRelease-1>", self.)
        # self.top.bind("<B1-Motion>", self.move_widget_with_mouse)
        self.conifgpanel = ConfigPanel(master)

        self.winfo = {
            "widget"    :   self.top,
            "configs"   : {"x"              :       "250",
                            "y"             :       "100",
                            "w"             :       "800",
                            "h"             :       "600",
                            "widget_label"  :       str(self.top.title()),
                            "theme"         :       self.style.theme_use()}
        }  
        self.conifgpanel.show_win_cfg(self.winfo)
        # self.show_top_config()
        # Variables
        self.current_selected_superwidget = None
        self.widgets_count = 0
        self.superwidget_contain = []
        self.widget_class_count = {
            "Label"             :   0,
            "Entry"             :   0,
            "Button"            :   0,
            "Radiobutton"       :   0,
            "Checkbutton"       :   0,
            "Labelframe"        :   0,
            "Notebook"          :   0,
            "Combobox"          :   0,
            "Spinbox"           :   0,
            "Treeview_tree"     :   0,
            "Treeview_headings"  :   0,
            "Progressbar_v"     :   0,
            "Progressbar_h"     :   0,
            "Scrollbar_v"       :   0,
            "Scrollbar_h"       :   0,
            # "Separator_h"       :   0,
            "Text"              :   0,
            "Listbox"           :   0,
            "Canvas"            :   0}
        self.cursor_pos = [0, 0]

    def show_top_config(self):
        self.current_selected_superwidget = None
        self.winfo = {
            "widget"    :   self.top,
            "configs"   : {"x"              :       str(self.top.winfo_x()),
                            "y"             :       str(self.top.winfo_y()),
                            "w"             :       str(self.top.winfo_width()),
                            "h"             :       str(self.top.winfo_height()),
                            "widget_label"  :       str(self.top.title()),
                            "theme"         :       self.style.theme_use()}
        }  
        self.conifgpanel.show_win_cfg(self.winfo)

    def add_superwidget(self, widget_type=""):
        superwidget = SuperWidget(self.widgets_count, self.widget_class_count[widget_type], self.top, widget_type)
        superwidget.widget.bind("<Button-1>", self.get_selected_widget)
        superwidget.widget.bind("<B1-Motion>", self.move_widget_with_mouse)
        # superwidget.widget.bind("<BackSpace>", self.del_superwidget)
        # superwidget.widget.bind("<ButtonRelease-1>", self.move_widget_with_mouse)
        # set default current superwidget 
        self.current_selected_superwidget = superwidget  
        self.superwidget_contain.append(superwidget)
        self.conifgpanel.superwidget_contain = self.superwidget_contain
        self.widgets_count += 1
        self.widget_class_count[widget_type] += 1

    def get_selected_widget(self, event):
        self.current_selected_superwidget = event.widget.topclass
        # get cursor for widget move
        self.cursor_pos = [event.x, event.y]
        self.conifgpanel.show_superwidget_cfg(self.current_selected_superwidget)

    # def get_cursor_current_position(self, event):
    #     self.cursor_pos = [event.x, event.y]

    def move_widget_with_mouse(self, event):
        deltax = event.x-self.cursor_pos[0]
        deltay = event.y-self.cursor_pos[1]
        # print(event.x, self.cursor_pos[0])
        if self.current_selected_superwidget != None:
            self.current_selected_superwidget.move_widget_pos(deltax, deltay)
            self.conifgpanel.show_superwidget_cfg(self.current_selected_superwidget)


    def move_widget(self, deltax=0, deltay=0):
        if self.current_selected_superwidget != None:
            self.current_selected_superwidget.move_widget_pos(deltax, deltay)
            self.conifgpanel.show_superwidget_cfg(self.current_selected_superwidget)
    def resize_widget(self, deltawidth=0, deltaheight=0):
        if self.current_selected_superwidget != None:
            self.current_selected_superwidget.resize_widget_size(deltawidth, deltaheight)
            self.conifgpanel.show_superwidget_cfg(self.current_selected_superwidget)

    def del_superwidget(self, event):
        if self.current_selected_superwidget != None:
            self.current_selected_superwidget.widget.place_forget()
            for superwidget in self.superwidget_contain:
                if superwidget.widget_id == self.current_selected_superwidget.widget_id:
                    self.superwidget_contain.remove(superwidget)
                    break
            self.current_selected_superwidget = None
            self.show_top_config()

                
class ConfigWidget():
    def __init__(self, master=None, key="", value="", index=0):
        self.master = master
        self.index = index
        self.key = key
        self.c_value = value

        self.top = Frame(self.master)
        self.top.place(x=0, y=0+self.index*30, relwidth=1, height=27, anchor="nw")
        self.style = Style()

        self.show_configwidget()

    def show_configwidget(self):
        if self.key == "widget_label":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "relief":
            self.type =  1
            self.parent_key = "app_show"
            self.combo_list = ["flat", "groove", "raised", "sunken", "solid", "ridge"]
        elif self.key == "lb_anchor":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "bg":
            self.type = 2
            self.parent_key = "app_show"
        elif self.key == "x":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "y":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "w":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "h":
            self.type = 0
            self.parent_key = "app_show"
        elif self.key == "theme":
            self.combo_list = self.style.theme_names()
            self.type = 1

        elif self.key == "family":
            self.type = 0
            self.parent_key = "font_cfg"
        elif self.key == "size":
            self.type = 0
            self.parent_key = "font_cfg"
        elif self.key == "weight":
            self.type = 1
            self.parent_key = "font_cfg"
            self.combo_list = ["normal", "bold"]
        elif self.key == "fg":
            self.type = 2
            self.parent_key = "font_cfg"
        elif self.key == "font_anchor":
            self.type = 0
            self.parent_key = "font_cfg"
        
        elif self.key == "show":
            self.type = 0
        elif self.key == "widget_name":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "master":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "selectmode":
            self.combo_list = ["browse", "extended"]
            self.type = 1
            self.parent_key = "code_gen"
        elif self.key == "mode":
            self.type = 1
            self.parent_key = "code_gen"
            self.combo_list = ["determinate", "indeterminate"]
        elif self.key == "maximum":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "from":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "to":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "increment":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "cmd_func":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "value":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "values":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "bind_key":
            self.type = 0
            self.parent_key = "code_gen"
        elif self.key == "bind_func":
            self.type = 0
            self.parent_key = "code_gen"

        self.style.configure("key.TLabel", anchor="center", relief="groove")
        self.key_label = Label(self.top, text=self.key, style="key.TLabel")
        self.key_label.place(relx=0, rely=0, relwidth=0.4, relheight=1, anchor="nw")

        if self.type == 0:      # for label entry   
            self.value_ctrl = Entry(self.top, justify="center")
            self.value_ctrl.place(relx=0.4, rely=0, relwidth=0.6, relheight=1, anchor="nw")
            self.value_ctrl.insert(0, self.c_value)
        elif self.type == 1:    # for label combobox
            self.value_ctrl = Combobox(self.top, justify="center", values=self.combo_list)
            if self.c_value not in self.combo_list: 
                self.value_ctrl.current(0)
            else:
                for i,j in enumerate(self.combo_list):
                    if j == self.c_value:
                        self.value_ctrl.current(i)
                        break
            self.value_ctrl.place(relx=0.4, rely=0, relwidth=0.6, relheight=1, anchor="nw")
        elif self.type == 2:    # for label entry label color choose
            self.value_ctrl = Entry(self.top, justify="center")
            self.value_ctrl.place(relx=0.4, rely=0, relwidth=0.5, relheight=1, anchor="nw")  
            self.value_ctrl.insert(0, self.c_value)

            self.style.configure(self.key+".TLabel", background=self.c_value, relief="groove")
            self.color_lb = Label(self.top, relief="groove", style=self.key+".TLabel")
            self.color_lb.place(relx=0.915, rely=0.25, relwidth=0.07, relheight=0.5, anchor="nw")
            self.color_lb.bind("<Button-1>", self.color_choose)

        self.value_ctrl.topclass = self     

    def chg_value(self, newvalue=""):
        self.c_value = newvalue
        if self.type == 0:
            self.value_ctrl.delete(0, "end")
            self.value_ctrl.insert(0, self.c_value)
        elif self.type == 1:
            if self.c_value not in self.combo_list: 
                self.value_ctrl.current(0)
            else:
                for i,j in enumerate(self.combo_list):
                    if j == self.c_value:
                        self.value_ctrl.current(i)
                        break
        elif self.type == 2:
            self.value_ctrl.delete(0, "end")
            self.value_ctrl.insert(0, self.c_value)
            self.style.configure(self.key+".TLabel", background=self.c_value, relief="groove")

    def color_choose(self, event):
        color = colorchooser.askcolor(color=self.c_value, parent=self.master)
        if color[0] != None:
            self.c_value = color[1]
            # self.enVar.set(self.c_value)
            self.value_ctrl.delete(0,"end")
            self.value_ctrl.insert(0, self.c_value)
            self.style.configure(self.key+".TLabel", background=self.c_value, relief="groove")
            # event.widget["bg"] = self.c_value
            
class ConfigPanel():
    def __init__(self, master=None):
        # self.top.bind("<Return>", self.configs_apply)
        # variable
        self.master = master
        self.superwidget_contain = []

        self.current_superwidget = None
        self.last_superwidget = None

        self.winfo = {}

        self.top = Toplevel(self.master)
        self.top.geometry("230x600+1500+100")
        self.top.title("Configs")

    def show_win_cfg(self, winfo={}):
        self.winfo = winfo
        self.current_superwidget = None
        # self.clear()
        self.top.destroy()
        self.top = Toplevel(self.master)
        self.top.geometry("230x600+1500+100")
        self.top.title("Configs")

        self.cfg_contain = []

        i = 0
        for key, value in self.winfo["configs"].items():
            cfg = ConfigWidget(self.top, key, value, i)
            self.cfg_contain.append(cfg)
            i += 1
            
        self.last_superwidget = self.current_superwidget
        for cfg in self.cfg_contain:
            cfg.value_ctrl.bind("<Return>", self.win_apply)

    def win_apply(self, event):
        event.widget.topclass.c_value = event.widget.get()
        self.winfo["configs"][event.widget.topclass.key] = event.widget.topclass.c_value
        for cfg in self.cfg_contain:
           self.winfo["configs"][cfg.key] = cfg.c_value 
    
        self.winfo["widget"].geometry("{}x{}+{}+{}".format(self.winfo["configs"]["w"], self.winfo["configs"]["h"], self.winfo["configs"]["x"], self.winfo["configs"]["y"]))
        self.winfo["widget"].title("{}".format(self.winfo["configs"]["widget_label"]))
        self.style = Style()
        self.style.theme_use("{}".format(self.winfo["configs"]["theme"]))

    def show_superwidget_cfg(self, superwidget=None):
        # if self.superwidget == 
        self.current_superwidget = superwidget
        if self.last_superwidget != None:
            if self.last_superwidget.widget_id != self.current_superwidget.widget_id:
                self.show_new_cfg_panel()
            else:
                self.chg_cfg_panel()
        else:
            self.show_new_cfg_panel()
        self.last_superwidget = self.current_superwidget

    def chg_cfg_panel(self):
        for cfg in self.cfg_contain:
            for k, c in self.current_superwidget.widget_configs.items():
                # for k_, c_ in c.items():
                if k == cfg.key:
                    cfg.chg_value(c)

    def show_new_cfg_panel(self):
        self.top.destroy()
        self.top = Toplevel(self.master)
        self.top.geometry("230x600+1500+100")
        self.top.title("Configs")

        self.cfg_contain = []

        i = 0
        # last_height = 0
        for key, value in self.current_superwidget.widget_configs.items():
            cfg = ConfigWidget(self.top, key, value, i)
            self.cfg_contain.append(cfg)
            i += 1

            # lbf = Labelframe(self.top, text=key, labelanchor="n")
            # lbf.place(x=0, y=0+last_height, relwidth=1, height=35*len(value), anchor="nw")
            # last_height = last_height + 35*len(value)
            # i = i+1
            # j = 0
            # if key == "app_show":
            #     for l, v in value.items():
            #         cfg = ConfigWidget(lbf, l, v, j)
            #         self.cfg_contain.append(cfg)
            #         j += 1
            # elif key == "font_cfg":
            #     for l, v in value.items():
            #         cfg = ConfigWidget(lbf, l, v, j)
            #         self.cfg_contain.append(cfg)

            #         j += 1
            # elif key == "code_gen":
            #     for l, v in value.items():
            #         cfg = ConfigWidget(lbf, l, v, j)
            #         self.cfg_contain.append(cfg)
            #         j += 1        

        for cfg in self.cfg_contain:
            cfg.value_ctrl.bind("<Return>", self.configs_apply)
    # def clear(self):
    #     for widget in self.top.winfo_children():
    #         for f in widget.winfo_children():
    #             for w in f.winfo_children():
    #                 w.destory()
    #             f.destory()
    #         widget.destory()
    def select_parent_widget(self, widget_name=""):
        widget_parent = None
        for superwidget in self.superwidget_contain:
            if superwidget.widget_configs["widget_name"] == widget_name:
                widget_parent = superwidget.widget
                break
        return widget_parent

    def configs_apply(self, event):
        # event.widget.topclass.c_value = event.widget.get()
        for cfg in self.cfg_contain:
            cfg.c_value = cfg.value_ctrl.get()

        if self.current_superwidget != None:
            for cfg in self.cfg_contain:
                if cfg.key == "master" and cfg.c_value != "top":
                    if self.select_parent_widget(cfg.c_value) != None:
                        self.current_superwidget.new_widget_parent = self.select_parent_widget(cfg.c_value)
                self.current_superwidget.widget_configs[cfg.key] = cfg.c_value
            # self.current_superwidget.widget_configs[event.widget.topclass.parent_key][event.widget.topclass.key] = event.widget.get()
    
        self.current_superwidget.configs_apply()

class WidgetCtrlPanel():
    def __init__(self, master=None):
        self.widget_type = ""
        self.master = master
        self.master.geometry("230x600+20+100")
        self.master.title("Tools")

        self.default_delta_size = 2        
        self.show()
        self.showpanel = ShowPanel(master)
        # self.showpanel.show_top_config()

        
    def show(self):
        self.style = Style()
        if os.name != "nt":
            self.style.theme_use("default")
        self.style.configure("WC.TButton", anchor="center")
        self.style.configure("WC.TLabel", anchor="center")

        widget_type_define = ["Label",
                                "Entry",
                                "Button",
                                "Radiobutton",
                                "Checkbutton",
                                "Labelframe",
                                "Notebook",
                                "Combobox",
                                "Spinbox",
                                "Treeview_tree",
                                "Treeview_headings",
                                "Progressbar_v",
                                "Progressbar_h",
                                "Scrollbar_v",
                                "Scrollbar_h",
                                "Text",
                                "Listbox",
                                "Canvas"]
        gen_exp_code_btn = Button(self.master, text="Generate And Export Code", command=self.gen_exp_code, style="WC.TButton")
        gen_exp_code_btn.place(relx=0.1, rely=0.03, relwidth=0.8, relheight=0.05, anchor="nw")

        for index, widget_type in enumerate(widget_type_define):
            btn = Button(self.master, text=widget_type, style="WC.TButton")
            btn.place(relx=0.01+(index%2)*0.5, rely=0.1+(index//2)*0.06, relwidth=0.48, relheight=0.045, anchor="nw")
            btn.bind("<Button-1>", self.add_widget)

        movef = Labelframe(self.master, text="Move", labelanchor="n")
        movef.place(relx=0, rely=0.63, relwidth=1, relheight=0.2, anchor="nw")
        
        m_up = Button(movef, text="UP", command=self.move_up, style="WC.TButton")
        m_up.place(relx=0.36,rely=0.01,relwidth=0.28, relheight=0.4, anchor="nw")
        m_down = Button(movef, text="DOWN", command=self.move_down, style="WC.TButton")
        m_down.place(relx=0.36,rely=0.59,relwidth=0.28, relheight=0.4, anchor="nw")
        m_left = Button(movef, text="LEFT", command=self.move_left, style="WC.TButton")
        m_left.place(relx=0.04,rely=0.36,relwidth=0.28, relheight=0.4, anchor="nw")
        m_right = Button(movef, text="RIGHT", command=self.move_right, style="WC.TButton")
        m_right.place(relx=0.68,rely=0.36,relwidth=0.28, relheight=0.4, anchor="nw")

        resizef = Labelframe(self.master, text="Resize", labelanchor="n")
        resizef.place(relx=0, rely=0.83, relwidth=1, relheight=0.17, anchor="nw")

        self.width_delta_Var = StringVar(value="2")
        r_width_lb = Label(resizef, text="WIDTH:", style="WC.TLabel")
        r_width_lb.place(relx=0.05, rely=0.01, relwidth=0.3, relheight=0.4, anchor="nw")
        r_width_plus_btn = Button(resizef, text="-", command=self.width_minus, style="WC.TButton")
        r_width_plus_btn.place(relx=0.4, rely=0.065, relwidth=0.15, relheight=0.4, anchor="nw")
        r_width_delta_en = Entry(resizef, textvariable=self.width_delta_Var, justify="center")
        r_width_delta_en.place(relx=0.55, rely=0.065, relwidth=0.3, relheight=0.4, anchor="nw")
        r_width_minus_btn = Button(resizef, text="+", command=self.width_plus, style="WC.TButton")
        r_width_minus_btn.place(relx=0.85, rely=0.065, relwidth=0.15, relheight=0.4, anchor="nw")

        self.height_delta_Var = StringVar(value="2")
        r_height_lb = Label(resizef, text="HEIGHT:", style="WC.TLabel")
        r_height_lb.place(relx=0.05, rely=0.495, relwidth=0.3, relheight=0.4, anchor="nw")
        r_height_plus_btn = Button(resizef, text="-", command=self.height_minus, style="WC.TButton")
        r_height_plus_btn.place(relx=0.4, rely=0.55, relwidth=0.15, relheight=0.4, anchor="nw")
        r_height_delta_en = Entry(resizef, textvariable=self.height_delta_Var, justify="center")
        r_height_delta_en.place(relx=0.55, rely=0.55, relwidth=0.3, relheight=0.4, anchor="nw")
        r_height_minus_btn = Button(resizef, text="+", command=self.height_plus, style="WC.TButton")
        r_height_minus_btn.place(relx=0.85, rely=0.55, relwidth=0.15, relheight=0.4, anchor="nw")
    
    def gen_exp_code(self):
        # self.gen_rel_pos()
        self.gen_code()
        flag = self.exp_code()
        self.codes = []
        if flag:
            messagebox.showinfo(title="Infos", message="Successful to Generate and Export Code.")
        else:
            messagebox.showinfo(title="Infos", message="Fail to Generate and Export Code.")
    
    def gen_rel_pos(self, superwidget=None):
        if superwidget.widget_configs["master"] != "top":
            for superwidget_p in self.showpanel.superwidget_contain:
                if superwidget_p.widget_configs["widget_name"] == superwidget.widget_configs["master"]:
                    superwidget.widget_configs["relx"] = '%.4f' % ((float(superwidget.widget_configs["x"]) - float(superwidget_p.widget_configs["x"]))/float(superwidget_p.widget_configs["w"]))
                    superwidget.widget_configs["rely"] = '%.4f' % ((float(superwidget.widget_configs["y"]) - float(superwidget_p.widget_configs["y"]))/float(superwidget_p.widget_configs["h"]))
                    superwidget.widget_configs["relw"] = '%.4f' % (float(superwidget.widget_configs["w"])/float(superwidget_p.widget_configs["w"]))
                    superwidget.widget_configs["relh"] = '%.4f' % (float(superwidget.widget_configs["h"])/float(superwidget_p.widget_configs["h"]))
                    break
        else:
            superwidget.widget_configs["relx"] = "%.4f" % (float(superwidget.widget_configs["x"])/float(self.showpanel.winfo["configs"]["w"]))
            superwidget.widget_configs["rely"] = "%.4f" % (float(superwidget.widget_configs["y"])/float(self.showpanel.winfo["configs"]["h"]))
            superwidget.widget_configs["relw"] = "%.4f" % (float(superwidget.widget_configs["w"])/float(self.showpanel.winfo["configs"]["w"]))
            superwidget.widget_configs["relh"] = "%.4f" % (float(superwidget.widget_configs["h"])/float(self.showpanel.winfo["configs"]["h"]))
        return superwidget.widget_configs

    def gen_code(self):
        # if os.name == "nt":
        #     json_filename = os.path.dirname(__file__)+"\\widgets.json"
        # else:
        #     json_filename = os.path.dirname(__file__)+"/widgets.json"
        with open("widgets.json", "r", encoding="utf-8") as f:
            template = json.loads(f.read())
            f.close()

        self.cmd_codes = []
        self.codes = []
       
        self.codes.append(template["tkhead"])
        self.codes.append("\n\n\n")
    
        self.codes.append(template["uiclass"]["class"])
        self.codes.append("\n\n")
        self.codes.append(template["uiclass"]["func"])
        self.codes.append("\n")

        for superwidget in self.showpanel.superwidget_contain:
            widget_configs = self.gen_rel_pos(superwidget)
            # widget_configs.pop("x")
            # widget_configs.pop("y")
            # widget_configs.pop("w")
            # widget_configs.pop("h")
            if superwidget.widget_type == "Label":    
                if superwidget.widget_configs["bind_key"] == "":
                    self.codes.append((template["widgets"]["Label"]["style"]+"\n"+
                                template["widgets"]["Label"]["variable"]+"\n"+
                                template["widgets"]["Label"]["define"]+"\n"+
                                template["widgets"]["Label"]["place"]+"\n").format(
                                    **widget_configs
                                    ))
                else:
                    self.cmd_codes.append((template["cmdclass"]["bindfunc"]).format(
                        funcname=widget_configs["bind_func"]
                    ))
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                    self.codes.append((template["widgets"]["Label"]["style"]+"\n"+
                                template["widgets"]["Label"]["variable"]+"\n"+
                                template["widgets"]["Label"]["define"]+"\n"+
                                template["widgets"]["Label"]["place"]+"\n"+
                                template["widgets"]["Label"]["bind"]+"\n").format(
                                    **widget_configs
                                ))

            if superwidget.widget_type == "Entry":
                if superwidget.widget_configs["bind_key"] == "" and superwidget.widget_configs["show"] == "":
                    self.codes.append((template["widgets"]["Entry"]["style"]+"\n"+
                                template["widgets"]["Entry"]["variable"]+"\n"+
                                template["widgets"]["Entry"]["define0"]+"\n"+
                                template["widgets"]["Entry"]["place"]+"\n").format(
                                    **widget_configs
                                    ))
                elif superwidget.widget_configs["bind_key"] == "" and superwidget.widget_configs["show"] != "":
                    self.codes.append((template["widgets"]["Entry"]["style"]+"\n"+
                                template["widgets"]["Entry"]["variable"]+"\n"+
                                template["widgets"]["Entry"]["define1"]+"\n"+
                                template["widgets"]["Entry"]["place"]+"\n").format(
                                    **widget_configs
                                    ))
                elif superwidget.widget_configs["bind_key"] != "" and superwidget.widget_configs["show"] == "":
                    self.cmd_codes.append((template["cmdclass"]["bindfunc"]).format(
                        funcname=widget_configs["bind_func"]
                    ))
                    self.codes.append((template["widgets"]["Entry"]["style"]+"\n"+
                                template["widgets"]["Entry"]["variable"]+"\n"+
                                template["widgets"]["Entry"]["define0"]+"\n"+
                                template["widgets"]["Entry"]["place"]+"\n").format(
                                    **widget_configs
                                    ))
                elif superwidget.widget_configs["bind_key"] != "" and superwidget.widget_configs["show"] != "":
                    self.cmd_codes.append((template["cmdclass"]["bindfunc"]).format(
                        funcname=widget_configs["bind_func"]
                    ))
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                    self.codes.append((template["widgets"]["Entry"]["style"]+"\n"+
                                template["widgets"]["Entry"]["variable"]+"\n"+
                                template["widgets"]["Entry"]["define1"]+"\n"+
                                template["widgets"]["Entry"]["place"]+"\n"+
                                template["widgets"]["Entry"]["bind"]+"\n").format(
                                    **widget_configs
                                ))
            if superwidget.widget_type == "Button":
                self.cmd_codes.append((template["cmdclass"]["cmdfunc"]).format(
                        funcname=widget_configs["cmd_func"]
                    ))
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                self.codes.append((template["widgets"]["Button"]["style"]+"\n"+
                            template["widgets"]["Button"]["variable"]+"\n"+
                            template["widgets"]["Button"]["define"]+"\n"+
                            template["widgets"]["Button"]["place"]+"\n").format(
                                **widget_configs
                            ))
            if superwidget.widget_type == "Radiobutton":
                self.cmd_codes.append((template["cmdclass"]["cmdfunc"]).format(
                        funcname=widget_configs["cmd_func"]
                    ))
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                self.codes.append((template["widgets"]["Radiobutton"]["style"]+"\n"+
                            template["widgets"]["Radiobutton"]["variable"]+"\n"+
                            template["widgets"]["Radiobutton"]["define"]+"\n"+
                            template["widgets"]["Radiobutton"]["place"]+"\n").format(
                                **widget_configs
                            ))
            if superwidget.widget_type == "Checkbutton":
                self.cmd_codes.append((template["cmdclass"]["cmdfunc"]).format(
                        funcname=widget_configs["cmd_func"]
                    ))
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                self.codes.append((template["widgets"]["Checkbutton"]["style"]+"\n"+
                            template["widgets"]["Checkbutton"]["variable"]+"\n"+
                            template["widgets"]["Checkbutton"]["define"]+"\n"+
                            template["widgets"]["Checkbutton"]["place"]+"\n").format(
                                **widget_configs
                            ))
            if superwidget.widget_type == "Labelframe":
                    # widget_configs.pop("bind_key")
                    # widget_configs.pop("bind_func")
                self.codes.append((template["widgets"]["Labelframe"]["style"]+"\n"+
                            template["widgets"]["Labelframe"]["define"]+"\n"+
                            template["widgets"]["Labelframe"]["place"]+"\n").format(
                                **widget_configs
                            ))
            if superwidget.widget_type == "Notebook":
                self.codes.append((template["widgets"]["Notebook"]["style"]+"\n"+
                            template["widgets"]["Notebook"]["define"]+"\n"+
                            template["widgets"]["Notebook"]["place"]+"\n").format(
                                **widget_configs
                            ))
            if superwidget.widget_type == "Combobox":
                if superwidget.widget_configs["bind_key"] == "":
                    self.codes.append((template["widgets"]["Combobox"]["style"]+"\n"+
                                template["widgets"]["Combobox"]["variable"]+"\n"+
                                template["widgets"]["Combobox"]["define"]+"\n"+
                                template["widgets"]["Combobox"]["place"]+"\n").format(
                                    **widget_configs
                                ))
                else:
                    self.codes.append((template["widgets"]["Combobox"]["style"]+"\n"+
                                template["widgets"]["Combobox"]["variable"]+"\n"+
                                template["widgets"]["Combobox"]["define"]+"\n"+
                                template["widgets"]["Combobox"]["place"]+"\n"+
                                template["widgets"]["Combobox"]["bind"]+"\n").format(
                                    **widget_configs
                                ))
            if superwidget.widget_type == "Spinbox":
                if superwidget.widget_configs["from"] != "" and superwidget.widget_configs["to"] != "" and superwidget.widget_configs["increment"] != "":
                    if superwidget.widget_configs["bind_key"] != "":
                        self.codes.append((template["widgets"]["Spinbox"]["style"]+"\n"+
                                    template["widgets"]["Spinbox"]["define0"]+"\n"+
                                    template["widgets"]["Spinbox"]["place"]+"\n"+
                                    template["widgets"]["Spinbox"]["bind"]+"\n").format(
                                        **widget_configs
                                    ))
                    else:
                        self.codes.append((template["widgets"]["Spinbox"]["style"]+"\n"+
                                    template["widgets"]["Spinbox"]["define0"]+"\n"+
                                    template["widgets"]["Spinbox"]["place"]+"\n").format(
                                        **widget_configs
                                    ))
                elif superwidget.widget_configs["values"] != "":
                    if superwidget.widget_configs["bind_key"] != "":
                        self.codes.append((template["widgets"]["Spinbox"]["style"]+"\n"+
                                    template["widgets"]["Spinbox"]["define1"]+"\n"+
                                    template["widgets"]["Spinbox"]["place"]+"\n"+
                                    template["widgets"]["Spinbox"]["bind"]+"\n").format(
                                        **widget_configs
                                    ))
                    else:
                        self.codes.append((template["widgets"]["Spinbox"]["style"]+"\n"+
                                    template["widgets"]["Spinbox"]["define1"]+"\n"+
                                    template["widgets"]["Spinbox"]["place"]+"\n").format(
                                        **widget_configs
                                    ))
            if superwidget.widget_type == "Treeview_tree":
                if superwidget.widget_configs["bind_key"] != "":
                    self.codes.append((template["widgets"]["Treeview"]["style"]+"\n"+
                                        template["widgets"]["Treeview"]["define1"]+"\n"+
                                        template["widgets"]["Treeview"]["place"]+"\n"+
                                        template["widgets"]["Treeview"]["bind"]+"\n").format(
                                            **widget_configs
                                        ))
                else:
                    self.codes.append((template["widgets"]["Treeview"]["style"]+"\n"+
                                        template["widgets"]["Treeview"]["define1"]+"\n"+
                                        template["widgets"]["Treeview"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Treeview_headings":
                if superwidget.widget_configs["bind_key"] != "":
                    self.codes.append((template["widgets"]["Treeview"]["style"]+"\n"+
                                        template["widgets"]["Treeview"]["define0"]+"\n"+
                                        template["widgets"]["Treeview"]["place"]+"\n"+
                                        template["widgets"]["Treeview"]["bind"]+"\n").format(
                                            **widget_configs
                                        ))
                else:
                    self.codes.append((template["widgets"]["Treeview"]["style"]+"\n"+
                                        template["widgets"]["Treeview"]["define0"]+"\n"+
                                        template["widgets"]["Treeview"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Progressbar_v":
                self.codes.append((template["widgets"]["Progressbar"]["style"]+"\n"+
                                        template["widgets"]["Progressbar"]["define1"]+"\n"+
                                        template["widgets"]["Progressbar"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Progressbar_h":
                self.codes.append((template["widgets"]["Progressbar"]["style"]+"\n"+
                                        template["widgets"]["Progressbar"]["define0"]+"\n"+
                                        template["widgets"]["Progressbar"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Scrollbar_v":
                self.codes.append((template["widgets"]["Scrollbar"]["define1"]+"\n"+
                                        template["widgets"]["Scrollbar"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Scrollbar_h":
                self.codes.append((template["widgets"]["Scrollbar"]["define0"]+"\n"+
                                        template["widgets"]["Scrollbar"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Text":
                self.codes.append((template["widgets"]["Text"]["define"]+"\n"+
                                        template["widgets"]["Text"]["place"]+"\n").format(
                                            **widget_configs
                                        ))
            if superwidget.widget_type == "Listbox":
                if superwidget.widget_configs["bind_key"] != "":
                    self.codes.append((template["widgets"]["Listbox"]["variable"]+"\n"+
                                    template["widgets"]["Listbox"]["define1"]+"\n"+
                                    template["widgets"]["Listbox"]["place"]+"\n"+
                                    template["widgets"]["Listbox"]["bind"]+"\n").format(
                                        **widget_configs
                                    ))
                else:
                    self.codes.append((template["widgets"]["Listbox"]["variable"]+"\n"+
                                    template["widgets"]["Listbox"]["define"]+"\n"+
                                    template["widgets"]["Listbox"]["place"]+"\n").format(
                                        **widget_configs
                                    ))
            if superwidget.widget_type == "Canvas":
                self.codes.append((template["widgets"]["Canvas"]["define"]+"\n"+
                                        template["widgets"]["Canvas"]["place"]+"\n").format(
                                            **widget_configs
                                        ))

        self.codes.append("\n\n")
        self.codes.append( template["cmdclass"]["class"])
        self.codes.append("\n")
        
        for s in self.cmd_codes:
            self.codes.append(s+"\n")
        self.codes.append("\n")

        self.codes.append("\n\n")
        self.codes.append("if __name__ == \"__main__\":\
                            \n\troot=Tk()\
                            \n\tapp = Application(root)\
                            \n\troot.geometry(\"{}x{}+{}+{}\")\
                            \n\troot.title(\"{}\")\
                            \n\troot.mainloop()".format(self.showpanel.winfo["configs"]["w"], \
                            self.showpanel.winfo["configs"]["h"], self.showpanel.winfo["configs"]["x"], \
                            self.showpanel.winfo["configs"]["y"], self.showpanel.winfo["configs"]["widget_label"]))

    def exp_code(self):
        file_o = filedialog.asksaveasfile(title="Save",mode="w",filetypes=[("Python file", ".py")],defaultextension=".py")
        # with open(os.path.dirname(__file__)+"/c.py", encoding="utf-8", mode="w") as file_o:

        if file_o:
            # print(file_o.encoding)
            if os.name == "nt":
                for i in self.codes:
                    file_o.write(i.encode("gb2312").decode("gb2312"))
            else:
                [file_o.write(i) for i in self.codes]
            file_o.close()
            return True
        return False


    def add_widget(self, event):
        self.showpanel.add_superwidget(event.widget["text"])

    def move_down(self):
        self.showpanel.move_widget(0, self.default_delta_size)
    def move_up(self):
        self.showpanel.move_widget(0, -1*self.default_delta_size)
    def move_left(self):
        self.showpanel.move_widget(-1*self.default_delta_size, 0)
    def move_right(self):
        self.showpanel.move_widget(self.default_delta_size, 0)

    def width_plus(self):
        self.showpanel.resize_widget(int(self.width_delta_Var.get()), 0)
    def width_minus(self):
        self.showpanel.resize_widget(-1*int(self.width_delta_Var.get()), 0)
    def height_plus(self):
        self.showpanel.resize_widget(0, int(self.height_delta_Var.get()))  
    def height_minus(self):
        self.showpanel.resize_widget(0, -1*int(self.height_delta_Var.get()))
        
if __name__ == "__main__":
    app = Tk()
    WidgetCtrlPanel(app)
    app.mainloop()

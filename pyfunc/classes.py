from tkinter import *
from tkinter.ttk import *
import tkinter as tk

class HyperLink(tk.Label):
	def __init__(self, parent, url, text=None, fg=None, cursor=None, *args, **kwargs):
		self.url = url;
		super().__init__(parent, text=(text or url),
            fg=(fg or "blue"),
            cursor=(cursor or "hand2"),
            font="Arial 9",
        *args, **kwargs)
		self.bind("<Button-1>", self.web_open);

	def web_open(self, event):
		return webbrowser.open(self.url);
  

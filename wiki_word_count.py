import re
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import StringVar, IntVar

URL = "https://en.wikipedia.org/wiki/"


class WikiWordCount:
    def __init__(self, master):
        self.master = master
        master.title("Wikipedia Word Counter")

        self.query = ""
        self.count = 0

        self.query_var = StringVar()
        self.query_var.set(self.query)
        self.count_var = IntVar()
        self.count_var.set(self.count)

        self.instructions = tk.Label(master, text="Enter a search query:")
        self.result_text = tk.Label(master, text="Count: ")
        self.count_text = tk.Label(master, textvariable=self.count_var)
        self.query_button = tk.Button(master, text="Find Count", command=self.get_count)

        vcmd = master.register(self.validate)
        self.query_entry = tk.Entry(master, validate="key", validatecommand=(vcmd, "%P"))

        self.instructions.grid(row=0, column=0)
        self.query_entry.grid(row=1, column=0)
        self.query_button.grid(row=2, column=0)
        self.result_text.grid(row=3, column=0)
        self.count_text.grid(row=3, column=1)

    def validate(self, new_query):
        """
        Validate entry widget contents
        :param new_query:
        :return:
        """
        if not new_query:
            self.query = ""
            return True
        try:
            self.query = new_query
            return True
        except ValueError:
            return False

    def get_count(self):
        """
        Set url string and parse html text
        Split for each " " then count length
        :return:
        """
        term = self.query_entry.get()
        main_url = URL + term
        url_request = requests.get(main_url)
        soup = BeautifulSoup(url_request.text, "html.parser")
        soup_text = soup.get_text()
        text_split = re.split(" ", soup_text)
        self.count = len(text_split)
        self.count_var.set(self.count)


if __name__ == '__main__':
    window = tk.Tk()
    gui = WikiWordCount(window)
    window.mainloop()

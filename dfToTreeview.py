"""
converts a pandas DataFrame to a tkinter treeview widget with a scrollbar
"""

from tkinter import * 
from tkinter.ttk import *

class DfView(Frame):
    """
    convert a pandas dataframe into a tkinter treeview widget with a scrollbar.

    parameters:
        df (DataFrame): a pandas dataframe to be converted  
        parent (tkinter widget): tkinter widget where you want the DfView to be placed
    """

    def __init__(self, df, parent=None, **kw):
        super().__init__(parent, **kw)

        self.df = df

        # treeview widget
        self.treeview = Treeview(self, show='headings', columns=list(self.df.columns))
        self.treeview.pack(side=LEFT, expand=True, fill=BOTH)

        # treeview scrollbar
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.treeview.yview)
        self.treeview.config(yscrollcommand=scrollbar.set)

        # creating columns inside treeview
        for column in self.df.columns:
            print(column)
            self.treeview.heading(
                column, 
                text=column,
                command=lambda: self.sort(column)
            )

        self.refresh()

    def refresh(self):
        #clearing the treeview before insertion of new values
        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for index, row in self.df.iterrows():
            self.treeview.insert('', 'end', index)

            for column in row.index:
                self.treeview.set(index, column, row[column])
            
    def sort(self, column):

        print(column)

        self.df.sort_values(by=column, inplace=True)
        self.refresh()

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("./example.csv")

    root = Tk()

    dfView = DfView(df, root)
    dfView.pack(fill=BOTH, expand=True)

    root.mainloop()

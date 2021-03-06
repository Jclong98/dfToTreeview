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
        self.sort_dict = {}
        for column in self.df.columns:
            self.sort_dict[column] = False
            print(column)
            self.treeview.heading(
                column, 
                text=column, 
                command=lambda c=column: self.sort(c)
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
        """called when a column name is clicked on. Depending on if it """

        if self.sort_dict[column]:
            self.sort_dict[column] = False
        else:
            self.sort_dict[column] = True

        self.df.sort_values(by=column, inplace=True, ascending=self.sort_dict[column])
        self.refresh()

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("./example.csv")

    root = Tk()

    dfView = DfView(df, root)
    dfView.pack(fill=BOTH, expand=True)

    root.mainloop()

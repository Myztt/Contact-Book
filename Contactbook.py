import sys

sys.path.insert(0, 'GUI')

import tkinter as tkinter
import db
import new

def get_contact(contact):
    """Returns a contact.

    Kryword arguements:
    contact -- First and Last name of a contact entry
    """
    entry = []

    try:
        if contact.split()[1]:
            entry.append(contact.split() [0])
            entry.append(contact.split() [1])
    except:
        entry.append('')
        entry.append(contact.split()[0])
    
    for row in db.get_entry(db.get_id(entry)):
    
def add_contact(contact):
    """Adds a contact to the database.

    Keyword arguments:
    contact -- List containing contact entry information
    """
    db.insert_entry(contact)

def remove_contact(contact):
    """Removes a contact.

    Keyword arguements:
    contact -- First and Last name of a contact entry
    """
    entry = []
    try:
        entry.append(contact.split() [0])
    except:
        entry.append('')
    
    try:
        entry.append(contact.split()[1])
    except:
        entry.append('')
     
     db.delete_entry(db.get_id(entry))
def edit_contact(entry_id, contact):
    """Edits a contact.

    Keyword arguements:
    entry_id -- rowid for contact entry
    contact -- List containing contact entry information
    """
    db.edit_entry(entry_id, contact)

def search(search_string, sort):
    """Searches the database and returns the results

    Keyword arguments:
    search_string -- (str) Search Term
    sort -- (str) Sorting method (Last Name or Zip)
    """
    return db.search_entry(search_string, sort)

if __name__ == "__main__":
    root = Tk.Tk()
    new.New_AddBookWindow(root)
    root.mainloop()
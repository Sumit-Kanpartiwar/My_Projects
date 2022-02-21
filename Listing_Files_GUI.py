from distutils.debug import DEBUG
from tkinter import *
from tkinter import ttk
import logging
logging.basicConfig(filename="File_Listing.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s") # initiate file logger
root = Tk() #initializing root frame
frm = ttk.Frame(root, padding=50)  #adding padding to frame
frm.grid() #adding grid to the frame
Path=StringVar() #ttk variable to store information given from input widget
def search_file_clicked():
    logging.info("executing search_file_clicked a command button function")
    try:
        import os
        os.chdir(Path.get())
        logging.info("changing directory to the path input by user")
        i=2
        for file in os.listdir():
            ttk.Label(frm, text=file).grid(column=0, row=i)
            i+=1   
        return i
    except Exception as e:
        logging.error("Error occured in search_file_clicked function")
        logging.exception(f"Error is {e}")
        print(e)
try:
    ttk.Label(frm, text="Please enter the path of folder from which you want to list the available files?").grid(column=0, row=0)
    ttk.Entry(frm,textvariable=Path).grid(column=0, row=1)
except Exception as e:
    logging.error("Error occured while taking input from the user")
    logging.exception(f"Error is {e}")
try:
    logging.info("trying to get files from input folder by calling search_file_clicked function")
    ttk.Button(frm, text="Get Files", command=search_file_clicked).grid(column=1, row=1)
except Exception as e:
    logging.error("Error occured while calling search_on_clicked function")
    loggig.exception(f"Error is {e}")

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
root.mainloop()
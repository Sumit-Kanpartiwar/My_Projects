from tkinter import *
from tkinter import ttk
import logging

logging.basicConfig(filename="Merging_PDF.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
root = Tk() #initializing root frame
frm = ttk.Frame(root, padding=10) #adding padding to frame
frm.grid() #adding grid to the frame
Path=StringVar() #ttk object to store information given from input widget
def done_clicked():
    """A function that uses folder path object #Path and creates list of pdfs #pdfs present in the folder"""
    logging.info("executing done_clicked function to create a list of pdfs #pdfs present in the folder ")
    import os
    os.chdir(Path.get())  #changing current directory to path given by user
    try:
        pdfs=[]
        for file in os.listdir():
            if file.endswith('.pdf'):
                pdfs.append(file)
    except Exception as e:
        logging.error("Error has happend")
        logging.exception(f"Error is {e}")

    def show_no_of_pdfs_clicked():
        """A function that displays number of pdfs present in the folder"""
        logging.info("executing show_no_of_pdf_clicked function")
        ttk.Label(frm, text=f"There are {len(pdfs)} PDF Files!").grid(column=0, row=3)
    def merg_pdf_clicked():
        """A function that calls pdf_merge function from PDF_Merge_Module to perform pdf merging operation and displays
        the status of merging process to the user
         """
        logging.info("calling pdf_merge function from PDF_Merge_Module to perform pdf merging operation ")
        try:
            import PDF_Merge_module
            PDF_Merge_module.pdf_merge(pdfs)
        except Exception as e:
            logging.error("Error occurred in PDF_Merge_Module!")
            logging.exception(f"Error is {e}")

        ttk.Label(frm, text="All PDFs merged in new file named 'combined.pdf'.You can Quit now!").grid(column=0, row=5)
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)

    logging.info("Asking user if he wants to know no. of pdf available in the folder and calling 'show_no_of_pdfs_clicked' when 'Yes' is clicked")
    try:
        ttk.Label(frm, text="Find number of PDF files present in this folder").grid(column=0, row=2)
        ttk.Button(frm, text="Yes", command=show_no_of_pdfs_clicked).grid(column=1,row=2)
    except Exception as e:
        logging.error("Error occurred!")
        logging.exception(f"Error is {e}")

    logging.info("asking user if he/she wants to merge the PDFs and calling 'merg_pdf_clicked' when 'Yes' is clicked")
    try:
        ttk.Label(frm, text="Do you want to merge all the PDF files in this folder?").grid(column=0, row=4)
        ttk.Button(frm, text="Yes", command=merg_pdf_clicked).grid(column=1, row=4)
    except Exception as e:
        logging.error("Error occurred!")
        logging.exception(f"Error is {e}")

logging.info("Asking user for the path of folder and storing the path in #Path variable")
try:
    ttk.Label(frm, text="Please enter the path of the folder from which you want to merge all PDF files").grid(column=0, row=0)
    ttk.Entry(frm,textvariable=Path).grid(column=0, row=1)
    ttk.Button(frm, text="Done", command= done_clicked).grid(column=1, row=1)
except Exception as e:
    logging.error("Error occurred!")
    logging.exception(f"Error is {e}")

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

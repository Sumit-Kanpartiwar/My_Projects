
def pdf_merge(pdfs):
    """function by which you will be able to merge all the PDF files available in current directory in a new PDf file.
     argument #pdfs is a list of pdf files
    """
    try:
        import PyPDF2
        pdf_merg_obj=PyPDF2.PdfFileMerger()
        for pdf in pdfs:
            pdf_merg_obj.append(pdf)
        f=open(r"combined.pdf",'wb')
        pdf_merg_obj.write(f)
    except Exception as e:
        print(e)
    finally:
        f.close()


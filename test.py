import fitz

   # Example: Open a PDF file
doc = fitz.open("example.pdf")  # Make sure to have an example.pdf file in the same directory
print("Number of pages:", doc.page_count)
doc.close()



#python test.py
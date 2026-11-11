# from pathlib import Path ## it is going to handle the python folder paths and handling file
# from pypdf import PdfReader  ## it is going to allow read and open and extract and access pdf meta data

# project_root = Path(__file__).resolve().parent.parent
# pdf_path = project_root / "data" / "tm1.pdf"

# #print("PDF exists:", pdf_path.exists())
# reader = PdfReader(pdf_path) #pdfreader is class that provides by the pypdf it opens the pdf and gives python access to its pages.
#print("total pdf pages: ",len(reader.pages))

# first_page_text = reader.pages[0].extract_text()
# print(first_page_text[:1000])


#here in the RAG we do retrival based on the knowledge base either it is pdf or docx some external data bases that we want to load first nothing but reading the information from the external data sources and converting into python application can process.

# here we have the data object which is nothing but we have already dicussed as already the document can be anything pdf or docx or db
#a typical Langchain document object contains two important parts page content(the actual text extracted from source) and meta data (additional information about the test such as source file name and page number document category)


#from langchain_core.documents import Document


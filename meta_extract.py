import pyPDF4 # if this module doesnt work for you either then im not crazy c:

def main():
    # Enter the location of 'ANONOPS_The_Press_Release.pdf'
    # Download the PDF if you haven't already
    filename = "LOCATION_OF_PDF"

    pdfFile = pyPDF2.PdfFileReader(file(filename,'rb'))
    data = pdfFile.getDocumentInfo()

    print("$$$$Metadata of the file$$$$")

    for metadata in data:
        print(metadata+ ":" +data[metadata])

if __name__ == '__main__':
    main()
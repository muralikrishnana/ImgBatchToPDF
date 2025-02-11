import os
import sys
import natsort
from fpdf import FPDF
from PIL import Image


def getPages():
    filesList = [file for file in os.listdir(
        './pages') if file.endswith('.png')]

    return filesList


def makePdf(pdfFileName, listPages, dir=''):
    # size of pdf
    # the below measures are px exuivalents of w and h of A4
    # unit used to create pdf is pt.
    # if required proper changes maybe made.
    width, height = [20.997333333, 29.701066667]

    if (dir):
        dir += "/"

    pdf = FPDF(unit="cm", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".png", 0, 0, width, height)

    pdf.output(dir + pdfFileName + ".pdf", "F")


if __name__ == '__main__':
    try:
        pagesList = getPages()
        pagesList = [p.strip(".png") for p in pagesList]
        pagesList.sort(key=int)
        print(pagesList)
    except:
        print("Error getting pages list. Make sure the pages directory exists.")
        sys.exit()

    if len(pagesList) == 0:
        print("Pages directory is empty. Retry after populating the pages directory.")
        sys.exit()

    print("Process started")
    try:
        makePdf("boe", pagesList, "pages")
        print("Success")
    except FileNotFoundError:
        print("The input filenames are invalide!")
    except:
        print("Some error occurred.")

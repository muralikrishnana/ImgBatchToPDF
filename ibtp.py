from fpdf import FPDF
from PIL import Image


def makePdf(pdfFileName, listPages, dir=''):
    # size of pdf
    # the below measures are px exuivalents of w and h of A4
    # unit used to create pdf is pt.
    # if required proper changes maybe made.
    width, height = [2480, 3508]

    if (dir):
        dir += "/"

    pdf = FPDF(unit="pt", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".png", 0, 0, width, height)

    pdf.output(dir + pdfFileName + ".pdf", "F")


if __name__ == '__main__':
    print("Process started")
    try:
        makePdf("test.pdf", ["a", "b"], "")
        print("Success")
    except FileNotFoundError:
        print("The input filenames are invalide!")
    except:
        print("Some error occurred.")

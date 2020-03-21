try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np
import sorting_contours
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


"""This main function for reading the certification"""


def imageToText(image):
    img = image
    # pre-process the image in order to read it properly

    # extract the information rectangle
    crop_img = img[110:1000, 15:350]

    # read the relevant info into a list
    diamond_settings = rectangleToText(crop_img)

    # return data for diamond object
    return diamond_settings


""" This function assuming that it been given the rectangle
    information. Pre-process is have been taken to extract
    the desierd rectangle
    the rectangle needs to be in size ________ X ______"""


def rectangleToText(image):
    diamond_settings = []
    level = 70

    # 1 shape extraction

    tmp_crop_img = image[level:level + 20, 0:350]
    # text reading
    tmp_text = pytesseract.image_to_string(tmp_crop_img)
    # text feature extraction
    split_text = tmp_text.split(' ')
    acronym = split_text[4][0] + split_text[5][0]
    diamond_settings.append(acronym)
    level = level + 92

    # 2 size extraction

    tmp_crop_img = image[level:level + 20, 0:350]
    # text reading
    tmp_text = pytesseract.image_to_string(tmp_crop_img)
    # text feature extraction
    split_text = tmp_text.split(' ')
    carat = caratFix(split_text[2])
    diamond_settings.append(carat)
    level = level + 20

    # 3 color grade extraction TODO

    # crop the relevant part of the picture
    tmp_crop_img = image[level:level + 20, 0:350]
    height, width = tmp_crop_img.shape[:2]

    # picture before picture pre-processing
    cv2.imshow("cropped", tmp_crop_img)
    cv2.waitKey(0)

    # enlarge the picture and threshold it
    tmp_resize = cv2.resize(tmp_crop_img, (round(width * 4), round(height * 4)),
                            interpolation=cv2.INTER_AREA)
    thresh = cv2.threshold(tmp_crop_img,127,255,cv2.THRESH_BINARY)
    cv2.imshow("cropped", thresh)

    tmp_text1 = pytesseract.image_to_string(thresh)
    cv2.waitKey(0)

    # text reading enhancing reading ability

    tmp_text = pytesseract.image_to_string(tmp_resize)
    # text feature extraction
    print(tmp_text)
    split_text = tmp_text.split(' ')
    color = colorFix(split_text[0])
    diamond_settings.append(color) # TODO - not reading well
    level = level + 20

    # 4 clarity grade extraction TODO - not reading well

    tmp_crop_img = image[level:level + 20, 0:350]
    # text reading
    tmp_text = pytesseract.image_to_string(tmp_crop_img)
    cv2.imshow("cropped", tmp_crop_img)
    cv2.waitKey(0)
    # text feature extraction
    split_text = tmp_text.split(' ')
    print(split_text[3])
    diamond_settings.append(split_text[2])
    level = level + 20

    # 5 cut grade extraction

    tmp_crop_img = image[level:level + 20, 0:350]
    # text reading
    tmp_text = pytesseract.image_to_string(tmp_crop_img)
    cv2.imshow("cropped", tmp_crop_img)
    cv2.waitKey(0)
    # text feature extraction
    split_text = tmp_text.split(' ')
    cut = cutFix(split_text[3])
    diamond_settings.append(cut)
    level = level + 110

    # 6 florecent grade extraction

    tmp_crop_img = image[level:level + 20, 0:350]
    # text reading
    tmp_text = pytesseract.image_to_string(tmp_crop_img)
    cv2.imshow("cropped", tmp_crop_img)
    cv2.waitKey(0)
    # text feature extraction
    split_text = tmp_text.split(' ')
    fluorescence = fluorescenceFix(split_text[1])
    diamond_settings.append(fluorescence)

    return diamond_settings


def caratFix(diamond):
    diamond_carat = float(diamond)

    if 0 <= diamond_carat <= 0.89:
        return "0.8-0.89"

    if 0.9 <= diamond_carat <= 0.99:
        return "0.9-0.99"

    if 1 <= diamond_carat <= 1.19:
        return "1-1.19"

    if 1.2 <= diamond_carat <= 1.29:
        return "1.2-1.29"

    if 1.3 <= diamond_carat <= 1.49:
        return "1.3-1.49"

    if 1.5 <= diamond_carat <= 1.69:
        return "1.5-1.69"

    if 1.7 <= diamond_carat <= 1.99:
        return "1.7-1.99"

    if 2 <= diamond_carat <= 2.24:
        return "2-2.24"

    if 2.25 <= diamond_carat <= 2.39:
        return "2.25-2.39"

    if 2.4 <= diamond_carat <= 2.69:
        return "2.4-2.69"

    if 2.7 <= diamond_carat <= 2.99:
        return "2.7-2.99"

    if 3 <= diamond_carat:
        return "3"


def colorFix(diamond):
    if diamond is "D" or "E":
        return "DE"
    if diamond is "F" or "G":
        return "FG"
    if diamond is "H" or "J":
        return "HJ"
    if diamond is "K" or "M":
        return "KM"


def cutFix(diamond):
    print("WE: " + diamond)
    if diamond is None:
        return 0
    if diamond[0] is "V":
        return 2
    if diamond[0] is "E":
        return 1


def fluorescenceFix(diamond):
    if diamond is None:
        return "NONE"
    else:
        return "FAINT"



imageToText(cv2.imread('image1.JPG'))
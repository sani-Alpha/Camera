#import cv2 for camera handling
#import pillow for image processing
import cv2
import numpy as np
from PIL import Image,ImageEnhance
class Camera:
    #to hold the final data
    global collage

    #declaring object for cv2.VideoCapture()
    cap = cv2.VideoCapture(0)

    #defining window for display
    cv2.namedWindow("Capture")

    def filters():
        #reading original image
        img0 = Image.open('image.jpg')

        #resizing the image to half of its original size
        basewidth = 350
        wpercent = (basewidth/float(img0.size[0]))
        hsize = int((float(img0.size[1])*float(wpercent)))
        img0 = img0.resize((basewidth,hsize), Image.ANTIALIAS)
        img0.save('image0.jpg')

        #creating object for image enhancement function
        en = ImageEnhance.Contrast(img0)

        #applying filters
        img1=en.enhance(1)
        img2=en.enhance(1.5)
        img3=en.enhance(2)
        img4=en.enhance(2.5)
        img5=en.enhance(3)
        img6=en.enhance(3.5)
        img7=en.enhance(4)
        img8=en.enhance(4.5)
        img9=en.enhance(5)
        img10=en.enhance(5.5)
        img11=en.enhance(6)
        img12=en.enhance(6.5)
        img13=en.enhance(7)
        img14=en.enhance(7.5)
        img15=en.enhance(8)


        #combining all the frames as one image
        collage1 = np.hstack((img1, img0, img2, img3))
        collage2 = np.hstack((img4, img5, img6, img7))
        collage3 = np.hstack((img8, img9, img10, img11))
        collage4 = np.hstack((img12, img12, img14, img15))
        collage = np.vstack((collage1, collage2, collage3, collage4))
        cv2.imshow('Collage', collage)

    def camera():
        #displaying camera feed
        while True:
            status, frame = cap.read()
            frame = cv2.flip(frame,1)
            cv2.imshow("Capture", frame)
            if not status:
                break
            k = cv2.waitKey(1)

            #key press operations
            if k%256 == 27:
                # ESC pressed
                print("Closing Camera")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "image.jpg"
                cv2.imwrite(img_name, frame)
                print("{} Saved".format(img_name))
        stop()

    def stop():
        cap.release()
        cv2.destroyAllWindows()

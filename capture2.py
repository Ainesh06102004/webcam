import time
import random
import cv2
import dropbox

starttime = time.time()


def Takephotos():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        imagename = "img" + str(number)+".png"
        cv2.imwrite(imagename, frame)
        starttime = time.time()
        result = False
    return imagename
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload(imagename):
    accesstoken = "sl.ArmSxrT82nuWp0mc_rB8afYUwY9JQkVo_50kMhToU2DZ_UawvP0uhhkeIDgcGFb9ksjZFoXQC0PJgaV0gIf2iFvV07RlzRtxxwaXMXLWWzzxnbKMIYdiHfSCA0FiV44o-8bg-V1l5m4"
    file = imagename

    fromfile = file

    tofile = "/videos" + (imagename)
    dbx = dropbox.Dropbox(accesstoken)

    with open(fromfile, 'rb') as f:
        dbx.files_upload(f.read(), tofile, mode=dropbox.files.WriteMode.overwrite)


def main():
    while(True):
        if((time.time() - starttime) >= 5):
            name = Takephotos()
            upload(name)


main()

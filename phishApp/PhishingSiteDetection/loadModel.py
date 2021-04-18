##IF USING MANNUALLY TO CHECK THEN 
## python load_model.py --model dup_not_dup.model --image test_samples/5.jpeg


from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import numpy as np
import imutils
import cv2
import base64
import os


# If you are doing it manually then please follow below instructions

# uncomment the below line and activate it !

# ap = argparse.ArgumentParser()
# ap.add_argument("-m", "--model", required=True,
# help="path to trained model model")
# ap.add_argument("-i", "--image", required=True,
#	help="path to input image")
# args = vars(ap.parse_args())


def testCase(image, url):

    flag = 0
    file = os.path.dirname(__file__) + '/siteList.txt'  # I assume you have a way of picking unique filenames

    file_open = open(file,'r')
    for line in file_open:
        line = line.strip()
        # line.find()
        print(line)
        print(url)
        if line == url:
            flag = 1
            print("Found: " + url)
            print("Data before split: " + image)
            image = str(image).split(',')
            image = image[1]
            print("Data after split: " + image)

            imgdata = base64.b64decode(image)
            print(type(imgdata))
            filename = os.path.dirname(__file__) + '/imageToSave.png'  # I assume you have a way of picking unique filenames

            with open(filename, 'w+b') as f:
                f.write(imgdata)

            img = cv2.imread(filename)
            # orig = img.copy()

            image = cv2.resize(img, (28, 28))
            image = image.astype("float") / 255.0
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)

            model = load_model(os.path.dirname(__file__)+'/dup_not_dup.model')  # in the place of dup_not_dup.model write (args['model'])

            (phished, notphished) = model.predict(image)[0]

            label = "phished" if notphished < phished else "notphished"

            proba = notphished if notphished > phished else phished

            label = "{}: {:.2f}%".format(label, proba * 100)

            return label

    if flag == 0:
        return "This site is not trained, please train it..."

    # output = imutils.resize(orig, width=400)
    #
    # cv2.putText(output, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
    #             0.7, (0, 255, 0), 2)
    #
    # cv2.imshow("Output", output)

    # cv2.waitKey(0)

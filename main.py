import sys
import getopt

import alsaaudio
import torch 
import cv2

def increase_volume(mixer:alsaaudio.Mixer, current_vol:int, sensitivity:int = 3):
    if current_vol <= 100-sensitivity:
        mixer.setvolume(current_vol + 3)
        print("Volume increased")
    else:
        print("max volume")

def decrease_volume(mixer:alsaaudio.Mixer, current_vol:int, sensitivity:int = 3):
    if current_vol >= 0 + sensitivity:
        mixer.setvolume(current_vol - 3)
        print("volume decreased")
    else:
        print("lowest volume")

def main(argv):
    sensitivity = 3
    opts, args = getopt.getopt(argv, "hi:0:", ["sensitivity="])
    for opt, arg in opts:
        if opt == '-h':
            print("main.py <sensitivity of audio change (default 3)>")
            sys.exit()
        if opt in ("-s","--sensitivity"):
            sensitivity = arg

    model = torch.hub.load("./yolov7", 'custom', "./fine_tuned_weights.pt", source='local', trust_repo=True)
    mixer = alsaaudio.Mixer()

    cap = cv2.VideoCapture(0)
    
    while True:
        current_vol = int(mixer.getvolume()[0])

        _, img = cap.read()
        result = model(img)
        result_list = result.xyxy[0].tolist()

        if len(result_list) > 0 and result_list[0][-1] == 1.0:
            increase_volume(mixer, current_vol, sensitivity)

        if len(result_list) > 0 and result_list[0][-1] == 0.0:
            decrease_volume(mixer, current_vol, sensitivity)   


if __name__ == "__main__":
    main(sys.argv[1:])
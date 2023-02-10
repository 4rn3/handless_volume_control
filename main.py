import alsaaudio
import torch 
import cv2
import numpy as np
import time

def increase_volume(mixer:alsaaudio.Mixer, current_vol:int):
    if current_vol < 97:
        mixer.setvolume(current_vol + 3)
        print("Volume increased")
    else:
        print("max volume")

def decrease_volume(mixer:alsaaudio.Mixer, current_vol:int):
    if current_vol > 3:
        mixer.setvolume(current_vol - 3)
        print("volume decreased")
    else:
        print("lowest volume")

def main():
    model = torch.hub.load("./yolov7", 'custom', "./best.pt", source='local', trust_repo=True)
    mixer = alsaaudio.Mixer()

    cap = cv2.VideoCapture(0)
    
    while True:
        current_vol = int(mixer.getvolume()[0])

        _, img = cap.read()
        result = model(img)
        result_list = result.xyxy[0].tolist()

        if len(result_list) > 0 and result_list[0][-1] == 1.0:
            increase_volume(mixer, current_vol)

        if len(result_list) > 0 and result_list[0][-1] == 0.0:
            decrease_volume(mixer, current_vol)   


if __name__ == "__main__":
    main()
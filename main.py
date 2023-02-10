import alsaaudio

def increase_volume(mixer:alsaaudio.Mixer, current_vol:int):
    mixer.setvolume(current_vol + 10)

def decrease_volume(mixer:alsaaudio.Mixer, current_vol:int):
    mixer.setvolume(current_vol - 10)

def main():
    mixer = alsaaudio.Mixer()
    current_vol = int(mixer.getvolume()[0])
    print(current_vol)
    
    if current_vol < 100:
        increase_volume(mixer, current_vol)
    else:
        print("max volume")
    
    print(int(mixer.getvolume()[0]))

if __name__ == "__main__":
    main()
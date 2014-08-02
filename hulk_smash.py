import hid
import time
import subprocess
import random

# HULK SMASH
SOUND_FILES = [
    'itsbeautiful.wav', 'smash.wav', 'talkingabout2.wav', 'waitinfor.wav',
    'snuggie.wav', 'wonagain.wav', 'partyhorn.mp3', 'choppa.mp3',
    'fireworks.mp3', 'winning.m4a',
]
DREAM_CHEEKY_VENDOR_ID = 0x1d34
HULK_SMASH_DEVICE_ID = 0x0008

def play_hulk_button():

    for d in hid.enumerate(0, 0):
        keys = d.keys()
        keys.sort()
        for key in keys:
            print "%s : %s" % (key, d[key])
        print ""

    try:
        print "Opening device"
        h = hid.device()
        h.open(DREAM_CHEEKY_VENDOR_ID, HULK_SMASH_DEVICE_ID)

        print "Manufacturer: %s" % h.get_manufacturer_string()
        print "Product: %s" % h.get_product_string()
        print "Serial No: %s" % h.get_serial_number_string()
        h.set_nonblocking(1)

        h.write([0x08] + [0x00]*6 + [0x02])
        count = 0
        button_count = 0
        while button_count < 10:
            resp = h.read(8)
            if resp:
                if resp[0] == 26:
                    print "HULK SMASH"
                    return_code = subprocess.call(
                        ["afplay", 'sounds/%s' % random.choice(SOUND_FILES)])
                    button_count += 1
            else:
                h.write([0x08] + [0x00]*6 + [0x02])
            time.sleep(.01)
            count += 1

        print "Closing device"
        h.close()

    except IOError, ex:
        print ex
        print "You probably don't have the hard coded test hid. Update the hid.device line"
        print "in this script with one from the enumeration list output above and try again."

    print "Done"

play_hulk_button()



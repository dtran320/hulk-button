#!/usr/bin/python

import datetime
import hid
import os
import random
import subprocess
import time

# HULK Button http://www.amazon.com/Smash-Button-Gadget-Dream-Cheeky/dp/B007GCAURS
DREAM_CHEEKY_VENDOR_ID = 0x1d34
HULK_SMASH_DEVICE_ID = 0x0008
HULK_BUTTON_OFF_STATE = 27
HULK_BUTTON_ON_STATE = 26

def play_hulk_button():
    """ Play awesome sounds whenever you hit the button!

    Open the HID device, send the command, listen for state changes,
    and play awesome sounds!

    """

    start_time = datetime.datetime.now()
    button_presses = 0
    for d in hid.enumerate(0, 0):
        keys = d.keys()
        keys.sort()
        for key in keys:
            print "%s : %s" % (key, d[key])
        print ""

    try:
        print "Opening device..."
        h = hid.device()
        h.open(DREAM_CHEEKY_VENDOR_ID, HULK_SMASH_DEVICE_ID)

        print "Manufacturer: %s" % h.get_manufacturer_string()
        print "Product: %s" % h.get_product_string()
        print "Serial No: %s" % h.get_serial_number_string()
        h.set_nonblocking(1)

        h.write([0x08] + [0x00]*6 + [0x02])
        
        while True:
            resp = h.read(8)
            if resp:
                if resp[0] == HULK_BUTTON_ON_STATE:
                    print "HULK SMASH"
                    button_presses += 1
                    sound = 'sounds/%s' % random.choice(os.listdir('sounds'))
                    subprocess.call(["afplay", sound])
            else:
                h.write([0x08] + [0x00]*6 + [0x02])
            time.sleep(.1)  # Not sure what the right interval to sleep for is

    except IOError as ex:
        print ex
        print "You probably don't have the Hulk button installed (or you smashed it too hard last time)."
    except KeyboardInterrupt:
        pass
    cleanup_and_exit(h, button_presses, start_time)

def cleanup_and_exit(handle, button_presses, start_time):
    print "Closing device"
    handle.close()
    print "Done smashing! Button pressed %d times since %s." % (
        button_presses, start_time)


if __name__ == "__main__":
    play_hulk_button()



Play awesome sounds whenever you push the Hulk Smash button:
http://www.amazon.com/Smash-Button-Gadget-Dream-Cheeky/dp/B007GCAURS

#Run:

**To run the program in the terminal (ends when you close the terminal):**

python hulk\_smash.py

Push the button!!!



**To run the program in the background (continues to run when the terminal is closed):**

Start the Program
./start

Press the button!

Stop the Program
./stop



#Setup:
This depends on cython-hidapi: https://github.com/trezor/cython-hidapi/
If you have trouble installing hidadpi, following the directions there to build from source.

Step 1
pip install Cython

Step 2
pip install hidapi

Step 3
Make the start and stop commands executable
chmod +x start
chmod +x stop

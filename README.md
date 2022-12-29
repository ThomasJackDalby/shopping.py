# shopping.py

shopping.py is a prototype/demonstration script to generate and print shopping lists using a barcode scanner and receipt printer.

It was developed during an afternoon hacking session to explore the concept of a "kitchen stock system" whereby a co-located barcode scanner could be utilised to keep track of depleted items and subsequently autogenerate a replenishment shopping list.

The setup included a cheap barcode scanner purchased from Amazon, and an Epson TM-88IV thermal receipt printer purchased second hand from ebay.

## Getting Started

⚠️ Note: this project has only been developed/tested on Windows. The setup process will likely be different for Mac/Linux.

First clone the project to a local folder:

``` terminal
git clone https://github.com/thomasjackdalby/shopping.py.git <target-folder>
```

Then, navigate to the cloned folder:

``` terminal
cd <target-folder>
```

Next, install required packages from PyPI using pip.

``` terminal
python -m pip install -r ./requirements.txt
```

In terms of hardware, the barcode scanner should enumerate as a keyboard device so no additional setup should be required.

Likewise, the receipt printer should enumerate over the COM port (and the correct port can be identified using Device Manager)

## Usage

Usage is fairly straightforward. First, to run the script, navigate to the containing folder and run:

``` terminal
python ./shopping.py
```

The script will then loop giving the prompt `SCAN>`, at which point if a barcode is scanned the item is logged and it's amount incremented by 1.

When the END_CODE is scanned, the shopping list is terminated and subsequently printed out via the receipt printer.

ℹ️ If the item is not in the loaded items, an additional prompt is shown allowing the user to enter a name fo the item, which is then added to the loaded items ready for subsequent scans.

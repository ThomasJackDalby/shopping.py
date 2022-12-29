# shopping.py

shopping.py is a prototype/demonstration script to generate and print shopping lists using a barcode scanner and receipt printer.

It was developed during an afternoon hacking session to explore the concept of a "kitchen stock system" whereby a co-located barcode scanner could be utilised to keep track of depleted items and subsequently autogenerate a replenishment shopping list.

The setup included a cheap barcode scanner purchased from Amazon, and an Epson TM-88IV thermal receipt printer purchased second hand from ebay.

## Getting Started

First clone the project to a local folder:

``` terminal
git clone https://github.com/thomasjackdalby/shopping.py.git <target-folder>
```

Navigate to the cloned folder, and install required packages:

``` terminal
python -m pip install -r ./requirements.txt
```

## Usage

To run the script, first navigate to the containing folder and run:

``` terminal
python ./shopping.py
```

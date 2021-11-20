# Links-Links
Project that aims to visualize coverage on certain area by optimizating the links based on the number of people on that area.  As part of Junction 2021

## Running the example
First you need to clone the repository to your own work station. Then you can start the program by running main.py. It uses packages
- pandas
- flask
- folium,

which can be installed by using the command "pip install {package}". The program should open into the default browser and if it does not, you should follow the instructions provided in the terminal.

## Layers of the example
The example visualization includes different layers. First and foremost it utilizes the datasets of the coverage of both 4G and 5G-networks. Red indicates coverage class 1, which corresponds to bad connection. Yellow then indicates class 2 and green is reserved for good, class 3 connection. Different layers can be removed or added from the drop-down menu on the right hand side. There will be similar layers for 5G than those for 4G. 

Additionally, we have utilized the data of travelers between postal codes. Layer "Postal code area" shows the how much there is travel to each postal code. The unit of travel has been normalized such that the postal code with most travel has value 1. As one might guess the highest amount of traffic occurs at 00100. It has been left out from the data, as the sole outlier skews the color gradient badly. The scale is still the same, as indicated in the legend.

As a completely new addition to the data provided by folks at Elisa, we also included some off-the-record locations of cell towers. They can be switched on and off from by the layer "Cell site". As there are quite a few of them, you will only find the exact locations by zooming in quite a bit.


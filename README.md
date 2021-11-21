# Links-Links
Project that aims to visualize coverage on certain area by optimizating the links based on the number of people on that area. As part of Junction 2021

## Running the example
First you need to clone the repository to your own work station. Then you can start the program by running main.py. It uses packages
- pandas
- flask
- folium,

which can be installed by using the command "pip install {package}". The program should open into the default browser and if it does not, you should follow the instructions provided in the terminal.

## Layers of the example
The example visualization includes different layers. First and foremost it utilizes the datasets of the coverage of both 4G and 5G-networks. Red indicates coverage class 1, which corresponds to bad connection. Yellow then indicates class 2 and green is reserved for good, class 3 connection. Different layers can be removed or added from the drop-down menu on the right hand side. There will be similar layers for 5G than those for 4G.

Additionally, we have utilized the data of travelers between postal codes. Layer "Postal code area" shows the how much there is travel to each postal code. The unit of travel has been normalized such that the postal code with most travel has value 1. As one might guess the highest amount of traffic occurs at 00100. It has been left out from the data, as the sole outlier skews the color gradient badly. The scale is still the same, as indicated in the legend.

We have also used the travel data given to visualize the change of travellers on the postcodes both monthly to describe the people leaving the metropolitan area during the summer and daily to describe change of activity on workdays compared to holidays. These are precented as relative change.

As a completely new addition to the data provided by folks at Elisa, we also included some off-the-record locations of cell towers. They can be switched on and off from by the layer "Cell site". As there are quite a few of them, you will only find the exact locations by zooming in quite a bit.


There are also examples of the possible savings that could be achieved by using a solution that would enable to turn the base stations to sleep mode when the traffic in the area decreases. The savings are calculated quite roughly by taking the traffic in the postcodes in a certain timespan and comparing it to a different point in time. We've taken this to describe the varying amount of people the network has to serve, and we have assumed that this is linearly dependent to power savings that could be achived by turning off the stations.

We used the values found in web sources to calculate the following values. These values might not be true for every case and the sources seemed to contradict each other on some points, but these are just examples to see how the visualization could be used. The base stations save 90% of the energy while turned to sleep mode. The energy used by base stations is 85% of the energy used by the network and energy consumption of the network is 30% (20%-40%) the operating cost of the network operator.
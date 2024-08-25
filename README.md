# yamlResourceComparer
Simple ptyhon script to compare attributes under two different yamls

install:

pip install pyyaml


run:

python yamldiff.py --fyp <second_file_path.yaml> --syp<second_file_path.yaml>

<br/>--fyp [string] :  first yaml file path
<br/>--syp [string] : second yaml file path
<br/>--fr [string] : first file root element - optional
<br/>--sr [string] : second file root element - optional
<br/>--fcrsf [boolean] : clear root sufixes on first file - optional
<br/>--scrsf [boolean] : clear root sufixes on second file - optional

examples: 

python yamldiff.py test.yaml test2.yaml --fre para --sre para --fcrsf --scrsf

python yamldiff.py test.yaml test2.yaml --fre para --sre para


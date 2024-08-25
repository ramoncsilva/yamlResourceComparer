# yamlResourceComparer
Simple ptyhon script to compare attributes under two different yamls

install:

pip install pyyaml


run:

python yamldiff.py --fyp <second_file_path.yaml> --syp<second_file_path.yaml>

--fyp [string] :  first yaml file path
--syp [string] : second yaml file path
--fr [string] : first file root element - optional
--sr [string] : second file root element - optional
--fcrsf [boolean] : clear root sufixes on first file - optional
--scrsf [boolean] : clear root sufixes on second file - optional

examples: 

python yamldiff.py test.yaml test2.yaml --fre para --sre para --fcrsf --scrsf

python yamldiff.py test.yaml test2.yaml --fre para --sre para


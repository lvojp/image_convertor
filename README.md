# image_convertor
This project consists of ```image_convertor.py``` that converts horizontal and vertical images to a specified resolution, and ```border_maker.py``` that adds border lines to images mainly for Instagram.

## Getting Started

### Case1: Use poetry
Install Poetry and command ```poetry install```

(Introduction | Documentation | Poetry - Python dependency management and packaging made easy
https://python-poetry.org/docs/)


### Case2: Use pip
Install packages from requirements.txt
```pip install -r requirements.txt```

### Run the program

You use poetry then run the command ```poetry run python src/image_convertor.py```
or ```poetry run python src/border_maker.py``` 

You use pip then run the command ```python src/image_convertor.py```
or ```python src/border_maker.py```

Specify the target directory with -d when using either program. 
For example ```python src/image_convertor.py -d ./images```
See help with -h for more options.

## License
This software is released under the MIT License, see ```LICENSE.txt```

# Album to Wordcloud
Takes any album link starting with "https://genius.com/albums/" and generates a wordcloud composed of all the words used in all songs on the album. The wordcloud also attempts to match the shaping and coloring of the album cover.

## Example:
The Miseducation of Lauryn Hill:  
![The Miseducation of Lauryn Hill](https://github.com/sopwithcamel110/AlbumToWordcloud/blob/master/examples/laurynhill.png?raw=true)

# How to run

## Create a virtual environment
1. Start by navigating to the project directory
2. Create the virtual environment
```console 
python3 -m venv ./venv
```
3. Activate the virtual environment
```console 
/venv/Scripts/activate.bat
```
## Install dependencies
```console 
pip install -r requirements.txt
```
## Start the Program
1. Run "python3 albumwordcloud.py"
2. Follow the printed instructions
3. The wordcloud will be saved in the "cloud.png" file in the local directory, and will also pop up using matplotlib.

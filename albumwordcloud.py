import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud, ImageColorGenerator
from bs4 import BeautifulSoup
import requests
from io import BytesIO

if __name__ == "__main__":
    url=input("Enter genius album url: ")
    while True:
        try:
            albumRequest = requests.get(url) 
            if ("genius.com/albums" not in url):
                raise Exception()
            break
        except:
            url=input("Invalid website detected, please enter an album url from genius.com: ")
    print("Loading...")
    # Total stores the entire string of words.
    text = ""
    # Parse album page on Genius.
    albumRequest = requests.get(url)
    albumSoup = BeautifulSoup(albumRequest.text, 'html.parser')
    # Try to scrape album art off page.
    try:
        imgUrl = albumSoup.find('img', attrs={'class':'cover_art-image'}).get('src')
        imgResponse = requests.get(imgUrl)
        img = Image.open(BytesIO(imgResponse.content))
    except:
        imgUrl = input("Image could not be found automatically, enter image url: ")
        imgResponse = requests.get(imgUrl)
        img = Image.open(BytesIO(imgResponse.content))
    # Go through each song link, scraping lyrics only.
    albumSoup.find_all('a', attrs={"class": "u-display_block"})
    for song in albumSoup.find_all('a', attrs={"class": "u-display_block"}):
        songRequest = requests.get(song.get("href"))
        songSoup = BeautifulSoup(songRequest.text, 'html.parser')
        lyricsBase = songSoup.find('div', attrs={'data-lyrics-container': 'true'})
        if (lyricsBase != None):
            print("Reading " + songSoup.title.text)
            for line in list(lyricsBase.stripped_strings):
                if '[' not in line: # Filter out "[Verse]" and other identifiers.
                    text += line.lower() + " "

    print("Creating wordcloud...")
    # Convert image to np array.
    cover_color = np.array(img)
    # Create shape mask.
    mask = cover_color.copy()
    edges = np.mean([gaussian_gradient_magnitude(cover_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
    mask[edges > .08] = 255
    # Create and initialize wordcloud.
    wc = WordCloud(max_words=2000, mask=mask, max_font_size=40, random_state=42, relative_scaling=0)
    wc.generate(text)
    # plt.imshow(wc)

    # Create color mask.
    image_colors = ImageColorGenerator(cover_color)
    wc.recolor(color_func=image_colors)

    wc.to_file("cloud.png")

    plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation="bilinear")
    """
    plt.figure(figsize=(10, 10))
    plt.title("Original Image")
    plt.imshow(cover_color)

    #plt.figure(figsize=(10, 10))
    #plt.title("Edge map")
    #plt.imshow(edges)
    """
    plt.show()
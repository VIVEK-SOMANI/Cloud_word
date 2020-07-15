#CloudWord project for black and white custom images of different shape or rectangle shape 
#I have used a batman black and white logo and a cloud image for shape
#I have used my whatsapp chat, Avengers:Endgame and batman Script for experiment of text

from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import io

#content related
text= io.open('endgame.txt', mode = "r", encoding ="UTF-8").read()
stopword=set(STOPWORDS)


#appearence related 
# to have rectangle shape commment line no. 13 and remove "mask = custom_mask " in line no.16
custom_mask=np.array(Image.open('batman.png'))
wc = WordCloud(background_color = 'yellow',
				max_words=100,contour_width=10,contour_color='black', max_font_size=100,
				stopwords=stopword, mask = custom_mask )
wc.generate(text)
colours=ImageColorGenerator(custom_mask)

wc.recolor(color_func = colours)  #to have colourful words comment this line.  

#plotting
 
plt.imshow(wc,interpolation = 'bilinear')
plt.axis('off')
plt.show()


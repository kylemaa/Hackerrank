import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


def _upload():

    _upload_widget = fileupload.FileUploadWidget()
    
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 ** 10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

# _upload()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    # lower the words in the file
    file_contents = file_contents.lower()
    # remove the punctuations in the file
    file_contents = file_contents.translate(
        {ord(i): None for i in punctuations})
    # dictionary that count each word
    count = {}
    for word in file_contents.split():
        if word in uninteresting_words:
            continue
        if word.isalpha():
            if word not in count:
                count[word] = 0
            count[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(count)
    return cloud.to_array()


some_content = 'Buy the ticket, take the ride. When the going gets weird, the weird turn pro. We were somewhere around Barstow on the edge of the desert when the drugs began to take hold. I hate to advocate drugs, alcohol, violence, or insanity to anyone, but they ve always worked for me. The Edge... there is no honest way to explain it because the only people who really know where it is are the ones who have gone over. A man who procrastinates in his choosing will inevitably have his choice made for him by circumstance. Faster, faster, faster, until the thrill of speed overcomes the fear of death.In a closed society where everybodys guilty, the only crime is getting caught. In a world of thieves, the only final sin is stupidity.I wouldnt recommend sex, drugs or insanity for everyone, but theyve always worked for me. If youre going to be crazy, you have to get paid for it or else youre going to be locked up.'
myimage = calculate_frequencies(some_content)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()

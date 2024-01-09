# Sentimental Analysis in Python (NLTK-Free)

This repository contains a Python script for sentimental analysis without utilizing NLTK libraries. The entire code has been manually written to perform sentimental analysis on English language text.

## How it Works

1. The script starts by reading the content present in the 'read.txt' file. The file can contain any English language text. The use of `# encoding` is employed to read data encoded in a specific format, commonly found in internet blogs.

2. Based on the content of 'read.txt', the script identifies main keywords representing emotions. These keywords are selected by comparing them with the keywords present in the 'emotion.txt' file.

3. The 'emotion.txt' file contains key-value pairs associating emotional words with the emotions they represent. Using this file, the script calculates the number of occurrences for each emotion.

4. Utilizing the `matplotlib` library, the script generates a graphical representation, such as a bar graph, depicting the frequency of each emotion. This graph provides insights into the predominant sentimental emotion expressed in the given text.

## How to Use

1. Ensure you have Python installed.
2. Clone this repository: `git clone https://github.com/Kouser3485/Sentimental-Analysis`
3. Navigate to the repository: `cd Sentimental-Analysis `
4. Run the script: `python sentiment.py`

Feel free to explore the code, modify it according to your needs, and gain insights into the emotional content of different texts.

Happy analyzing emotions! 📊

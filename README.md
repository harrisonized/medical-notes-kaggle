# Classifying Medical Notes

This is past Kaggle competition, found [here](https://www.kaggle.com/c/medical-notes).

The prompt is to take medical notes and classify them into one of five clinical domains. The notes are stored in individual text files, and Kaggle has specified that the models should be trained on 1001.txt through 1826.txt and tested on 1827.txt through 2239.txt. Since only the training set has been labeled, the model accuracy cannot be determined using the provided test set, so the provided training set must be used for train and test.

I had two goals in doing this project:

1. Since I had already written a text-classifier (available [here](https://github.com/harrisonized/yelp-climbing-gyms)), I wanted to see if I can simply swap out the data and get a classifier up and running quickly.
2. I wanted to gain some familiarity with MongoDB.

The order of operations for the notebooks is as follows:

1. convert-text-to-json.ipynb
2. eda.ipynb
3. classify-notes.ipynb

Here are some quick conclusions:

1. Without much massaging and cleaning of the data, training on the section-text only gave a micro-average training accuracy of 92% and micro-average test accuracy of 69%.
2. Without much massaging and cleaning of the data, training on the headers only gave a micro-average training accuracy of 78% and a micro-average test accuracy of 49%.
3. Training on headers, section-text, and some numerical features like section-text length and number of section headers performed exactly the same as training on section-text alone. This means the headers are redundant to the section text when they contain meaningful information.

To improve the model, there are two paths forward:

1. Pick a better classifier than logistic regression
2. Perform better preprocessing (eg. standardize all the words, remove punctuation, etc.)

For more information, please feel free to email me directly at [harrison.c.wang@gmail.com](mailto:harrison.c.wang@gmail.com) with any questions.


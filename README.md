# Classifying Medical Notes

This is past Kaggle competition, found [here](https://www.kaggle.com/c/medical-notes).

The purpose of this project is to take medical note samples and classify them into one of five clinical domains. The clinical notes are stored in individual text files, and Kaggle has specified that the models should be trained on 1001.txt through 1826.txt and tested on 1827.txt through 2239.txt. Since only the training set has been labeled, the model accuracy cannot be determined using the provided test set, so the provided training set must be used for train and test.

To be able to easily access the data, I converted the data from individual text files to JSON format, added the labels, and then stored them into MongoDB for easy access.

This is a current project. For more information, please feel free to [email me](mailto:harrisonized@gmail.com) with any questions.
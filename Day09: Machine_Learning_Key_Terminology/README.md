## Machine Learning

Machine Learning is a part of Artificial Intellingence in which the learning computer algorithms improves the machine/model through the experience and use of the data. Machine learning algorithms build a model based on available data, known as `training data`, in order to make predictions or decisions without being explicitly programmed to do so. Once the model is trained, the performance is checked on the `testing data`. Machine learning algorithms are used in a wide variety of applications, such as in medicine, text classsification, speech recognition, and Computer Vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.

### Fetures And Label/Target

Features are the input variable that is used to train the model. Features can be any form of data i.e., vector of image pixels, recorded medical data, sample text or para for text classification and so on. Whereas Label/ Target is the output variable that is obtained after the predicition of model. The label could be the sale prediction for future month, Image classsification i.e., identifying what image the model had predicted, Sentiment analysis of the text and so on. We shall look lots of features and label examples in the ongoing course. 

Machine learning is basically is divided into 3 types: Supervised Learning, Unsupervised Learning and Reinforcement Learning.


[![ml](https://www.researchgate.net/publication/329533120/figure/fig1/AS:702267594399761@1544445050584/Supervised-learning-and-unsupervised-learning-Supervised-learning-uses-annotation.png)](https://www.researchgate.net/figure/Supervised-learning-and-unsupervised-learning-Supervised-learning-uses-annotation_fig1_329533120)
Image Credits: [researchgate.net](https://www.researchgate.net/figure/Supervised-learning-and-unsupervised-learning-Supervised-learning-uses-annotation_fig1_329533120)

### Supervised Learning

Supervised learning is a machine learning approach that’s defined by its use of labeled datasets. These datasets are designed to train algorithms into classifying data or predicting outcomes accurately. Using labeled inputs and outputs, the model can measure its accuracy and learn over time.

Supervised consists of Regression and Classification learning algorthims which we shall look into detail while discussing individual algorithms. 

### Unsupervised Learning

Unsupervised learning uses machine learning algorithms to analyze and cluster unlabeled data sets. These algorithms discover hidden patterns in data without the need for human intervention.

Unsupervised consists of Clustering and Dimensionality reduction learning algorthims, even this will be covered in detail. 

### Reinforcement Learning

Reinforcement learning (RL) is an area of machine learning concerned with how intelligent agents ought to take actions in an environment in order to maximize the notion of cumulative reward. Reinforcement learning is one of three basic machine learning paradigms, alongside supervised learning and unsupervised learning. Reinforcement learning requires clever exploration mechanisms; randomly selecting actions, without reference to an estimated probability distribution, shows poor performance. The case of (small) finite Markov decision processes is relatively well understood. However, due to the lack of algorithms that scale well with the number of states (or scale to problems with infinite state spaces), simple exploration methods are the most practical.

### Supervised vs. unsupervised learning

Choosing the right approach for your situation depends on how your data scientists assess the structure and volume of your data, as well as the use case. To make your decision, be sure to do the following:

- Evaluate your input data: Is it labeled or unlabeled data? Do you have experts that can support additional labeling?
- Define your goals: Do you have a recurring, well-defined problem to solve? Or will the algorithm need to predict new problems?
- Review your options for algorithms: Are there algorithms with the same dimensionality you need (number of features, attributes or characteristics)? Can they support your data volume and structure?

### Variance, Bias, Overfitting and Underfitting

Bias: Difference between the average prediction and the correct value.
Variance: The amount that the prediction will change if different training data sets were used.
Low Bias: KNN, DT, SVM
High Bias: Logistic, Linear

Low Variance models: Linear Regression and Logistic Regression.
High Variance models: k-Nearest Neighbors (k=1), Decision Trees and Support Vector Machines.

Overfitting: It is a Low Bias and High Variance model. Generally, Decision trees are prone to Overfitting.
Underfitting: It is a High Bias and Low Variance model. Generally, Linear and Logistic regressions are prone to Underfitting.

### What are the problems associated with different Bias - Variance combinations?

High Bias - Low Variance (Underfitting): Predictions are consistent, but inaccurate on average. This can happen when the model uses very few parameters.
High Bias - High Variance: Predictions are inconsistent and inaccurate on average.
Low Bias - Low Variance: It is an ideal model. But, we cannot achieve this.
Low Bias - High Variance (Overfitting): Predictions are inconsistent and accurate on average. This can happen when the model uses a large number of parameters.

[Overfitting are like toppers
Underfitting are like backbenchers
Optimized are like me, who reads what is required and score good marks.
]

[![variance_bias](https://miro.medium.com/max/1400/1*vWklmX52_mHDC40zd7JPjg.png)](https://medium.com/analytics-vidhya/difference-between-bias-and-variance-in-machine-learning-fec71880c757)
Image Credits: [medium.com](https://medium.com/analytics-vidhya/difference-between-bias-and-variance-in-machine-learning-fec71880c757)

### How to address High Variance or High Bias?

#### High Variance is due to a model that tries to fit most of the training dataset points making it complex. Consider the following to reduce High Variance:
- Reduce input features(because you are overfitting)
- Use less complex model
- Include more training data
- Increase Regularization term

#### High Bias is due to a simple model. Consider the following to reduce High Bias:
- Use more complex model (Ex: add polynomial features)
- Increase input features
- Decrease Regularization term

### What is Bias-Variance Trade-Off?

To increase the accuracy of Prediction, we need to have Low Variance and Low Bias model. But, we cannot achieve this due to the following:
Decreasing the Variance will increase the Bias
Decreasing the Bias will increase the Variance

### Reference:

- [Wikipedia](https://en.wikipedia.org/wiki/Supervised_learning)
- [Medium](https://medium.com/analytics-vidhya/difference-between-bias-and-variance-in-machine-learning-fec71880c757)
- [Geeksforgeeks](https://www.geeksforgeeks.org/bias-vs-variance-in-machine-learning/)
- [IBM](https://www.ibm.com/cloud/blog/supervised-vs-unsupervised-learning)

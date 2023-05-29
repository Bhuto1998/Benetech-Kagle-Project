# Initial Planning

Below I will list my initial planning for the project. It is clear that we have list of images which can be of 4(5) types, goal is to find out the content of each image. For now I am dividing the problem into two parts:

## Project Phases

I will divide the probelm into two sub probelms, first is identifying the image type (classification problem), then training separate models for each image types to get the content of the images.

### Phase-1

* Divide the train data in 40% test and 60% train
* On the 60% train data, build 3 different classification models and check which one perform best.
  * ResNet based model
  * Simple CNN based classification model
  * Placeholder
* Now use the test data to make sure we are getting the results we expected in terms of classification
* Document the results and decide on which model you want to use and give reason on why you want it.

### Phase-2

* Build different models for each image type
* Perform research on what are benchmark models that can be leveraged for this problem.

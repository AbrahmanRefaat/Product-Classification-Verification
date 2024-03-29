import os
import numpy as np
from keras.applications import MobileNet
from keras.applications.mobilenet_v2 import preprocess_input
from keras.utils import load_img, img_to_array
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# model_vgg16 = VGG16(weights='imagenet', include_top=False) # 97
model_MobileNet = MobileNet(weights='imagenet', include_top=False)  # 100


def extract_features(images):
    features = []
    for img_path in images:
        img = load_img(img_path, target_size=(224, 224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features.append(model_MobileNet.predict(x).flatten())
    return np.array(features)


num_classes = 20
train_images = []
train_labels = []
validation_images = []
validation_labels = []

for i in range(1, num_classes + 1):
    train_dir = "Product Classification/" + str(i) + "/Train"
    validation_dir = "Product Classification/" + str(i) + "/Validation"
    class_name = str(i)

    for filename in os.listdir(train_dir):
        if filename.endswith('.png'):
            img_path1 = os.path.join(train_dir, filename)
            train_images.append(img_path1)
            train_labels.append(class_name)

    for filename in os.listdir(validation_dir):
        if filename.endswith('.png'):
            img_path2 = os.path.join(validation_dir, filename)
            validation_images.append(img_path2)
            validation_labels.append(class_name)

train_features = extract_features(train_images)
validation_features = extract_features(validation_images)

logistic_regression = LogisticRegression()
logistic_regression.fit(train_features, train_labels)
train_predictions = logistic_regression.predict(train_features)
train_accuracy = accuracy_score(train_labels, train_predictions)
validation_predictions = logistic_regression.predict(validation_features)
accuracy = accuracy_score(validation_labels, validation_predictions)

print(f"\n\033[92mValidation Predictions: {validation_predictions} \033[0m")
print(f"\033[94mAccuracy Logistic Regression on train data: {train_accuracy} \033[0m")
print(f"\033[94mAccuracy Logistic Regression on validation data: {accuracy} \033[0m \n")

svm_model = SVC(kernel='linear', C=1, probability=True)
svm_model.fit(train_features, train_labels)
train_predictions2 = svm_model.predict(train_features)


train_accuracy2 = accuracy_score(train_labels, train_predictions2)
svm_predictions = svm_model.predict(validation_features)
svm_accuracy = accuracy_score(validation_labels, svm_predictions)

print(f"\n\033[92mSVM Predictions: {svm_predictions} \033[0m")
print(f"\033[94mAccuracy SVM on train data: {train_accuracy2} \033[0m")
print(f"\033[94mAccuracy SVM on validation data: {svm_accuracy} \033[0m\n")

test_images = []
test_labels = []


def test_data():
    for i in range(1, num_classes + 1):
        class_name = str(i)
        test_dir = "Test Classification/" + class_name
        for filename in os.listdir(test_dir):
            #if filename.endswith('.jpg'):
                img_path3 = os.path.join(test_dir, filename)
                test_images.append(img_path3)
                test_labels.append(class_name)

    print(len(test_images), test_images)
    test_features = extract_features(test_images)
    test_predictions = logistic_regression.predict(test_features)
    accuracy1 = accuracy_score(test_labels, test_predictions)
    print(f"\n\033[92mtest Predictions: {test_predictions} \033[0m")
    print(f"\033[94mAccuracy Logistic Regression on test data: {accuracy1} \033[0m")

    svm_predictions_test = svm_model.predict(test_features)
    accuracy2 = accuracy_score(test_labels, svm_predictions_test)
    print(f"\n\033[92mSVM Predictions: {svm_predictions_test} \033[0m")
    print(f"\033[94mAccuracy SVM on test data: {accuracy2} \033[0m")

if __name__ == '__main__':
    test_data()

# EuroSat-Satellite-CNN
Performing Convolution Neural Network and Data Augementation on EuroSat Satellite dataset.

### Dataset Info

This dataset contains images belonging to the EuroSat dataset. There are 2 folders, namely,

EuroSAT → Contains RGB images collected from the Sentinel Dataset.
EuroSATallBands → Contains .tif files which have all the bands of the spectrum as collected from the Sentinel-2 satellite.
Each image is 64x64 pixels with a Ground Sampling Distance of 10m. They were all collected from the Sentinel-2 satellite

The 2 directories containing the following class folders :

![Screenshot from 2022-07-27 23-31-05](https://user-images.githubusercontent.com/66197713/181341086-fea55b68-6c0e-43f6-93ad-ec9ba9075bc7.png)


- AnnualCrop
- Forest
- HerbaceousVegatation
- Highway
- Industrial
- Pasture
- PermanentCrop
- Residential
- River
- SeaLake

Download: [Kaggle Eurosat Dataset](https://www.kaggle.com/datasets/apollo2506/eurosat-dataset)

### Visualize Training Images

![Screenshot from 2022-07-27 23-30-22](https://user-images.githubusercontent.com/66197713/181340958-51f7c061-5fcb-4480-a325-a83abb9fee09.png)

### Convolution Neural Network and Data Augmentation

```py

data_augmentation = tf.keras.Sequential([
  layers.RandomFlip("horizontal_and_vertical"),
  layers.RandomRotation(0.2),
])

model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.RandomZoom(.5, .2),
  #data_augmentation,
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(16, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(16, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10,activation="softmax")
])
```

### Performance

```py
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = history.epoch

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
```

Total params: 26,698
Trainable params: 26,698
Non-trainable params: 0

### Predictions

```py
plt.figure(figsize=(20,8))
for images, labels in test_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3,3,i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(f"\n Actual:{class_names[labels[i]]} \n Prediction:{class_names[np.argmax(prediction[i])]}")
        plt.axis("off")
```

![Screenshot from 2022-07-27 23-33-50](https://user-images.githubusercontent.com/66197713/181341579-7d9f87ce-710f-466a-8123-f33a997227e4.png)


from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))#, data_format = 'channels_first'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))#, data_format = 'channels_first'))

model.add(Conv2D(32, (3, 3)))#, data_format = 'channels_first'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))#, data_format = 'channels_first'))

model.add(Conv2D(64, (3, 3)))#, data_format = 'channels_first'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))#, data_format = 'channels_first'))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('sigmoid'))
model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

batch_size = 16

train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '/content/drive/MyDrive/data/DataCapstoneDesign/Final2/train',  # this is the target directory
        target_size=(150, 150), # 150*150
        batch_size=batch_size,
        class_mode='categorical')  

validation_generator = validation_datagen.flow_from_directory(
        '/content/drive/MyDrive/data/DataCapstoneDesign/Final2/test',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='categorical')

test_generator = test_datagen.flow_from_directory(
        '/content/drive/MyDrive/data/DataCapstoneDesign/Final2/test',
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='categorical')

model.fit_generator(
        train_generator,
        steps_per_epoch=1000 // batch_size,
        validation_data=validation_generator,
        epochs=150)
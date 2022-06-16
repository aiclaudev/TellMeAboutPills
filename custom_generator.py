from keras.preprocessing.image import ImageDataGenerator

def custom_generator() :
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
    'custom_folder', # Our test data path
    target_size=(150, 150), # my_model's input is (150*150)
    batch_size=1, # 16
    class_mode='categorical') # To predict categorical class
    return test_generator

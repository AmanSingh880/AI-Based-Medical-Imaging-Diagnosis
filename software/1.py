from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Example augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    'path_to_dataset/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import sys

# Redirect stdout to a file
sys.stdout = open('output.log', 'w', encoding='utf-8')

# Define paths
img_size = 224
train_dir = 'data/chest_xray/train'
model_save_path = 'models/model_weights.keras'
log_path = 'logs/training.log'
weights_path = 'models/resnet50_weights.h5'

# Load preprocessed data
train_data = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
).flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val_data = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
).flow_from_directory(
    train_dir,
    target_size=(img_size, img_size),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Build model
base_model = ResNet50(weights=None, include_top=False, input_shape=(img_size, img_size, 3))

# Load weights manually
base_model.load_weights(weights_path, by_name=True)

for layer in base_model.layers:
    layer.trainable = False

model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Callbacks
checkpoint = ModelCheckpoint(model_save_path, save_best_only=True, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train model
history = model.fit(
    train_data,
    epochs=10,
    validation_data=val_data,
    callbacks=[checkpoint, early_stopping]
)

# Save training history
with open(log_path, 'w', encoding='utf-8') as f:
    f.write(f"Training History:\n{history.history}\n")

# Close stdout redirection
sys.stdout.close()
sys.stdout = sys.__stdout__

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Load features and labels
X = np.load("features/features.npy")
y = np.load("features/labels.npy")

print(f"✅ Loaded data successfully: X={X.shape}, y={y.shape}")

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.33, random_state=42
)


# Build a simple fully-connected neural network
model = Sequential([
    Dense(256, activation='relu', input_shape=(X.shape[1],)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(set(y)), activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Callbacks to prevent overfitting
es = EarlyStopping(patience=5, restore_best_weights=True)
mc = ModelCheckpoint("best_model.h5", save_best_only=True)

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=50,
    batch_size=16,
    callbacks=[es, mc],
    verbose=1
)

# Save final model
model.save("final_model.h5")

print("\n🎉 Training complete!")
print("✅ Best model saved as: best_model.h5")
print("✅ Final model saved as: final_model.h5")

import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras import backend as K
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import average_precision_score

# Define the Pdestre dataset
pdestre = Pdestre(root='')

# Create the custom data generators
train_generator = CustomDataGenerator(pdestre.train, batch_size=32)
query_generator = CustomDataGenerator(pdestre.query, batch_size=32)
gallery_generator = CustomDataGenerator(pdestre.gallery, batch_size=32)

# Define the ResNet50-based model architecture with an embedding layer
inputs = Input(shape=(224, 224, 3))
base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model(inputs)
x = Flatten()(x)
x = Dense(512, activation='relu')(x) # embedding layer
x = Dropout(0.5)(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
embeddings = Dense(384)(x) # update the size of the embeddings
model = Model(inputs=inputs, outputs=embeddings)

# Define the custom triplet loss function
def triplet_loss(y_true, y_pred, alpha=0.2):
    # Split the embeddings into anchor, positive and negative
    anchor, positive, negative = tf.split(y_pred, num_or_size_splits=3, axis=1)
    # Compute the pairwise distances between anchor and all samples
    pos_dist = K.sum(K.square(anchor - positive), axis=1)
    neg_dist = K.sum(K.square(anchor - negative), axis=1)
    # Compute the triplet loss
    basic_loss = pos_dist - neg_dist + alpha
    loss = K.maximum(basic_loss, 0.0)
    # Handle the case when there are no positive or negative examples in the batch
    num_positives = tf.shape(positive)[0]
    num_negatives = tf.shape(negative)[0]
    no_positives = tf.equal(num_positives, 0)
    no_negatives = tf.equal(num_negatives, 0)
    no_triplets = tf.logical_or(no_positives, no_negatives)
    loss = tf.cond(no_triplets, lambda: 0.0, lambda: loss)
    # Return the mean triplet loss
    return K.mean(loss)

# Define the custom metric function for mAP
def mean_ap(y_true, y_pred):
    return tf.py_function(average_precision_score, [y_true, y_pred], tf.float32)

# Compile the model with the triplet loss and mAP metric
model.compile(optimizer=Adam(lr=0.0001), loss=triplet_loss, metrics=[mean_ap])

# Train the model
model.fit(train_generator, epochs=20)

# Evaluate the model using the query and gallery sets
query_embeddings = model.predict(query_generator)
gallery_embeddings = model.predict(gallery_generator)
distances = np.linalg.norm(query_embeddings[:, np.newaxis, :] - gallery_embeddings[np.newaxis, :, :], axis=2)
cmc = np.zeros((len(query_generator.labels), len(gallery_generator.labels)))
for i in range(len(query_generator.labels)):
    idx = np.argsort(distances[i, :])
    matches = np.zeros(len(gallery_generator.labels))
    for j in range(1, 6):
        matches[query_generator.labels[i] == gallery_generator.labels[idx[j]]] = 1
        cmc[i, j-1] = np.sum(matches) / j
print('Rank-1 accuracy:', cmc[:, 0].mean())
print('Rank-5 accuracy:', cmc[:, 4].mean())


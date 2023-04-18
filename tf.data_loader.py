import tensorflow as tf
from tensorflow.keras.utils import Sequence
import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)


class CustomDataGenerator(Sequence):
    def __init__(self, data, batch_size=32, shuffle=True):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        
        # Define any necessary transformations here
        self.image_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            rotation_range=20,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True
        )
        
        # Get the unique labels from the data
        self.labels = set(item[1] for item in data)
        
        # Create a mapping from label to integer index
        self.label2idx = {label: idx for idx, label in enumerate(sorted(self.labels))}
        
        # Create a list of indices for the data
        self.indices = list(range(len(data)))
        
        # Shuffle the indices if required
        if shuffle:
            np.random.shuffle(self.indices)
        
    def __len__(self):
        # Return the total number of batches
        return int(np.ceil(len(self.data) / self.batch_size))
        
    def __getitem__(self, index):
        # Get the indices for the current batch
        batch_indices = self.indices[index * self.batch_size:(index + 1) * self.batch_size]
        
        # Load and preprocess the images for the current batch
        batch_inputs = []
        batch_targets = []
        for idx in batch_indices:
            image_path = self.data[idx][0]
            label = self.data[idx][1]
            
            image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
            image = tf.keras.preprocessing.image.img_to_array(image)
            image = self.image_data_generator.random_transform(image)
            image = self.image_data_generator.standardize(image)
            
            batch_inputs.append(image)
            batch_targets.append(self.label2idx[label])
        
        # Convert the inputs and targets to numpy arrays
        batch_inputs = np.array(batch_inputs)
        batch_targets = np.array(batch_targets)
        
        # Convert the targets to one-hot encoding
        batch_targets = tf.keras.utils.to_categorical(batch_targets, num_classes=len(self.labels))
        
        return batch_inputs, batch_targets

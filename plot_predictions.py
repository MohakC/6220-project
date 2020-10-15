import matplotlib.pyplot as plt 
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
import numpy as np
from net import Net

validation_data_dir = 'test/' 
test_datagen = ImageDataGenerator(featurewise_center=True, featurewise_std_normalization=True, rescale=1. / 255)
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(32, 32),
    batch_size=72000,
    class_mode='categorical',
    shuffle=False)
test_images, test_labels = validation_generator.next()
test_images = np.array(test_images)
test_labels = np.array(test_labels)
test_labels = np.argmax(test_labels,axis=1)


#initialize model
model = Net.build(width = 32, height = 32, depth = 3)
print('building done')
# Compile model
rms = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
print('optimizing done')
model.compile(loss='categorical_crossentropy',
              optimizer=rms,
              metrics=['accuracy'])
print('compiling')
validation_generator.reset()

model.load_weights('trained_weights_2.h5')
model.evaluate(validation_generator)
validation_generator.reset()

predicted_classes = model.predict(validation_generator)
predicted_classes = np.argmax(predicted_classes,axis=1)
labels = (validation_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())

correct = np.where(predicted_classes==test_labels)[0]
print("Found {} correct labels".format(len(correct)))
print("Found {} incorrect labels".format(7200-len(correct)))

for i in range(0,25):
    plt.subplot(5,5,i+1)
    random_int = np.random.randint(len(correct))
    random_index = correct[random_int]
    plt.imshow(test_images[random_index], interpolation='none')
    plt.title("Predicted {}, Class {}".format(labels[predicted_classes[random_index]], labels[test_labels[random_index]]))
    plt.tight_layout()
plt.show()
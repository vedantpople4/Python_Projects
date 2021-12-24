from keras.datasets import mnist
from keras.engine import sequential
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

(x_train , y_train),(x_test, y_test) = mnist.load_data()

num_pixels = x_train.shape[1]*x_train.shape[2]
x_train = x_train.reshape((x_train.shape[0], num_pixels)).astype('float')
x_test = x_test.reshape((x_test.shape[0], num_pixels)).astype('float')

x_train = x_train / 255
x_test = x_test / 255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
#num_classes = y_test[1]

def baseline_model():
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    model.add(Dense(y_train[1], kernel_initializer='normal', activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

model = baseline_model()
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)
scores = model.evaluate(x_test, y_test, verbose=0)
print("Baseline Error: %2f%%" % (100-scores[1]*100))
import tensorflow as tf

model = tf.keras.models.load_model('D:\Durian\model3.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("model_now_1.tflite", "wb").write(tflite_model)
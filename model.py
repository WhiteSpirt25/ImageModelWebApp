from os import EX_CANTCREAT
from tensorflow.keras.models import load_model
from tensorflow.image import resize
 
class MlModel:

    def __init__(self) -> None:
        try:
            self.model = load_model('saved_model.h5')
        except:
            self.model = None
            
    def predict(self,image):
        if self.model is not None:
            image = image.resize(image, [224,224]).numpy()
            try:
                result = self.model.predict(image)
            except:
                return "Unable to predict. Check model file or image prerocessing."
        else:
            return "Unable to load model. Check if model file exists."
import mlflow
import os
from pawpularitypipeline.preprocessing import resize
import numpy as np
 
class MlModel:

    def __init__(self) -> None:
        try:
            experiment_id = mlflow.get_experiment_by_name('Pawpularity').experiment_id
            last_run_id = mlflow.list_run_infos(experiment_id, max_results=1)[0].run_id
            self.model = mlflow.pyfunc.load_model(os.path.join('mlruns','0', last_run_id, 'artifacts', 'model'))
        except:
            self.model = None
            
    def predict(self,image):
        if self.model is not None:
            image = resize(image,240,240)
            try:
                result = self.model.predict(np.array([image]))
                return int(result[0][0])
            except:
                return "Unable to predict. Check model file or image prerocessing."
        else:
            return "Unable to load model. Check if model file exists."

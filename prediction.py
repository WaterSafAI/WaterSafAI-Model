import torch
import numpy as np


class WaterQualityPredictor:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = torch.load(model_path, map_location=self.device)
        self.model.eval()
        self.model.to(self.device)

    def prepare_input_data(self, sample_data, mean_values):
        # Replace missing values with mean values
        for key in sample_data:
            if sample_data[key] is None:
                sample_data[key] = mean_values[key]

        # Convert to numpy array and then to tensor
        input_features = np.array(list(sample_data.values()), dtype=np.float32)
        input_tensor = torch.tensor(input_features)

        # Reshape if necessary (e.g., if your model expects a specific shape)
        input_tensor = input_tensor.unsqueeze(0)  # Adds a batch dimension

        return input_tensor

    def predict(self, input_data, mean_values):
        input_tensor = self.prepare_input_data(input_data, mean_values)
        with torch.no_grad():
            input_tensor = input_tensor.to(self.device)
            output = self.model(input_tensor)
            _, predicted = torch.max(output, 1)
            return predicted.item()


# Mean values (should be set based on your training data)
mean_values = {
    "ph": 7.0,
    # Add mean values for other features if necessary
}

# Initialize the predictor with the model path
predictor = WaterQualityPredictor("model.pth")

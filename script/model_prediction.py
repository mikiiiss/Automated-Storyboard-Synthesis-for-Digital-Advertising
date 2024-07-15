import joblib
from PIL import Image
import numpy as np

# Load the model and the scaler
model = joblib.load('../model/linear_regression_model.pkl')
scaler = joblib.load('../model/scaler.pkl')

# Define the paths to the image files
cta_path = '/home/michael_george/trial/cta.png'
logo_path = '/home/michael_george/trial/logo.png'
background_path = '/home/michael_george/trial/background.png'
engagement_instruction_path = '/home/michael_george/trial/engagement_instruction.png'

# Load the images and extract the required features
cta_image = Image.open(cta_path)
cta_dimensions = cta_image.size
cta_relative_dimensions = (cta_dimensions[0] / 1920, cta_dimensions[1] / 1080)
cta_image.close()

logo_image = Image.open(logo_path)
logo_dimensions = logo_image.size
logo_relative_dimensions = (logo_dimensions[0] / 1920, logo_dimensions[1] / 1080)
logo_file_size = os.path.getsize(logo_path)
logo_image_array = np.array(logo_image)
logo_dominant_colors = [(color, count) for color, count in np.unique(logo_image_array.reshape(-1, logo_image_array.shape[2]), axis=0, return_counts=True)]
logo_image.close()

engagement_instruction_image = Image.open(engagement_instruction_path)
engagement_instruction_dimensions = engagement_instruction_image.size
engagement_instruction_relative_dimensions = (engagement_instruction_dimensions[0] / 1920, engagement_instruction_dimensions[1] / 1080)
engagement_instruction_file_size = os.path.getsize(engagement_instruction_path)
engagement_instruction_image_array = np.array(engagement_instruction_image)
engagement_instruction_dominant_colors = [(color, count) for color, count in np.unique(engagement_instruction_image_array.reshape(-1, engagement_instruction_image_array.shape[2]), axis=0, return_counts=True)]
engagement_instruction_image.close()

background_image = Image.open(background_path)
endframe_file_size = os.path.getsize(background_path)
endframe_image_array = np.array(background_image)
endframe_dominant_colors = [(color, count) for color, count in np.unique(endframe_image_array.reshape(-1, endframe_image_array.shape[2]), axis=0, return_counts=True)]
background_image.close()

# Flatten the new entry into a single list of features
new_features = [
    *cta_dimensions, *cta_relative_dimensions,
    *logo_dimensions, *logo_relative_dimensions, logo_file_size, *logo_dominant_colors,
    *engagement_instruction_dimensions, *engagement_instruction_relative_dimensions, engagement_instruction_file_size, *engagement_instruction_dominant_colors,
    endframe_file_size, *endframe_dominant_colors
]

# Standardize the new features
new_features = scaler.transform([new_features])

# Predict the positions
predicted_positions = model.predict(new_features)
print(f"Predicted frame.png positions: {predicted_positions}")
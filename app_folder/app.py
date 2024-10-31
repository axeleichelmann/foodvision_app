import streamlit as st
import PIL

import torch
import torch.nn as nn
import torchvision


st.set_page_config(page_title='Food Recognizer App',
                   layout='wide',
                   initial_sidebar_state='expanded')


# Set title of app
st.title("Food Recognizer Web App")

# Import pre-trained model tand its corresponding pre-processing transformer
model = torch.load("effnet_b0.pth")
transform = torchvision.models.EfficientNet_B0_Weights.DEFAULT.transforms()

# Create Dictionary with classes and their corresponding labels
with open("text_files/classes.txt", "r") as file:   # Read all classes into a list
    classes = file.readlines()

with open("text_files/labels.txt", "r") as file:   # Read all labels into a list
    labels = file.readlines()

class_to_label = {_class : label for label, _class in zip(labels, classes)}
label_to_class = {label : _class for label, _class in zip(labels, classes)}
idx_to_class = {i : _class for i, _class in enumerate(classes)}
idx_to_label = {i : label for i, label in enumerate(labels)}


#### Display loaded image file & predicted value

# Display uploaded image 
uploaded_file = st.file_uploader(label="Upload Image of your Food (Note : Image must be in JPG, JPEG or PNG format)",
                                 type=['jpg','jpeg','png'])
if uploaded_file:
    input_image = PIL.Image.open(uploaded_file)
    st.image(input_image, width=500)

    # Predict & Display malignant/benign value
    transformed_image = transform(input_image).unsqueeze(0)
    pred_probs = model(transformed_image).softmax(dim=1)
    pred_class = pred_probs.argmax(dim=1).item()
    st.write(f"Predicted Food : {idx_to_label[pred_class]}")

    # Add option for user to comment on correctness of the prediction
    prediction_correct = st.selectbox(label="Was this prediction correct?",
                                        options=["Yes", "No"], index=None)
    if prediction_correct=="Yes":
        st.write(f"Thank you for your feedback!")
        #logging.info(f"Correct Prediction : Predicted Class = {idx_to_class[pred_class]}")
    elif prediction_correct=="No":
        correct_label = st.text_input(label="What food does your image actually show?",
                                      value=None)
        if correct_label:
            st.write(f"Thank you for your feedback!")
            #logging.info(f"Incorrect Prediction : Predicted Class = {idx_to_class[pred_class]}, True Class = {correct_label}")
    







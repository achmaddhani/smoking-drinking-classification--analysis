'''
Phase 1 Milestone 2

Nama : Achmad Dhani

Batch : HCK-009

Objective : Creating a main page of the webapps.
'''

import streamlit as st
import eda

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Prediction Model'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write('Phase 1 Milestone 2')
    st.write('Name      : Achmad Dhani')
    st.write('Batch     : HCK-009')
    st.markdown('Dataset: [Water Quality](https://www.kaggle.com/datasets/adityakadiwal/water-potability)')
    st.write('Objective : Water is essential for all forms of life, yet its quality can vary dramatically, with the potential to sustain health or cause disease. The distinction between potable water, which is safe for consumption, and non-potable water, which poses health risks, determined by the presence of certain chemicals. By employing classification model focused on the Recall metric, we can effectively predict the potability of water, ensuring its safety for consumption.')
    st.write('')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption('The dataset used `Water Quality` is a public dataset from keggle consist of data of water samples from different water bodies. It has 3276 entries with 10 columns. The dataset also has a total of 1434 missing values')
        
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
            '''
            - Loading the data, checking for duplicated and missing values
            - EDA on the dataset to gain insights regarding the dataset and the missing value
            - Feature Engineering to prepare data for the model
            - Creating and Evaluating to get the best model
            - Deployment in Hugging Face
            
            '''
        )

#============================= Conclussion =================================
    with st.expander("Conclusion"): # conclusion
        st.caption(
            '''
            The dataset is well documented but has missing values. These missing values after exploration deemed MCAR and most likely due to the person in charge taking the water samples did not have the equipment to messure these missing values chemical levels. All the chemicals don't have a relationship with each other or a trend, and each of them are important because the PCA shows a linear relationship between number of features and the percentage of data kept. Most water sample has a ph of 5-9, has a quite high amount of chemicals like sulfate, chloramines and trihalomethanes which doesn't seem to have difference between the ones potable and non-potable. It can be assumed that the water samples are from environment that is scarce on really good drinkable water or a highly contaminated environment like a factory side of the city. The model that gives the best overall score is RandomForest which has a recall of 65% meaning, when predicting if the water is drinkable or not, it will be correct 65% of the time. There are few things to suggest for the future. The SVC model can be further searched if resources are available, there needed to be more potable water data since the data is imbalanced towards non-potable water and dataset potability validity needed to be checked by the author.
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    pass
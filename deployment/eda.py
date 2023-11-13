'''
Phase 1 Milestone 2

Nama : Achmad Dhani

Batch : HCK-009

Objective : Creating EDA page specifically to explain insights from EDA
'''

import streamlit as st
import pandas as pd
from PIL import Image

def run():
    st.title('Exploration Data Analysis Section')

    df= pd.read_csv('smoke_drink.csv') # reading CSV

#============================= Display Data ===============================
    
    with st.expander("View the top 10 entries of the original dataset"):
        st.table(df.head(10))

#============================= Correlation =====================================
    st.subheader('Smoking Type Distribution of The Dataset')
    
    # Assume you have two images
    image1 = 'smoke_dist_bar.png'
    image2 = 'smoke_dist_pie.png'
    horizontal_radio_css = """
    <style>
    div.row-widget.stRadio > div{flex-direction:row;}
    </style>
    """
    st.markdown(horizontal_radio_css, unsafe_allow_html=True)
    image_show = st.radio("**Visualization Options**", ['Bar Plot', 'Pie Chart'])
    if image_show == 'Bar Plot':
        st.image(image1, caption=f'Figure 1 Bar Plot of Smoking Type Distribution')
    else:
        st.image(image2, caption=f'Figure 2 Pie Chart of Smoking Type Distribution')

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''            
            Based on both visualization, most of the variables do not have any relationship except for a few.

            - `Hardness` has a very positive low value with `ph` in spearman but close to 0 in pearsons. This suggests there might be a very weak positive non
            linear relationship.
            - `Sulfate` with `Solids` and with `Sulfate` has a very low negative value both in spearman and pearsons. This suggests there might be a very weak
            negative linear relationship.
            '''
            )
        
#================================ ph ==========================================
    
    # st.subheader('ph Values Distribution')
    # image3 = Image.open('ph.png')
    # st.image(image3, caption='Figure 3 ph values distribution histogram',  width=600)

    # # explaination
    # with st.expander('Explanation'):
    #     st.caption(
    #         '''
    #         - The water sample taken mostly has ph between `5-9`
    #         - The visualization also suggest a lot of data are in the range for drinkable water but doesn't mean that the water is drinkable.
    #         - This could mean most water samples that's taken could come contaminated water bodies.
    #         '''
    #         )

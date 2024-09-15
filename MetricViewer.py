import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import Backend as func
from streamlit_tree_select import tree_select

st.set_page_config(
    layout='wide', page_title='GM Motorsports Metric Viewer', page_icon=func.image_dark)

with st.container():  # Hide standard Streamlit footer
    st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
    
# setup containers for page areas
with st.container():  # Setup Page Header and title with logo
    col1, col2 = st.columns([.4, .6])

    with col1:
        st.image(func.image_home, width=250)

    with col2:
        st.title("Metrics Viewer")
st.subheader("",divider='blue')

# # initialize session state variables
# if 'user_data' not in st.session_state:  # create session state variables
#     st.session_state['user_data'] = ''

# Function to load and cache the CSV data
@st.cache_data
def load_csv(uploaded_file):
    # Load the CSV into a DataFrame
    df = pd.read_csv(uploaded_file)
    return df

with st.sidebar:

    st.header("Upload Data",divider="blue")

    uploaded_files = st.file_uploader("Choose a CSV file", type={
                                        "csv"}, accept_multiple_files=False)

if uploaded_files:
    #combine all uploaded files into one
    # for file in uploaded_files:
    #     file.seek(0)
    # uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    # raw_data = pd.concat(uploaded_data_read)
    raw_data = load_csv(uploaded_files)

    #setup widget for units swap
    units_USA = st.toggle('Southern Units')

    if units_USA:
        units = 'USA'
    else:
        units = 'SI'

    #Take raw data and get list of col names and metrics
    # Initialize sets to store the split parts (sets automatically handle duplicates)
    channel_names = set()
    segments = set()
    aggregations = set()
    results_list = []

    for name in raw_data.columns:
            if '_' in name:
                parts = name.rsplit('_',2)  # Split by underscore
                
                # Add the parts to corresponding sets
                channel_names.add(parts[0])
                segments.add(parts[1])
                aggregations.add(parts[2])
            else:
                results_list.append(name)

    #If units are USA convert
    if units == 'USA':
        # Apply the conversion
        df_converted = func.convert_columns(raw_data, func.lookup, func.conversion)
    else:
        df_converted = raw_data.copy()
    
    st.dataframe(df_converted, use_container_width=True,hide_index=True)

    st.markdown("""   """)

    with st.sidebar:

        st.header("Segment Filter",divider="blue")
        # Allow user to select which Segments to filter
        selected_segments = st.multiselect(
                            'Select Segments:', segments)
                   
    if selected_segments:
        col_list = []
        col_list = df_converted.columns[df_converted.columns.str.contains('|'.join(selected_segments))].tolist()
        col_list += results_list

        #filter df to only include selected segments
        df_converted = df_converted[col_list]
        # st.dataframe(df_converted, use_container_width=True,hide_index=True)

        # Create an empty dictionary to store the results 
        result_dict = {}

        # Loop through the column names and split them
        for name in df_converted.columns:
            if '_' in name:
                parts = name.rsplit('_',2)  # Split by underscore
                
                # Add the parts to corresponding sets
                channel_names.add(parts[0])
                segments.add(parts[1])
                aggregations.add(parts[2])

                main_key = parts[0]  # The first part is the main key
                sub_key = parts[1]  # The second part is the sub key
                min_max = parts[2]  # The last part is either 'min' or 'max'

                # Initialize the main key if not present
                if main_key not in result_dict:
                    result_dict[main_key] = {}
                
                # Add the min/max to the sub_key in the nested dictionary
                if sub_key not in result_dict[main_key]:
                    result_dict[main_key][sub_key] = {}
                
                # Assign 'min' or 'max' to the corresponding sub_key
                result_dict[main_key][sub_key][min_max] = min_max

        filtered_cols = []
        
        single_entries, other_entries = func.filter_keys_with_multiple_sub_keys(result_dict)
        
        filtered_cols = func.flatten_dict_to_list(other_entries)
        with st.sidebar:
            st.header("Aggregation Filter",divider="blue")
    
            return_selected = tree_select(func.convert_to_nodes_format(single_entries),only_leaf_checkboxes=True)

        filtered_cols += return_selected['checked']
        filtered_cols += results_list

        df_filtered = df_converted[filtered_cols]

        st.header("Filtered Data",divider="blue")
        st.markdown("""   """)

        st.dataframe(df_filtered, use_container_width=True,hide_index=True)

        selected_cols = st.multiselect(
                            'Select Metrics to Filter:', df_filtered.columns)
        st.markdown("""   """)
    
        if selected_cols:
        
            #For each selected filter, add a slider for max and min and allow user to adjust
            sliders = {}
            def display_sliders():
                for col in selected_cols:
                    min_val = float(df_converted[col].min())
                    max_val = float(df_converted[col].max())
                    sliders[col] = st.slider(col, value=[min_val,max_val],min_value=min_val,max_value=max_val)
                return sliders
            
            sliders = display_sliders()

            # Filter raw_data based on sliders
            filtered_data = df_filtered.copy()
            for col, slider_range in sliders.items():
                filtered_data = filtered_data[(filtered_data[col] >= slider_range[0]) & (filtered_data[col] <= slider_range[1])]

            st.markdown("""   """)
            st.header("Resultant Data",divider="blue")

            if len(selected_cols) > 1:

                # Add Parrallel Coordinates Plot for all sliders in filtered data
                fig_par =  px.parallel_coordinates(filtered_data, 
                                    dimensions=selected_cols,
                                    color_continuous_scale=px.colors.diverging.Tealrose,
                                    color_continuous_midpoint=2)
                
                st.plotly_chart(fig_par,use_container_width=True)

            st.dataframe(filtered_data, use_container_width=True,hide_index=True)

            st.markdown("""   """)
            st.header("Data Plots",divider="blue")

            col1,col2,col3 = st.columns([0.15,0.1,0.75])

            with col1:
                col_names = filtered_data.columns.tolist()
                col_names.append(None)

                x_axis = st.selectbox('X-Axis:',col_names,index=0)

                y_axis = st.selectbox('Y-Axis:',col_names,index=1)

                c_axis = st.selectbox('Color:',col_names,index=len(col_names)-1)

            with col3:

                fig = px.scatter(filtered_data, x=x_axis, y=y_axis, color=c_axis)
                st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No Data Loaded")

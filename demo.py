import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)

if 'selected_nav' not in st.session_state:
    st.session_state.selected_nav = 0

def set_selected_nav(index):
    st.session_state.selected_nav = index
    st.rerun()  # Forces an immediate rerun

with col1:
    if st.session_state.selected_nav == 0:
        st.button("Product description", type="primary")
    else:
        if st.button("Product description"):
            set_selected_nav(0)

with col2:
    if st.session_state.selected_nav == 1:
        st.button("AI innovation LAB", type="primary")
    else:   
        if st.button("AI innovation LAB"):
            set_selected_nav(1)

with col3:
    if st.session_state.selected_nav == 2:
        st.button("Product refinement", type="primary")
    else:
        if st.button("Product refinement"):
            set_selected_nav(2)

with col4:
    if st.session_state.selected_nav == 3:
        st.button("Virtual consumer panel", type="primary")
    else:
        if st.button("Virtual consumer panel"):
            set_selected_nav(3)

with col5:
    if st.session_state.selected_nav == 4:
        st.button("Final insights", type="primary")
    else:
        if st.button("Final insights"):
            set_selected_nav(4)
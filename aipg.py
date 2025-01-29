import streamlit as st
import numpy as np
import extra_streamlit_components as stx
import time

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)


st.set_page_config(layout="wide")


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

if st.session_state.selected_nav == 0:
    st.title("Product brief")

    product_description = st.text_area("Enter product keypoints")

    product_image = st.file_uploader("Upload product idea image", type=["jpg", "jpeg", "png"])

    if product_image is not None:
        st.image(product_image, caption="Uploaded product idea image", use_column_width=True)

    st.title("Coming soon")

    st.text("Personalised your product description with brand detailes and related product sales data.")

    col1, col2 = st.columns([9, 1])
    with col2:
        if(st.button("To Innovation lab")):
            set_selected_nav(1)

if st.session_state.selected_nav == 1:
    st.title("AI inovation LAB")
    left_col, right_col = st.columns([2, 1])  
    with left_col:   
        speed = 101
    
        if 'messages' not in st.session_state:
            st.session_state.messages = [
                {"role": "user", "person":"product manager", "content": "Hi, I'm Alex, the product manager.", "avatar": "👨‍💼"},
                {"role": "user", "person":"marketing specialist", "content": "Hello, I'm Jamie, the marketing specialist.", "avatar": "👩‍💼"},
                {"role": "user", "person":"design lead", "content": "Hey, I'm Taylor, the design lead.", "avatar": "👨‍🎨"},
                {"role": "user", "person":"data analyst", "content": "Hi, I'm Jordan, the data analyst.", "avatar": "👩‍🔬"},
                {"role": "user", "person":"product manager", "content": "We need to improve our new product idea: a chocolate bar for people with allergies to milk, gluten, and eggs. Any thoughts?", "avatar": "👨‍💼"},
                {"role": "user", "person":"marketing specialist", "content": "I think we should highlight the health benefits and the fact that it's allergen-free in our marketing campaigns.", "avatar": "👩‍💼"},
                {"role": "user", "person":"design lead", "content": "Agreed. We should also make the packaging visually appealing and clearly indicate that it's allergen-free.", "avatar": "👨‍🎨"},
                {"role": "user", "person":"data analyst", "content": "From the data, we can see a growing trend in demand for allergen-free products. We should leverage this in our product positioning.", "avatar": "👩‍🔬"},
                {"role": "user", "person":"product manager", "content": "Great points. Jamie, can you work on a marketing strategy that emphasizes these benefits?", "avatar": "👨‍💼"},
                {"role": "user", "person":"marketing specialist", "content": "Sure, I'll draft a strategy that focuses on health benefits and allergen-free aspects.", "avatar": "👩‍💼"},
                {"role": "user", "person":"design lead", "content": "I'll start working on the packaging design. Any specific colors or themes we should consider?", "avatar": "👨‍🎨"},
                {"role": "user", "person":"product manager", "content": "Let's go with earthy tones to emphasize the natural ingredients.", "avatar": "👨‍💼"},
                {"role": "user", "person":"data analyst", "content": "I'll gather more data on consumer preferences for allergen-free products to support our strategy.", "avatar": "👩‍🔬"},
                {"role": "user", "person":"product manager", "content": "Perfect. Let's reconvene next week to review our progress.", "avatar": "👨‍💼"}
            ]



        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user", avatar=message["avatar"]):
                    typewriter(text=message["content"], speed=speed)




        st.subheader("Product Ideas")

        col1, col2, col3 = st.columns([1, 1, 1])  

        with col1:
            st.image("images/mango1.jpeg", caption="Coca Cola Natural Mango")
            st.markdown("""
            **Coca Cola Natural Mango**:
            - Made with real mango puree
            - No added sugar
            - Refreshing and natural taste
            """)
            if st.button("Select idea", key="idea1"):
                st.session_state.selected_idea = "Coca Cola Natural Mango"
                set_selected_nav(2)
        with col2:    
            st.image("images/mango2.jpeg", caption="Coca Cola Natural Strawberry")
            st.markdown("""
            **Coca Cola Natural Strawberry**:
            - Made with real strawberry puree
            - No added sugar
            - Refreshing and natural taste
            """)
            if st.button("Select idea", key="idea2"):
                st.session_state.selected_idea = "Coca Cola Natural Strawberry"
                set_selected_nav(2)
        with col3:    
            st.image("images/mango3.jpeg", caption="Coca Cola Natural Strawberry Mango")
            st.markdown("""
            **Coca Cola Natural Strawberry Mango**:
            - Made with real strawberry mango puree
            - No added sugar
            - Refreshing and natural taste
            """)    
            if st.button("Select idea", key="idea3"):
                st.session_state.selected_idea = "Coca Cola Natural Strawberry Mango"  
                set_selected_nav(2)              
    with right_col:
        st.subheader("Recommendations")   
        followup = """
        **Refine the Flavor Profile with Natural Ingredients**: To cater to both taste preferences and health-conscious consumers, refine the mango flavor using natural mango puree or extracts, and reduce the sugar content. This can improve the product’s authenticity and appeal to health-conscious segments, while still maintaining the refreshing Coca-Cola experience.

        **Target Regional Preferences and Position as a Functional Beverage**: Conduct regional flavor testing to identify local preferences (e.g., tropical fruit variants) and customize marketing strategies accordingly. Position **Coca-Cola Mango Boost** not just as a flavored soft drink, but as a functional beverage with added benefits like vitamins or electrolytes to attract health-focused consumers, especially within younger demographics.
        """  
        st.markdown(followup)


    st.title("Coming soon")
    st.text("Use real time events data from online sources.")     
              

if st.session_state.selected_nav == 2:
    st.title("Product refinement")
    st.subheader("AI inovation LAB insights")        
    followup = """
    **Conclusions:**

    **Refine the Flavor Profile with Natural Ingredients**: To cater to both taste preferences and health-conscious consumers, refine the mango flavor using natural mango puree or extracts, and reduce the sugar content. This can improve the product’s authenticity and appeal to health-conscious segments, while still maintaining the refreshing Coca-Cola experience.

    **Target Regional Preferences and Position as a Functional Beverage**: Conduct regional flavor testing to identify local preferences (e.g., tropical fruit variants) and customize marketing strategies accordingly. Position **Coca-Cola Mango Boost** not just as a flavored soft drink, but as a functional beverage with added benefits like vitamins or electrolytes to attract health-focused consumers, especially within younger demographics.

    """
    st.markdown(followup)



    st.subheader("Final product idea")
    col1, col2, = st.columns([2, 1])  
    with col1:
        if 'selected_idea' in st.session_state:
            if st.session_state.selected_idea == "Coca Cola Natural Mango":
                st.image("images/mango1.jpeg", caption="Coca Cola Natural Mango", use_container_width=True)
            elif st.session_state.selected_idea == "Coca Cola Natural Strawberry":
                st.image("images/mango2.jpeg", caption="Coca Cola Natural Strawberry", use_container_width=True)
            elif st.session_state.selected_idea == "Coca Cola Natural Strawberry Mango":
                st.image("images/mango3.jpeg", caption="Coca Cola Natural Strawberry Mango", use_container_width=True)
        else:
            st.text("No product idea selected.")
    with col2:
        if 'selected_idea' in st.session_state:
            st.markdown(f"""
            **{st.session_state.selected_idea}**:
            - Dairy-free
            - Vegan-friendly
            - Infused with natural flavors
            """)
        else:
            st.text("No product idea selected.")


    st.subheader("Your Comments & Ideas")
    user_idea = st.text_area("Share your product idea or feedback here")

    if st.button("Submit comments"):
        if user_idea:
            with st.spinner("Working on your idea..."):
                time.sleep(2)  
            st.success("To be implemented!")

if st.session_state.selected_nav == 3:
    st.title("Virtual consumer panel")



    st.subheader("Panelists")
    st.image("https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?q=80&w=900&auto=format&fit=crop&ixlib=rb-4.0.3", caption="America", use_container_width=True)
   
    st.subheader("Product uniqueness")
    st.bar_chart(np.random.randn(30, 3))   
    st.title("Comming soon")
    st.text("Simulate real life situations")  

if st.session_state.selected_nav == 4:
    st.title("Final insights") 
    col1, col2, = st.columns([2, 1])     
    with col1:
        st.subheader("Product uniqueness") # kako izgledajo grafi
        st.area_chart(np.random.randn(30, 3))        
        st.line_chart(np.random.randn(30, 3))        
        st.bar_chart(np.random.randn(30, 3))      

    with col2:
        st.subheader("Filter insights by")

        age_filter = st.selectbox("Age", ["<20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80+"])
        gender_filter = st.selectbox("Gender", ["Male", "Female"])

        st.write(f"Filtering insights for age group: {age_filter} and gender: {gender_filter}")

        # Placeholder for filtered insights logic
        st.text("Filtered insights will be displayed here based on the selected filters.")
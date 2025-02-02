import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time
from openai import OpenAI
api_key = st.secrets["openai"]["api_key"]
client = OpenAI(api_key=api_key)
def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)




st.set_page_config(layout="wide")


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

if 'selected_nav' not in st.session_state:
    st.session_state.selected_nav = 0

def set_selected_nav(index):
    st.session_state.selected_nav = index
    st.rerun()  # Forces an immediate rerun

with col2:
    if st.session_state.selected_nav == 0:
        st.button("Product brief", type="primary")
    else:
        if st.button("Product brief"):
            set_selected_nav(0)

with col3:
    if st.session_state.selected_nav == 1:
        st.button("AI innovation LAB", type="primary")
    else:   
        if st.button("AI innovation LAB"):
            set_selected_nav(1)

with col4:
    if st.session_state.selected_nav == 2:
        st.button("Product refinement", type="primary")
    else:
        if st.button("Product refinement"):
            set_selected_nav(2)

with col5:
    if st.session_state.selected_nav == 3:
        st.button("Virtual consumer panel", type="primary")
    else:
        if st.button("Virtual consumer panel"):
            set_selected_nav(3)

with col6:
    if st.session_state.selected_nav == 4:
        st.button("Final insights", type="primary")
    else:
        if st.button("Final insights"):
            set_selected_nav(4)

if st.session_state.selected_nav == 0:
    st.title("Product brief")
    sample_product_brief = """Product Name: Coca-Cola Mango (Working Title)

Category: Carbonated Soft Drinks

Brand: Coca-Cola

Stage: Concept Exploration

1. Product Overview

Coca-Cola Mango is an idea for a new, fruit-infused cola variant. The goal is to explore whether a tropical twist on the classic Coca-Cola taste could excite consumers. The product would balance the familiar cola profile with a hint of ripe mango, offering a refreshing, potentially exotic experience.

Key Questions:

- How strong should the mango flavor be?
- Should this be a limited-edition or permanent SKU?
- Does the market perceive mango as a complementary or competing flavor to cola?

2. Target Audience (Tentative)

- Existing Coca-Cola drinkers looking for variety
- Gen Z and Millennials, who seek new and adventurous flavors
- Fans of tropical fruit beverages
- Markets where mango is a popular flavor (e.g., Latin America, South Asia)

3. Unique Selling Proposition (USP) (Still Developing)

- A tropical twist on a global classic
- Potentially a healthier alternative (lower sugar? natural flavors?)
- A seasonal or limited-edition buzz generator

4. Key Features & Considerations

Feature: Questions & Hypotheses
- Mango Flavor Infusion: Should it be subtle or bold? Artificial or real juice?
- Sugar & Calories: Should we offer a zero-sugar variant from launch?
- Carbonation Level: Does mango pair better with standard or lighter fizz?
- Packaging: Do we highlight mango in branding or keep it subtle?

5. Packaging (Early Thoughts)

- Format: Cans? Bottles? Multi-pack options?
- Design: Classic Coca-Cola branding with a mango color cue?
- Labeling: Should we emphasize "limited edition" to drive urgency?

6. Pricing Strategy (To Be Determined)

- Should it be priced at parity with existing flavored Coke variants?
- Would a higher price point position it as a premium, exotic offering?"""

    product_description = st.text_area("Write product brief:", height=600, placeholder=sample_product_brief)

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
                    if 'selected_idea' in st.session_state:
                        st.write(message["content"])
                    else:
                        typewriter(text=message["content"], speed=speed)

        st.subheader("Product Ideas")


        if 'ideas' not in st.session_state:
            st.session_state.ideas = [
                {
                    "prompt": "Coca Cola Natural Mango",
                    "description": """
                    **Coca Cola Natural Mango**:
                    - Made with real mango puree
                    - No added sugar
                    - Refreshing and natural taste
                    """,
                    "image_url": ""
                },
                {
                    "prompt": "Coca Cola Natural Strawberry",
                    "description": """
                    **Coca Cola Natural Strawberry**:
                    - Made with real strawberry puree
                    - No added sugar
                    - Refreshing and natural taste
                    """,
                    "image_url": ""
                },
                {
                    "prompt": "Coca Cola Natural Strawberry Mango",
                    "description": """
                    **Coca Cola Natural Strawberry Mango**:
                    - Made with real strawberry mango puree
                    - No added sugar
                    - Refreshing and natural taste
                    """,
                    "image_url": ""
                }
            ]

        col1, col2, col3 = st.columns([1, 1, 1])  
        
        for i, idea in enumerate(st.session_state.ideas):
            col = [col1, col2, col3][i]
            with col:
                prompt = idea["prompt"]
                description = idea["description"]
                if idea["image_url"]=="":  # If image URL is not already generated
                    with st.spinner("Generating image..."):
                        try:
                            response = client.images.generate(
                                model="dall-e-3",
                                prompt=prompt,
                                size="1024x1024",
                                quality="standard",
                                n=1,
                            )
                            image_url = response.data[0].url  # Get the image URL
                            st.session_state.ideas[i]["image_url"] = image_url  # Store the image URL in session state
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    image_url = idea["image_url"]

                st.image(image_url, caption=prompt, use_container_width=True)
                st.markdown(description)
                if st.button("Select idea", key=f"idea{i+1}"):
                    st.session_state.selected_idea = {"name": prompt, "description": description, "image_url": image_url}
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
    # st.write(st.session_state)
    if 'regenerated_idea' in st.session_state and 'regenerated_idea_description' in st.session_state:
        col1, col2, = st.columns([2, 1])  
        with col1:
            if 'regenerated_idea_image_url' in st.session_state:
                st.image(st.session_state.regenerated_idea_image_url, caption=st.session_state.regenerated_idea, use_container_width=True)
                st.write(st.session_state.regenerated_idea)
            else:    
                try:
                    with st.spinner("Generating image..."):
                        response = client.images.generate(
                            model="dall-e-3",
                            prompt=st.session_state.regenerated_idea,
                            size="1024x1024",
                            quality="standard",
                            n=1,
                        )
                        image_url = response.data[0].url  
                        st.session_state.regenerated_idea_image_url= image_url
                        st.image(image_url, caption=st.session_state.regenerated_idea, use_container_width=True)
    

                except Exception as e:
                    st.error(f"Error: {e}")
        with col2:
            if 'regenerated_idea_description' in st.session_state:
                st.subheader(st.session_state.regenerated_idea)
                st.markdown(st.session_state.regenerated_idea_description)

        col1, col2 = st.columns([9, 1])
        with col2:
            if(st.button("To virtual consumer panel")):
                set_selected_nav(3)                    
    elif 'selected_idea' in st.session_state:

        st.subheader("Preferred product idea generated by the Innovation lab")
        col1, col2, = st.columns([2, 1])  
        with col1:
            st.image(st.session_state.selected_idea["image_url"], caption=st.session_state.selected_idea["name"], use_container_width=True)
        with col2:
            st.subheader(st.session_state.selected_idea["name"])
            st.markdown(st.session_state.selected_idea["description"])


        st.subheader("Refine the product")
        user_idea = st.text_area("Share your product idea or feedback here:")

        if st.button("Submit comments"):
            if user_idea:
                with st.spinner("Working on your idea..."):
                    try:
                        prompt = f"Rewrite the following image prompt for a product based on the user comments:\n\nOld Prompt: {st.session_state.selected_idea["name"]}\n\n Old product description: {st.session_state.selected_idea["description"]} \n\nUser Comments: {user_idea}. Return only the prompt!"
                        # st.write(prompt)

                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "developer", "content": "You are a helpful prompt writing assistant."},
                                {
                                    "role": "user",
                                    "content": prompt
                                }
                            ]
                        )

                        new_prompt = response.choices[0].message.content.strip()
                        # st.write(new_prompt)        
                        st.session_state.regenerated_idea = new_prompt
                        prompt = f"Rewrite the following product description based on the user comments:\n\nOld Product: {st.session_state.selected_idea["name"]}\n\n Old product description: {st.session_state.selected_idea["description"]} \n\nUser Comments: {user_idea} \n\nNew Product: {new_prompt}. Return only the product description!"
                        # st.write(prompt)

                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "developer", "content": "You are a helpful assistant."},
                                {
                                    "role": "user",
                                    "content": prompt
                                }
                            ]
                        )

                        new_product_description = response.choices[0].message.content.strip()                        

                        st.session_state.regenerated_idea_description = new_product_description
                        # st.subheader("bbbb " + new_product_description)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")                    
    
        col1, col2 = st.columns([9, 1])
        with col2:
            if(st.button("To virtual consumer panel")):
                set_selected_nav(3)       
    else:
        st.text("No product idea selected.")                     

if st.session_state.selected_nav == 3:
    st.title("Virtual consumer panel")
    col1, col2, = st.columns([2, 1])   

    with col1:
        st.subheader("Panelists")
        st.image("https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?q=80&w=900&auto=format&fit=crop&ixlib=rb-4.0.3", caption="America", use_container_width=True)
    
    with col2:
        st.subheader("Filter panelists by:")

        age_filter = st.selectbox("Age", ["<20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80+"])
        gender_filter = st.selectbox("Gender", ["Male", "Female"])

        st.write(f"Filtering panelists for age group: {age_filter} and gender: {gender_filter}")

    st.subheader("Product uniqueness")
    st.bar_chart(np.random.randn(30, 3))   
    st.title("Comming soon")
    st.text("Simulate real life situations")  

    col1, col2 = st.columns([9, 1])
    with col2:
        if(st.button("To final insights")):
            set_selected_nav(4)      

if st.session_state.selected_nav == 4:
    st.title("Final insights") 
    col1, col2, = st.columns([2, 1])     
    with col1:






        # Sample Data
        data = {
            "Purchase Intent": {"score": 3.9, "norm": 4.0},
            "Unique And Different": {"score": 3.9, "norm": 3.9},
            "Relevance": {"score": 4.0, "norm": 4.1},
            "Overall Appeal": {"score": 3.9, "norm": 4.2},
        }

        # Color function based on performance
        def get_color(score, norm):
            if score >= norm:
                return "#6AB04C"  # Green (Above Norm)
            elif score >= norm - 0.2:
                return "#F7CA18"  # Yellow (In Line)
            else:
                return "#E55039"  # Red (Below Norm)

        # Streamlit UI
        st.subheader("Concept Evaluation Dashboard")
        st.write("### Performance Metrics")

        # Create Donut Charts
        cols = st.columns(len(data))  # Creates equal column sections
        for i, (metric, values) in enumerate(data.items()):
            score = values["score"]
            norm = values["norm"]
            color = get_color(score, norm)
            
            fig = go.Figure(go.Pie(
                values=[score, norm - score, 5 - norm],
                labels=["Score", "Norm Difference", "Remaining"],
                hole=0.6,
                marker=dict(colors=[color, "#D3D3D3", "#F4F4F4"]),
                textinfo='none'
            ))
            
            fig.update_layout(
                showlegend=False,
                title={
                    "text": f"<b>{metric}</b><br>{score} (Norm: {norm})",
                    "y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top",
                    "font": dict(size=14)
                },
                margin=dict(l=20, r=20, t=40, b=20)
            )
            
            cols[i].plotly_chart(fig, use_container_width=True)

        st.write("### Legend")
        st.markdown("- **🟢 Green**: Significantly above norm\n- **🟡 Yellow**: In line with norm\n- **🔴 Red**: Below norm")


        # Sample data (Price vs Purchase Consideration %)
        price = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
        purchase_consideration = np.array([90, 80, 65, 50, 35, 25, 15, 5])

        # Streamlit UI
        st.subheader("Demand Curve: Price vs Purchase Consideration")
        st.write("This graph shows how the percentage of target consumers considering purchase changes with price.")

        # Create the graph
        fig, ax = plt.subplots()
        ax.plot(purchase_consideration, price, marker='o', linestyle='-', color='b')
        ax.set_xlabel("Purchasing Consideration (% of Target Population)")
        ax.set_ylabel("Price ($)")
        ax.set_title("Demand Curve")
        ax.grid(True)

        # Display the graph in Streamlit
        st.pyplot(fig)

        # Explanation
        st.write("### Interpretation:")
        st.write("- As price increases, fewer consumers are willing to consider purchasing.")
        st.write("- This follows the typical demand curve behavior.")


        
        st.subheader("Extra data") 
        st.area_chart(np.random.randn(30, 3))        
        st.line_chart(np.random.randn(30, 3))        
        st.bar_chart(np.random.randn(30, 3))      

    with col2:
        st.subheader("Filter insights by:")

        age_filter = st.selectbox("Age", ["<20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80+"])
        gender_filter = st.selectbox("Gender", ["Male", "Female"])

        st.write(f"Filtering insights for age group: {age_filter} and gender: {gender_filter}")

        # Placeholder for filtered insights logic
        st.text("Filtered insights will be displayed here based on the selected filters.")
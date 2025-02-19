import streamlit as st
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px
import time
import pandas as pd
import seaborn as sns

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

price_grap_x = 50
purchases_per_month_graph_x =2
total_customers_graph_x = 16000000
separator = '''

---

'''

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
    context = """Coca-Cola Mango is an idea for a new, fruit-infused cola variant. The goal is to explore whether a tropical twist on the classic Coca-Cola taste could excite consumers. The product would balance the familiar cola profile with a hint of ripe mango, offering a refreshing, potentially exotic experience.

Key Questions:

- How strong should the mango flavor be?
- Should this be a limited-edition or permanent SKU?
- Does the market perceive mango as a complementary or competing flavor to cola?
"""
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

    product_name = st.text_input("Product Name", 
        placeholder="Coca-Cola Mango",
        value="Coca-Cola Mango"
    )

    context = st.text_area("Context:", 
        height=400, 
        placeholder=context,
        value=context
    )

    product_image = st.file_uploader("Upload product idea image", type=["jpg", "jpeg", "png"])

    if product_image is not None:
        st.image(product_image, caption="Uploaded product idea image", use_column_width=True)

    col1, col2 = st.columns([7, 1])
    with col2:
        if product_name and context:
            generate = st.button("Generate product brief")


    if generate:
        product_brief = st.text_area("Product Brief:", value=sample_product_brief, height=1200)

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
                    "image_url": "images/m1.webp"
                },
                {
                    "prompt": "Coca Cola Natural Strawberry",
                    "description": """
                    **Coca Cola Natural Strawberry**:
                    - Made with real strawberry puree
                    - No added sugar
                    - Refreshing and natural taste
                    """,
                    "image_url": "images/mm.jpeg"
                },
                {
                    "prompt": "Coca Cola Natural Strawberry Mango",
                    "description": """
                    **Coca Cola Natural Strawberry Mango**:
                    - Made with real strawberry mango puree
                    - No added sugar
                    - Refreshing and natural taste
                    """,
                    "image_url": "images/m3.jpeg"
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

    st.markdown(separator)

    st.subheader("AI inovation LAB discussion log")   
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
                    st.write(message["content"])
                    # typewriter(text=message["content"], speed=speed)

    st.markdown(separator)
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

        st.markdown(separator)
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
    
        col1, col2 = st.columns([5, 1])
        with col2:
            if(st.button("To virtual consumer panel")):
                set_selected_nav(3)       
    else:
        st.text("No product idea selected.")                     

if st.session_state.selected_nav == 3:
    st.title("Virtual consumer panel")


    potential_customers = {
        "<20": {"Male": 5000000, "Female": 5100000},
        "20-30": {"Male": 15000000, "Female": 16000000},
        "30-40": {"Male": 20200000, "Female": 19000000},
        "40-50": {"Male": 15000000, "Female": 15000000},
        "50-60": {"Male": 8000000, "Female": 10000000},
        "60-70": {"Male": 5000000, "Female": 4300000},
        "70-80": {"Male": 3000000, "Female": 8600000},
        "80+": {"Male": 800000, "Female": 600000},
    }


    col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])  

    with col1:
        st.text("Filter panelists by age:", help="Filter by age group")

    with col2:
        age_filter = st.multiselect("Age", ["<20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80+"], default=["20-30", "30-40"], label_visibility="collapsed")
    with col3:
        st.text("or gender:", help="Filter by gender")
    with col4:    
        gender_filter = st.multiselect("Gender", ["Male", "Female"], default=["Male", "Female"], label_visibility="collapsed")

    # Calculate total customers based on selected filters
    total_customers_graph_x = 0
    for age in age_filter:
        for gender in gender_filter:
            total_customers_graph_x += potential_customers.get(age, {}).get(gender, 0)
    st.session_state.total_customers_graph_x = total_customers_graph_x

    col1, col2, col3 = st.columns([6, 1, 1])
    with col2:
        if(st.button("RUN SIMULATION")):
            set_selected_nav(4)    



    st.markdown(separator)
    st.subheader("Explore your market ")
    st.markdown("#### Total Addressable Market (TAM) Visualization")
    st.text("We’ve estimated your market size based on industry benchmarks. Adjust if needed.")
    col1, col2, col3 = st.columns([1, 1, 3])  
    with col1:
        
        # User inputs for dynamic TAM calculation
        st.session_state.price_grap_x = st.number_input("Enter Price ($ per unit)", min_value=1, value=50)
      
        st.session_state.purchases_per_month_graph_x = st.number_input("Enter Purchases per Month (avg)", min_value=1, value=2)
       
        st.write(f"Total potential customers: {st.session_state.get('total_customers_graph_x')}")

    with col2:
        # Calculate TAM
        TAM = st.session_state.get('price_grap_x') * st.session_state.get('purchases_per_month_graph_x') * st.session_state.get('total_customers_graph_x') * 12  # Annualized TAM

        # Plot TAM as a circle
        fig, ax = plt.subplots(figsize=(5, 5))
        circle = plt.Circle((0, 0), 1, color='blue', alpha=0.3)  # Blue circle
        ax.add_patch(circle)

        # Display TAM value inside the circle
        ax.text(0, 0, f"TAM\n${TAM/1e9:.1f}B", ha='center', va='center', fontsize=18, fontweight="bold", color="black")

        # Remove axes for clean look
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        # Display the plot
        st.pyplot(fig)
    with col3:
        st.markdown("""
        ##### What is TAM and how it is calculated?
        - **Total Addressable Market (TAM)** represents the total revenue opportunity available for a product or service.
        - **TAM = number of customers X annual value per customer (AVC)**
        - AVC = **product price X number of purchases per month X number of months in a year**
        """)

    st.markdown(separator)
    st.markdown("#### Competitors on the marker")   
    st.text("Explore your competitors and their product offerings.") 
    competitors = [
        {
            "name": "Pepsi Mango",
            "description": "Pepsi with a hint of mango flavor.",
            "image_url": "https://sweet-shop.si/2747-large_default/pepsi-max-mango-zero-330ml.jpg"
        },
        {
            "name": "Dr Pepper Cherry",
            "description": "Dr Pepper with a cherry twist.",
            "image_url": "https://ameriskedobrote.si/wp-content/uploads/2022/12/Dr-Pepper-Cherry-355ml.jpg"
        },
        {
            "name": "Sprite Tropical Mix",
            "description": "Sprite with tropical fruit flavors.",
            "image_url": "https://louisianapantry.com/cdn/shop/files/tropicalspriteonabeachbackgroundwithfruitsaroundthebottom.jpg?v=1696525285"
        }
    ]


    coll1, coll2, coll3 = st.columns(3)
    for i, competitor in enumerate(competitors):
        col = [coll1, coll2, coll3][i % 3]
        with col:
            st.image(competitor["image_url"], caption=competitor["name"], use_container_width=False, width=150)
            st.markdown(f"**{competitor['name']}**: {competitor['description']}")



    st.markdown(separator)
    st.subheader("Comming soon")
    st.text("Simulate real life situations")  

    col1, col2 = st.columns([9, 1])
    with col2:
        if(st.button("To final insights")):
            set_selected_nav(4)      

if st.session_state.selected_nav == 4:
    st.title("Final insights") 
    st.subheader("Concept Evaluation Dashboard")
    st.markdown("#### Key Metrics ")
    st.text("See the most important insights from the survey to guide your decisions.")
    col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 8])  

    with col1:
        st.text("Filter insights by age:", help="Filter by age group")

    with col2:
        age_filter = st.selectbox("Age", ["<20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80+"], label_visibility="collapsed")
    with col3:
        st.text("or gender:", help="Filter by gender")
    with col4:    
        gender_filter = st.selectbox("Gender", ["Male", "Female"], label_visibility="collapsed")



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

    # TODO: add data from an API
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


    col1, col2, col3 = st.columns([8, 1, 2])
    with col1:
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
                "text": f"<b>{metric}</b>",
                "y": 0.9, "x": 0.5, "xanchor": "center", "yanchor": "top",
                "font": dict(size=25)
                },
                annotations=[
                dict(
                    text=f"{score}",
                    x=0.5, y=0.5, font_size=40, showarrow=False
                )
                ],
                margin=dict(l=20, r=20, t=40, b=20)
            )
            
            cols[i].plotly_chart(fig, use_container_width=True, key="chart_" + str(i))
    with col3:
        st.text("")
        st.text("")
        st.markdown("""
        #### Legend
        - **🟢 Green**: Significantly above norm
        - **🟡 Yellow**: In line with norm
        - **🔴 Red**: Below norm
        """)

    st.markdown(separator)


    age_categories = {
        "20-30": "blue",
        "30-40": "green",
        "40-50": "red",
        "50-60": "purple",
        "60-70": "orange",
        "70-80": "brown"
    }
    # Generate synthetic data for demonstration
    regions = ["Northeast", "Southwest", "West", "Southeast", "Midwest"]
    genders = ["Male", "Female"]
    ages = ["18", "19", "20", "21", "22", "23", "24"]

    data = []
    for age_group, color in age_categories.items():
        relevance = np.random.rand(10) * 10  # Random values for relevance
        uniqueness = np.random.rand(10) * 10  # Random values for uniqueness
        for r, u in zip(relevance, uniqueness):
            age = np.random.choice(ages)
            gender = np.random.choice(genders)
            region = np.random.choice(regions)
            data.append([age_group, r, u, age, gender, region])

    df = pd.DataFrame(data, columns=["Age Group", "Relevance", "Uniqueness", "Age", "Gender", "Region"])

    # Streamlit app layout
    st.subheader("Segment Analysis")
    st.text("Understand which customer segments matter most and how they differ.")
    st.markdown("#### Insights Parametric Graph")
    col1, col2 = st.columns([2, 1])
    with col1:
        metric_filter = st.multiselect(
            "Select performance metrics:",
            ["Purchase Intent", "Unique And Different", "Relevance", "Overall Appeal"],
            default=["Purchase Intent", "Unique And Different"]
        )

    col1, col2 = st.columns([8, 1])
    with col1: 
        # Create a Plotly scatter plot with hover tooltips
        fig = px.scatter(
            df,
            x="Relevance",
            y="Uniqueness",
            color="Age Group",  # Color points by age group
            title="Segmentation (Relevance & Uniqueness) According to Age",
            labels={"Relevance": "Relevance", "Uniqueness": "Uniqueness"},
            hover_data={"Relevance": True, "Uniqueness": True, "Age Group": False, "Age": True, "Gender": True, "Region": True},  # Enables hover tooltips
        )

        # Move legend to the right with more space
        fig.update_layout(
            legend=dict(
                title=dict(text="Select age group:", font=dict(size=22)),  # Increase legend title font size
                orientation="v",
                yanchor="top",
                y=1,
                xanchor="left",
                x=1.1,  # Increase space between graph and legend
                font=dict(size=18)  # Increase legend font size
            ),
            title_font_size=22,  # Increase title font size
            font=dict(size=18),  # Increase overall font size
            xaxis=dict(title_font=dict(size=20)),  # Increase x-axis title font size
            yaxis=dict(title_font=dict(size=20))   # Increase y-axis title font size
        )

        # Show interactive Plotly chart in Streamlit
        st.plotly_chart(fig)



    st.markdown(separator)







    col1, col2, col3 = st.columns([5, 1, 5])


    with col1:
        # Sample data (Price vs Purchase Consideration %)
        price = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
        purchase_consideration = np.array([90, 80, 65, 50, 35, 25, 15, 5])
        df = pd.DataFrame({"Price ($)": price, "Purchase Consideration (%)": purchase_consideration})
        # Streamlit UI
        st.subheader("Pricing Impact")
        st.write("Explore how pricing changes can maximize demand and market potential.*")
        st.write("This graph shows how the percentage of target consumers considering purchase changes with price.")

        # Create an interactive Plotly graph
        fig = px.line(
            df,
            x="Price ($)",
            y="Purchase Consideration (%)",
            markers=True,
            title="Demand Curve",
            hover_data={"Price ($)": True, "Purchase Consideration (%)": True}  # Enables tooltips
        )

        # Show the interactive chart
        st.plotly_chart(fig)

        # Explanation
        st.write("### Interpretation:")
        st.write("- As price increases, fewer consumers are willing to consider purchasing.")
        st.write("- This follows the typical demand curve behavior.")




    with col3:
        price_grap_x=50
        purchases_per_month_graph_x=2
        total_customers_graph_x=16000000
        if 'price_grap_x' in st.session_state and 'purchases_per_month_graph_x' in st.session_state and 'total_customers_graph_x' in st.session_state:
            price_grap_x = st.session_state.price_grap_x
            purchases_per_month_graph_x = st.session_state.purchases_per_month_graph_x
            total_customers_graph_x = st.session_state.total_customers_graph_x

        st.subheader("Market Visualization: TAM vs SAM")
        # User inputs for dynamic TAM and SAM calculation
        price = st.number_input("Enter Price ($ per unit)", min_value=1, value=price_grap_x)
        purchases_per_month = st.number_input("Enter Purchases per Month (avg)", min_value=1, value=purchases_per_month_graph_x)
        total_customers = st.number_input("Enter Total Potential Customers", min_value=1000, value=total_customers_graph_x)
        capture_percentage = 20
        st.write(f"Potential Customers Captured (SAM): {capture_percentage}%")
        # capture_percentage = st.slider("Enter % of Potential Customers Captured (SAM)", min_value=1, max_value=100, value=20)
        
        # Calculate TAM
        TAM = price * purchases_per_month * total_customers * 12 
        SAM = TAM * (capture_percentage / 100)  # SAM is a percentage of TAM

        # Plot TAM & SAM as nested circles
        fig, ax = plt.subplots(figsize=(6, 6))

        # Draw TAM (Large outer circle)
        tam_circle = plt.Circle((0, 0), 1, color='blue', alpha=0.3, label="TAM") 
        ax.add_patch(tam_circle)

        # Draw SAM (Smaller inner circle)
        sam_radius = (SAM / TAM)  # Scale SAM relative to TAM
        sam_circle = plt.Circle((0, 0), sam_radius, color='green', alpha=0.5, label="SAM")
        ax.add_patch(sam_circle)

        # Display TAM value inside the larger circle
        ax.text(0, 0.5, f"TAM\n${TAM/1e9:.1f}B", ha='center', va='center', fontsize=16, fontweight="bold", color="black")

        # Display SAM value inside the smaller circle
        ax.text(0, -0.2, f"SAM\n${SAM/1e9:.1f}B", ha='center', va='center', fontsize=14, fontweight="bold", color="black")

        # Remove axes for a clean look
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        coll1, coll2, coll3 = st.columns([1, 3, 1])
        with coll2:
            st.pyplot(fig)





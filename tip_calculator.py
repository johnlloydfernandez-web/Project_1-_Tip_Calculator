import streamlit as st

st.set_page_config(
    page_title="BILL & TIP CALCULATOR",
    page_icon="₱",
    layout="centered"
)

st.markdown(
    """
    <style>
    div[data-testid="stButton"] > button {
        height: 60px;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center;'>LLOYD'S FIRST PYTHON PROJECT: THE BILL & TIP CALCULATOR</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align: center;'>HI! INPUT YOUR TOTAL BILL, # OF PEOPLE, AND TIP PERCENT</h4>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="
        position: fixed;
        top: 190px;
        right: 90px;
        width: 230px;
        transform: rotate(7deg);
        text-align: center;
        font-style: italic;
        font-size: 18px;
        opacity: 0.75;
    ">
        “Quickly split your bill and tip with your group.”
    </div>
    """,
    unsafe_allow_html=True
)

# Remember values
if "total_bill" not in st.session_state:
    st.session_state.total_bill = 0

if "people" not in st.session_state:
    st.session_state.people = 0

if "tip_percent" not in st.session_state:
    st.session_state.tip_percent = 0


# Button functions
def add_to_bill(amount):
    st.session_state.total_bill += amount


def add_person():
    st.session_state.people += 1


def add_tip():
    st.session_state.tip_percent += 1


# Calculator card
with st.container(border=True):

    total_bill = st.number_input(
        "Total bill",
        min_value=0,
        step=1,
        key="total_bill"
    )

    # Bill quick-add buttons
    b1, b2 = st.columns(2)

    with b1:
        st.button(
            "+10,000",
            on_click=add_to_bill,
            args=(10000,),
            use_container_width=True
        )

    with b2:
        st.button(
            "+1,000",
            on_click=add_to_bill,
            args=(1000,),
            use_container_width=True
        )

    b3, b4, b5 = st.columns(3)

    with b3:
        st.button(
            "+100",
            on_click=add_to_bill,
            args=(100,),
            use_container_width=True
        )

    with b4:
        st.button(
            "+10",
            on_click=add_to_bill,
            args=(10,),
            use_container_width=True
        )

    with b5:
        st.button(
            "+1",
            on_click=add_to_bill,
            args=(1,),
            use_container_width=True
        )

    # People and tip
    col1, col2 = st.columns(2)

    with col1:
        people = st.number_input(
            "Number of people",
            min_value=0,
            step=1,
            key="people"
        )

        st.button(
            "+1 person",
            on_click=add_person,
            use_container_width=True
        )

    with col2:
        tip_percent = st.number_input(
            "Tip percentage",
            min_value=0,
            step=1,
            key="tip_percent"
        )

        st.button(
            "+1% tip",
            on_click=add_tip,
            use_container_width=True
        )


# Calculate tip split
def tip_divided(tip_percent, people):
    if people == 0:
        return 0

    tip_percent_divided = tip_percent / 100
    divided_bill = (total_bill * tip_percent_divided) / people

    return divided_bill


# Calculate bill split
if people == 0:
    bill_split = 0
else:
    bill_split = total_bill / people


tip_split = tip_divided(tip_percent, people)


# Results
result_col1, result_col2 = st.columns(2)

with result_col1:
    st.metric("Bill per person", f"₱{bill_split:,.2f}")

with result_col2:
    st.metric("Tip per person", f"₱{tip_split:,.2f}")

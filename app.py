
import streamlit as st

# 1. Configure the webpage
st.set_page_config(
    page_title="Car Enquiry",
    page_icon="🚗",
    layout="wide"
)

# 2. Sample car information
# These are demo values, not verified current prices.
cars = {
    "baleno": {
        "name": "Maruti Suzuki Baleno",
        "price": "Demo: ₹6.7 lakh onwards",
        "fuel": "Petrol",
        "engine": "1.2L",
        "transmission": "Manual / AMT",
        "seats": "5",
        "image": "Baleno.jpg",
        "body": "Hatchback"
    },
    "swift": {
        "name": "Maruti Suzuki Swift",
        "price": "Demo: ₹6.5 lakh onwards",
        "fuel": "Petrol",
        "engine": "1.2L",
        "transmission": "Manual / AMT",
        "seats": "5",
        "image": "SWIFT.jpg",
        "body": "Hatchback"
    },
    "creta": {
        "name": "Hyundai Creta",
        "price": "Demo: ₹11 lakh onwards",
        "fuel": "Petrol / Diesel",
        "engine": "Variant dependent",
        "transmission": "Manual / Automatic",
        "seats": "5",
        "image": "CRETA.jpg",
        "body": "SUV"
    }
}

# 3. Display the heading
st.title("🚗 Car Enquiry Application")
st.write("Search for a car to explore its price and specifications.")

# 4. Get the model name from the user
model = st.text_input(
    "Enter car model",
    placeholder="Example: Baleno, Swift, Creta"
)

# 5. Search when the button is clicked
if st.button("🔍 Search Car", use_container_width=True):

    search_name = model.strip().lower()

    if search_name == "":
        st.warning("Please enter a car model.")

    elif search_name in cars:

        car = cars[search_name]

        # 6. Display the car information
        st.success("Car found!")

        st.header("🚘 " + car["name"])
        st.subheader("💰 " + car["price"])
    
        st.image(car["image"], use_container_width=True)

        col1, col2, col3 = st.columns(3)

        col1.metric("⛽ Fuel Type", car["fuel"])
        col2.metric("⚙️ Engine", car["engine"])
        col3.metric("🔧 Transmission", car["transmission"])

        col4, col5 = st.columns(2)

        col4.metric("👥 Seating", car["seats"])
        col5.metric("🚙 Body Type", car["body"])

        st.caption(
            "Demo data only. Verify specifications and current prices "
            "with the manufacturer or dealer."
        )

    else:
        st.error(
            "Car not found. Try Baleno, Swift, or Creta."
        )

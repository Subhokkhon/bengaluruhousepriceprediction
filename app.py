import streamlit as st

def predict_price(total_sqft, bhk, bath, location):
    # Implement your prediction logic here
    # This function should return the predicted price based on the input features
    # For simplicity, let's just return the price corresponding to the selected location
    prices = {
        "Yelahanka": 186.000,
        "Hebbal": 477.000,
        "8th Phase JP Nagar": 54.005,
        "Sarjapur": 43.490,
        "KR Puram": 56.800,
        "Kengeri": 18.500,
        "Hennur Road": 63.770,
        "Arekere": 265.000,
        "Bettahalsoor": 445.000
    }
    return prices.get(location, 0)  # Return 0 if location not found

def main():
    st.title('Bangalore House Price Prediction')

    total_sqft = st.number_input('Total Square Feet')
    bhk = st.number_input('Number of Bedrooms')
    bath = st.number_input('Number of Bathrooms')
    location = st.selectbox('Location', ['Yelahanka', 'Hebbal', '8th Phase JP Nagar', 'Sarjapur', 'KR Puram', 'Kengeri', 'Hennur Road', 'Arekere', 'Bettahalsoor'])

    if st.button('Predict Price'):
        predicted_price = predict_price(total_sqft, bhk, bath, location)
        st.success(f'Predicted Price: ${predicted_price}')

if __name__ == '__main__':
    main()

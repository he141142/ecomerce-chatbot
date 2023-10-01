import streamlit as st

# Product data (replace with your product data)
products = [
    {'name': 'Product 1', 'price': 19.99, 'description': 'Description for Product 1'},
    {'name': 'Product 2', 'price': 29.99, 'description': 'Description for Product 2'},
    {'name': 'Product 3', 'price': 39.99, 'description': 'Description for Product 3'},
]

# Streamlit app
st.title('E-commerce Product Catalog')

# Display product catalog
for product in products:
    st.write(f"**{product['name']}**")
    st.write(f"Price: ${product['price']:.2f}")
    st.write(f"Description: {product['description']}")
    st.button(f"Add to Cart - ${product['price']:.2f}")

# Shopping cart (a simple example)
st.sidebar.title('Shopping Cart')
cart_total = 0

# Handle adding products to the cart
for product in products:
    if st.sidebar.button(f"Add {product['name']}"):
        cart_total += product['price']

st.sidebar.subheader(f'Total: ${cart_total:.2f}')
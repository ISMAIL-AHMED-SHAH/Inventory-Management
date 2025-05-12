import streamlit as st
from services.inventory import Inventory
from models.electronics import Electronics
from models.grocery import Grocery
from models.clothing import Clothing
from sidebar import my_sidebar
import pandas as pd
import os

# --- Streamlit Config ---
st.set_page_config(page_title="📦 Inventory Manager", layout="centered")
st.title("📦 Inventory Management System")

DATA_FILE = "data/inventory.json"
# --- Inventory Instance ---
inventory = Inventory(DATA_FILE)

# --- Load data if exists ---
if os.path.exists(DATA_FILE):
    inventory.load_from_file(DATA_FILE)

st.sidebar.image("assets/inventory.jpg", use_container_width=True)
# --- Sidebar Menu ---
menu = st.sidebar.selectbox("🔍 Select Action", [
    "Add Product", "View Products", "Sell Product",
    "Restock Product", "Search Product", "Save Inventory", "Load Inventory"
])

# --- Add Product ---
if menu == "Add Product":
    st.subheader("➕ Add New Product")
    prod_type = st.selectbox("Product Type", ["Electronics", "Grocery", "Clothing"])
    
    st.sidebar.image("assets/add.png", use_container_width=True)
    prod_id = st.text_input("Product ID")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)

    if prod_type == "Electronics":
        brand = st.text_input("Brand")
        warranty = st.number_input("Warranty (Years)", min_value=0)
        if st.button("Add Product"):
            try:
                product = Electronics(prod_id, name, price, quantity, brand, warranty)
                inventory.add_product(product)
                st.success("✅ Electronics Product added!")
            except Exception as e:
                st.error(str(e))

    elif prod_type == "Grocery":
        expiry = st.date_input("Expiry Date")
        if st.button("Add Product"):
            try:
                product = Grocery(prod_id, name, price, quantity, expiry.strftime("%Y-%m-%d"))
                inventory.add_product(product)
                st.success("✅ Grocery item added!")
            except Exception as e:
                st.error(str(e))

    elif prod_type == "Clothing":
        size = st.selectbox("Size", ["S", "M", "L", "XL"])
        material = st.text_input("Material")
        if st.button("Add Product"):
            try:
                product = Clothing(prod_id, name, price, quantity, size, material)
                inventory.add_product(product)
                st.success("✅ Clothing item added!")
            except Exception as e:
                st.error(str(e))

# --- View Products ---
elif menu == "View Products":
    st.subheader("📋 All Products")
    all_products = inventory.list_all_products()
    st.sidebar.image("assets/view.png", use_container_width=True)
    st.sidebar.image("assets/prod.png", use_container_width=True)
    if all_products:
        rows = [str(p) for p in all_products]
        st.write("\n\n".join(rows))
        st.info(f"💰 Total Inventory Value: {inventory.total_inventory_value():.2f}")
    else:
        st.warning("Inventory is empty.")

# --- Sell Product ---
elif menu == "Sell Product":
    st.subheader("💸 Sell a Product")
    product_id = st.text_input("Product ID to sell")
    quantity = st.number_input("Quantity to sell", min_value=1)
    st.sidebar.image("assets/cart.png", use_container_width=True)
    if st.button("Sell"):
        try:
            inventory.sell_product(product_id, quantity)
            st.success("✅ Product sold successfully.")
        except Exception as e:
            st.error(str(e))

# --- Restock Product ---
elif menu == "Restock Product":
    st.subheader("🔄 Restock Product")
    st.sidebar.image("assets/restock.png")
    product_id = st.text_input("Product ID to restock")
    quantity = st.number_input("Quantity to add", min_value=1)
    if st.button("Restock"):
        try:
            inventory.restock_product(product_id, quantity)
            st.success("✅ Product restocked.")
        except Exception as e:
            st.error(str(e))

# --- Search Product ---
elif menu == "Search Product":
    st.subheader("🔎 Search Product")
    search_type = st.radio("Search by", ["Name", "Type"])
    
    st.sidebar.image("assets/search.jpg", use_container_width=True)
    if search_type == "Name":
        name = st.text_input("Enter product name")
        if st.button("Search"):
            result = inventory.search_by_name(name)
            if result:
                st.write(str(result))
            else:
                st.warning("No product found.")
    
    if search_type == "Type":
        ptype = st.selectbox("Select Type", ["Electronics", "Grocery", "Clothing"])
        results = inventory.search_by_type(ptype)
        if results:
            st.write(f"Found {len(results)} products of type {ptype}:")
            for p in results:
                st.write(str(p))
        else:
            st.warning("No products of this type found.")

# --- Save Inventory ---
elif menu == "Save Inventory":
    st.sidebar.image("assets/save.png", use_container_width=True)
    st.subheader("💾 Save Inventory to JSON")
    if st.button("Save Now"):
        st.write(f"📦 Current Inventory Size: {len(inventory._products)}")

        inventory.save_to_file(DATA_FILE)
        st.success("✅ Inventory saved to JSON.")

# --- Load Inventory ---
elif menu == "Load Inventory":

    st.sidebar.image("assets/load.png", use_container_width=True)
    st.subheader("📂 Load Inventory")
    if st.button("Load from File"):
        inventory.load_from_file(DATA_FILE)
        st.success("✅ Inventory loaded successfully.")


st.image("assets/invent.png")
st.sidebar.markdown("----")

my_sidebar()
import streamlit as st
from streamlit_option_menu import option_menu

# Function for the "Contact Us" tab
def contact_us():
    st.header(":mailbox: Get in touch with me!")

    contact_form = """
    <form action="https://formsubmit.co/vaibhav2oke@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin: 8px 0;">
        <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin: 8px 0;">
        <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 8px; margin: 8px 0; height: 150px;"></textarea>
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer;">
            Send
        </button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

# Main function
def main():
    selected = option_menu(
        menu_title=None,  # required
        options=["Contact Us"],  # Only "Contact Us" tab
        icons=["envelope"],  # Icon for the tab
        menu_icon="cast",  # optional
        default_index=0,  # Set default selection
        orientation="horizontal"
    )

    if selected == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()
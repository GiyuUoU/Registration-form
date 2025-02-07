import streamlit as st

st.title("Registration Form")
st.write("Please fill in the form below")


#Form

form_values = {
    "name":None,
    "course":None,
    "roll_no":None,
    "contact":None,
    "email":None
    }


with st.form( key= "user_info_form"):

 form_values["name"] = st.text_input("Name ")
 form_values["course" ] = st.text_input("Course")
 form_values["roll_no"] = st.number_input("Roll number")
 form_values["contact"] = st.number_input("Contact Number")
 form_values["email"] = st.text_input("Email")

 print(form_values)

 submitted = st.form_submit_button()

 if submitted:
    if not all(form_values.values()):
        st.warning("Please fill all the sections !!!")
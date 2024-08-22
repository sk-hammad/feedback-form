import streamlit as st

st.title("Police Service Feedback Form")

# 1. Service Quality
st.header("Service Quality")
overall_service = st.selectbox("How would you rate the overall service provided by the police?",
                               ['Excellent', 'Good', 'Fair', 'Poor'])
professionalism = st.selectbox("How satisfied were you with the professionalism and courtesy of the officers?",
                               ['Very Satisfied', 'Satisfied', 'Neutral', 'Unsatisfied', 'Very Unsatisfied'])
communication = st.selectbox("How clear and understandable was the communication from the police?",
                             ['Very Clear', 'Clear', 'Neutral', 'Unclear', 'Very Unclear'])

# 2. Response Time
st.header("Response Time")
response_time = st.selectbox("How would you rate the police's response time to your incident?",
                             ['Excellent', 'Good', 'Fair', 'Poor'])
appropriate_response = st.selectbox("Was the response time appropriate for the nature of the incident?",
                                    ['Yes', 'No', 'Unsure'])

# 3. Safety and Security
st.header("Safety and Security")
safety = st.selectbox("How safe do you feel in your community?",
                      ['Very Safe', 'Safe', 'Neutral', 'Unsafe', 'Very Unsafe'])
safety_improvement = st.selectbox("Have you noticed any improvement in safety in your community in the last year?",
                                  ['Yes', 'No', 'Unsure'])

# 4. Interaction with Police
st.header("Interaction with Police")
interactions = st.selectbox("Have you had any interactions with the police in the last 6 months?",
                            ['Yes', 'No'])
if interactions == 'Yes':
    interaction_nature = st.text_area("If yes, please describe the nature of your interaction:")

# 5. Trust and Confidence
st.header("Trust and Confidence")
trust = st.selectbox("How much do you trust the police to handle incidents in your community?",
                     ['Fully Trust', 'Somewhat Trust', 'Neutral', 'Distrust', 'Fully Distrust'])
confidence = st.selectbox("Do you feel confident that the police will protect your rights and safety?",
                          ['Yes', 'No', 'Unsure'])

# 6. Specific Incidents or Concerns
st.header("Specific Incidents or Concerns")
mistreatment = st.selectbox("Have you ever felt mistreated or unfairly treated by the police?",
                            ['Yes', 'No'])
if mistreatment == 'Yes':
    mistreatment_details = st.text_area("If yes, please explain:")
improvements = st.text_area("What improvements would you like to see in police services?")

# 7. Additional Comments
st.header("Additional Comments")
additional_comments = st.text_area("Please provide any additional comments or suggestions:")

# 8. Demographics (Optional)
st.header("Demographics (Optional)")
age_group = st.selectbox("Age group:",
                         ['Under 18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+'])
gender = st.selectbox("Gender:",
                      ['Male', 'Female', 'Other', 'Prefer not to say'])
area_of_residence = st.text_input("Area of residence:")

# Submit button
if st.button("Submit"):
    st.success("Thank you for your feedback!")

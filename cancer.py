import pickle
import streamlit as st
pickle_in = open("breast_cancer.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict(mean_radius,mean_perimeter,mean_area,mean_concavity,mean_concave_points,area_error,worst_radius,worst_perimeter,worst_area,worst_concave_points):
    
    prediction = classifier.predict([[mean_radius,mean_perimeter,mean_area,mean_concavity,mean_concave_points,area_error,worst_radius,worst_perimeter,worst_area,worst_concave_points]])
#    print(prediction)
    return prediction

def main():
    st.title("Breast Cancer Prediction")
    html_temp = '''
    <div style = "background-color:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Breast Cancer ML App</h2>
    </div>
    '''
	
    st.markdown(html_temp, unsafe_allow_html=True)
    mean_radius = st.text_input("mean radius")
    st.caption("EX: 20")
    mean_perimeter = st.text_input("mean perimeter")
    st.caption("EX: 140")
    mean_area = st.text_input("mean area")
    st.caption("EX: 1250")
    mean_concavity = st.text_input("mean concavity")
    st.caption("EX: 0")
    mean_concave_points = st.text_input("mean concave points")
    st.caption("EX: 0")
    area_error = st.text_input("area error")
    st.caption("EX: 40")
    worst_radius = st.text_input("worst radius")
    st.caption("EX: 25")
    worst_perimeter = st.text_input("worst perimeter")
    st.caption("EX: 184")
    worst_area = st.text_input("worst area")
    st.caption("EX: 1821")
    worst_concave_points = st.text_input("worst concave points")
    st.caption("EX: 0")
    result=""
    if st.button("Predict"):
        result=predict(mean_radius,mean_perimeter,mean_area,mean_concavity,mean_concave_points,area_error,worst_radius,worst_perimeter,worst_area,worst_concave_points)
    st.success('The Output is {}'.format(result))

if __name__ =='__main__':
        main()
import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1, col2= st.columns(2)

    with col1:
        a_AU = st.text_input ('input nilai Jarak semimayor objek astronomi dalam satuan astronomi (AU))')
    with col1:
        e = st.text_input ('input nilai Eksentrisitas orbit objek astronomi')
    with col1:
        i_deg = st.text_input ('input nilai Inklinasi orbit objek astronomi dalam derajat')
    with col1:
        w_deg = st.text_input ('input nilai Argumen perihelion objek astronomi dalam derajat')
    with col1:
        Node_deg = st.text_input ('input nilai Longitudinal node objek astronomi dalam derajat')
    with col2:
        M_deg = st.text_input ('input nilai Anomali rata-rata objek astronomi dalam derajat')
    with col2:
        q_AU = st.text_input ('input nilai Jarak perihelion objek astronomi dalam satuan astronomi (AU)')
    with col2:
        Q_AU = st.text_input ('input nilai Jarak aphelion objek astronomi dalam satuan astronomi (AU)')
    with col2:
        P_yr = st.text_input ('input nilai Periode orbit objek astronomi dalam tahun')
    with col2:
        H_mag = st.text_input ('input nilai Magnitudo absolut objek astronomi')
    with col2:
        MOID_AU = st.text_input ('input nilai Minimum Orbit Intersection Distance')

    features = [a_AU,e,i_deg,w_deg,Node_deg,M_deg,q_AU,Q_AU,P_yr,H_mag,MOID_AU]

    #tombol
    if st.button("prediksi orbit"):
        prediction, score =  predict(x,y,features)
        score = score
        st.info("prediksi berhasil")

        if (prediction[0]==0):
            st.warning("Asteroid Main Belt (AMO*)")
        elif (prediction[0]==1):
            st.warning("Asteroid Perihelion Object (APO)")
        elif (prediction[0]==2):
            st.warning("kelompok Asteroid Aten (APO*)")
        elif (prediction[0]==3):
            st.warning("Asteroid Apohele (ATE)")
        elif (prediction[0]==4):
            st.warning("kelompok Asteroid Atira (ATE*)")
        else:
            st.success("Inner-Earth Object (IEO*)")
        
        st.write("model akurasi", (score*100), "%")
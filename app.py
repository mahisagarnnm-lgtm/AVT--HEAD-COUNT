import pandas as pd
import plotly.express as px
import streamlit as st

# પેજ સેટઅપ
st.set_page_config(
    page_title="Mission Dashboard", page_icon="📊", layout="wide"
)

# શીર્ષક
st.markdown(
    "<h1 style='color: #0f2c59;'>Poshan Maah 2026 — Mission Dashboard</h1>",
    unsafe_allow_html=True,
)
st.write("Government of Gujarat | Women and Child Development Department")

# એક્સેલ ફાઈલ રીડ કરવી (તમારી એક્સેલ ફાઈલનું નામ અહીં આપવું)
# દા.ત. file_name = "data.xlsx"
@st.cache_data
def load_data():
  # અહીં તમારી એક્સેલ ફાઈલ લોડ કરો
  df = pd.read_excel("data.xlsx")
  return df


# ઉદાહરણ તરીકે KPI કાર્ડ્સ અને ડેટા પ્રદર્શિત કરવો
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(
      label="Total Activities", value="4,14,31,940", delta="86.2% Target"
  )
with col2:
  st.metric(label="Pending Activities", value="66,33,610")
with col3:
  st.metric(label="Districts with Data", value="33 / 33")

st.markdown("---")
st.subheader("Poshan Maah Overall Achievement — State Total")

# ટેબલ ડેટા બતાવવા માટે
data = {
    "CATEGORY": ["MoW&CD", "Other Line Departments", "Total"],
    "TARGET ACTIVITIES": [7959750, 40105800, 48065550],
    "ACHIEVEMENT ACTIVITIES": [8119936, 33312004, 41431940],
    "ACHIEVEMENT %": ["102.0%", "83.1%", "86.2%"],
    "PENDING ACTIVITIES": [-160186, 6793796, 6633610],
}
df_display = pd.DataFrame(data)
st.table(df_display)

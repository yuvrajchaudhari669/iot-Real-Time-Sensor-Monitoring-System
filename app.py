import random
import time
from datetime import datetime
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="IoT Telemetry & Anomaly Detection", layout="wide"
)

st.title("⚡ Real-Time IoT Sensor Telemetry Dashboard")
st.write("Live data streaming and automated anomaly detection pipeline.")

# Metrics layout
kpi1, kpi2, kpi3 = st.columns(3)

# Baseline limits
FLOW_RATE_THRESHOLD = 8.5  # L/min

# Simulated streaming data
current_flow = round(random.uniform(2.0, 9.5), 2)
is_anomaly = current_flow > FLOW_RATE_THRESHOLD

with kpi1:
    st.metric("Sensor Status", "ONLINE", delta="Active")

with kpi2:
    st.metric("Live Flow Rate", f"{current_flow} L/min")

with kpi3:
    status_label = "CRITICAL ALERT" if is_anomaly else "NORMAL"
    delta_val = "Threshold Exceeded" if is_anomaly else "Stable"
    st.metric("System State", status_label, delta=delta_val)

if is_anomaly:
    st.error(
        f"⚠️ Anomaly Detected! Flow rate exceeded baseline limit of {FLOW_RATE_THRESHOLD} L/min."
    )
else:
    st.success("✅ Operational metrics within expected parameters.")

# Telemetry Log
st.subheader("Historical Telemetry Log")
timestamps = pd.date_range(end=datetime.now(), periods=10, freq="1min")
sample_data = pd.DataFrame(
    {
        "Timestamp": timestamps,
        "Sensor_ID": ["FLOW_01"] * 10,
        "Flow_Rate (L/min)": [
            round(random.uniform(2.0, 7.5), 2) for _ in range(10)
        ],
        "Relay_State": ["CLOSED"] * 10,
    }
)
st.dataframe(sample_data, use_container_width=True)
st.line_chart(sample_data.set_index("Timestamp")["Flow_Rate (L/min)"])

import os
import time
import streamlit as st
from subprocess import run
from threading import Timer

# Path where battery report will be stored
battery_report_path = r"C:\Users\samar\battery-report.html"

# Function to execute the powercfg command to generate battery report
def generate_battery_report():
    command = f"powercfg /batteryreport /output {battery_report_path}"
    run(command, shell=True)

# Function to read the contents of the battery report file
def read_battery_report():
    if os.path.exists(battery_report_path):
        with open(battery_report_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return "Battery report not found."

# Function to automatically update the battery report after a given interval
def auto_update_report(interval=300):
    generate_battery_report()
    Timer(interval, auto_update_report, [interval]).start()

# Streamlit Dashboard UI
st.title("Battery Report Dashboard")

st.write("This dashboard shows the contents of your battery report, which is updated automatically every few minutes.")

# Button to manually generate a new battery report
if st.button("Generate Battery Report Now"):
    generate_battery_report()
    st.success("Battery report generated successfully!")

# Display battery report
st.subheader("Battery Report:")
battery_report_content = read_battery_report()
st.components.v1.html(battery_report_content, height=500, scrolling=True)

# Set an auto-update interval (in seconds)
st.sidebar.header("Auto Update Settings")
interval = st.sidebar.slider("Update interval (in minutes):", 1, 60, 5)

# Start auto-updating the report
auto_update_report(interval * 60)


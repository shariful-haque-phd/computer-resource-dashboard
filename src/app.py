import time
import psutil
import streamlit as st

st.set_page_config(page_title="Computer Resource Dashboard",layout="wide")
st.title("Computer Resource Dashboard")

cpu=psutil.cpu_percent(interval=0.4)
mem=psutil.virtual_memory()
disk=psutil.disk_usage("/")
net=psutil.net_io_counters()

cols=st.columns(4)
cols[0].metric("CPU",f"{cpu:.1f}%")
cols[1].metric("Memory",f"{mem.percent:.1f}%")
cols[2].metric("Disk",f"{disk.percent:.1f}%")
cols[3].metric("Memory available",f"{mem.available/1024**3:.2f} GB")

st.subheader("Network counters")
st.write({"bytes_sent":net.bytes_sent,"bytes_received":net.bytes_recv})

try:
    temps=psutil.sensors_temperatures()
except Exception:
    temps={}
if temps:
    st.subheader("Temperatures")
    st.json({k:[{"label":x.label,"current":x.current} for x in v] for k,v in temps.items()})

try:
    import pynvml
    pynvml.nvmlInit()
    st.subheader("NVIDIA GPU")
    for i in range(pynvml.nvmlDeviceGetCount()):
        h=pynvml.nvmlDeviceGetHandleByIndex(i)
        util=pynvml.nvmlDeviceGetUtilizationRates(h)
        m=pynvml.nvmlDeviceGetMemoryInfo(h)
        st.write({"gpu":i,"utilization_percent":util.gpu,"memory_percent":round(100*m.used/m.total,2)})
except Exception:
    st.caption("NVIDIA GPU metrics are not available on this system.")

# Computer Resource Dashboard

A local Streamlit dashboard for CPU, memory, storage, network, temperature, and optional NVIDIA GPU utilization.

## Usage
```bash
pip install -r requirements.txt
streamlit run src/app.py
```

GPU metrics are shown when `pynvml` can initialize successfully. Temperature support depends on the operating system and hardware sensors exposed to `psutil`.

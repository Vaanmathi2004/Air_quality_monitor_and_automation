# IoT-Based Real-Time Indoor Air Quality Classification and Automated Ventilation Control Using KNN


IoT-based indoor air quality monitoring and automation system that uses a K-Nearest Neighbors (KNN) algorithm to classify air quality levels in real-time. It runs on a local server, with data processed and stored locally on your computer. The system automatically controls ventilation when pollutant levels are unsafe.

## Project Objectives
- **Real-Time Air Quality Monitoring**: Detect harmful indoor pollutants like VOCs, CO, and LPG.
- **Automated Ventilation Control**: Activate a fan when pollutant levels exceed safe thresholds.
- **Local Processing and Storage**: Run the system on a local server with data saved for offline analysis.

## System Components

### Hardware
- **MQ-6, MQ-9, and MQ-135 Gas Sensors**: Detect LPG, CO, and VOCs.
- **MCP3008 ADC**: Converts analog sensor signals to digital data for processing.
- **NodeMCU (ESP8266)**: Collects and processes data, classifies air quality, and controls the fan via relay.
- **Relay-Activated Fan**: Ventilation activated automatically when pollutant levels are high.

### Software
- **KNN Model**: Classifies air quality as "Good," "Moderate," or "Severe."
- **Local Server**: Processes and stores data on your computer, allowing for local control.
- **Excel Logging**: Saves data locally in Excel format for offline analysis.

## Project Workflow

1. **Data Collection**: Gas sensors detect pollutants, and their analog signals are converted to digital by MCP3008.
2. **Data Processing**: NodeMCU preprocesses the data and sends it to the local server for classification.
3. **Classification**: The KNN model classifies air quality and determines if ventilation is required.
4. **Automated Fan Control**: If air quality is “Severe,” the fan is activated to improve ventilation.
5. **Data Logging**: Saves real-time data to an Excel file on the local computer for future reference.

## Features
- **Local IoT Monitoring**: Operates entirely on a local server, avoiding the need for cloud storage.
- **Automatic Fan Control**: Reacts in real time to unsafe air quality by activating a fan.
- **High Classification Accuracy**: The KNN model achieves 93% accuracy for air quality classification.
- **Data Storage and Analysis**: Logs data locally for tracking air quality trends over time.

## Setup Instructions

### Prerequisites
- **Hardware**: NodeMCU (ESP8266), MCP3008 ADC, MQ-6, MQ-9, and MQ-135 gas sensors, relay module, fan.
- **Software**: Python 3.x, Arduino IDE, necessary libraries (`numpy`, `pandas`, `urllib`, `pickle`, `openpyxl` for Excel logging).

### Steps to Set Up

1. **Hardware Assembly**:
   - Connect MQ sensors to the MCP3008 ADC.
   - Link MCP3008 to NodeMCU for data transfer.
   - Set up the relay for fan control via the NodeMCU.
   - Power connections should be tested to ensure each sensor is working correctly.

2. **Software Installation**:
   - Clone the repository to your computer.
   - Install dependencies:
     ```bash
     pip install numpy pandas urllib3 openpyxl
     ```
   - Upload NodeMCU code from the Arduino IDE, setting it up to communicate with the local server.

3. **Running the System**:
   - Start data collection and processing with `data_collection.py` on your local server.
   - Run `knn_prediction.py` to classify sensor data and control the fan based on air quality.
   - Use `data_transfer_excel.py` to save data to an Excel file for analysis.

## Testing and Validation
- **Real-Time Testing**: Tested under conditions with varying pollutant levels. The system achieved rapid response times (2-3 seconds) and 93% accuracy for classifying air quality.
- **Local Data Analysis**: Saved data can be reviewed offline to track long-term air quality trends.

---

This project offers a complete, locally-run solution for monitoring and improving indoor air quality, making it suitable for a range of indoor spaces.

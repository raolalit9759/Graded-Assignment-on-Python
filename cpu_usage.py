import psutil
import time
import logging
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Define the CPU usage threshold
CPU_USAGE_THRESHOLD = 80.0  # percentage
def monitor_cpu_usage(threshold):
    logging.info("Starting CPU usage monitoring...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            logging.info(f"Current CPU usage: {cpu_usage}%")
            if cpu_usage > threshold:
                logging.warning(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("CPU usage monitoring stopped.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
if __name__ == "__main__":
    monitor_cpu_usage(CPU_USAGE_THRESHOLD)

import time
import random
import json

class Device:
    def __init__(self, device_id, device_type, location):
        self.device_id = device_id
        self.device_type = device_type
        self.location = location
        self.status = "idle"
        self.data = {}

    def start_operation(self, operation_name):
        print(f"[{self.device_id}] Starting operation: {operation_name}")
        self.status = "running"
        self.data = {"operation": operation_name, "start_time": time.time()}

    def collect_data(self):
        if self.status == "running":
            # Simulate data collection based on device type
            if self.device_type == "sensor":
                self.data["reading"] = round(random.uniform(10.0, 30.0), 2)
                self.data["timestamp"] = time.time()
            elif self.device_type == "actuator":
                self.data["state"] = random.choice(["on", "off"])
                self.data["timestamp"] = time.time()
            print(f"[{self.device_id}] Data collected: {self.data}")
        else:
            print(f"[{self.device_id}] Device is not running. No data collected.")

    def stop_operation(self):
        if self.status == "running":
            print(f"[{self.device_id}] Stopping operation.")
            self.status = "idle"
            self.data["end_time"] = time.time()
            print(f"[{self.device_id}] Final data: {self.data}")
            self.data = {}

    def get_status(self):
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "location": self.location,
            "status": self.status,
            "current_data": self.data
        }

# --- Simulation --- 

# Initialize devices for the osFoundry room
osfoundry_devices = [
    Device("temp-sensor-01", "sensor", "Room A"),
    Device("humidity-sensor-01", "sensor", "Room A"),
    Device("led-strip-01", "actuator", "Room A"),
    Device("fan-controller-01", "actuator", "Room B")
]

print("--- osFoundry Room Device Simulation ---")

# Simulate a sequence of operations
osfoundry_devices[0].start_operation("monitor_temperature")
osfoundry_devices[2].start_operation("set_lighting")

for _ in range(5):
    for device in osfoundry_devices:
        device.collect_data()
    time.sleep(1)

osfoundry_devices[0].stop_operation()
osfoundry_devices[2].stop_operation()

osfoundry_devices[3].start_operation("control_airflow")

for _ in range(3):
    for device in osfoundry_devices:
        device.collect_data()
    time.sleep(1)

osfoundry_devices[3].stop_operation()

print("--- Final Device Status ---")
for device in osfoundry_devices:
    print(json.dumps(device.get_status(), indent=2))

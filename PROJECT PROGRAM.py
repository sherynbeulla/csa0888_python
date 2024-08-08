import time
import random

# Define traffic light timings in seconds
RED_LIGHT_DURATION = 30
GREEN_LIGHT_DURATION = 30

class TrafficLight:
    def __init__(self, name):
        self.name = name
        self.state = 'RED'
        self.time_remaining = RED_LIGHT_DURATION

    def update_state(self):
        if self.state == 'RED':
            self.state = 'GREEN'
            self.time_remaining = GREEN_LIGHT_DURATION
        else:
            self.state = 'RED'
            self.time_remaining = RED_LIGHT_DURATION

    def countdown(self):
        if self.time_remaining > 0:
            self.time_remaining -= 1
        else:
            self.update_state()

    def __str__(self):
        return f"{self.name} Light: {self.state} ({self.time_remaining}s remaining)"

class TrafficSystem:
    def __init__(self):
        self.lights = [
            TrafficLight("North-South"),
            TrafficLight("East-West")
        ]

    def simulate_traffic(self):
        while True:
            for light in self.lights:
                light.countdown()
                print(light)
            
            # Simulate changes in traffic flow
            self.adjust_traffic_lights()

            print("\n" + "-"*40 + "\n")
            time.sleep(1)

    def adjust_traffic_lights(self):
        # Simulate adjusting traffic lights based on random traffic conditions
        if random.random() > 0.5:
            # Randomly switch light durations to simulate traffic conditions
            for light in self.lights:
                if light.state == 'RED':
                    light.time_remaining = RED_LIGHT_DURATION - random.randint(0, 10)
                else:
                    light.time_remaining = GREEN_LIGHT_DURATION - random.randint(0, 10)

if __name__ == "__main__":
    system = TrafficSystem()
    system.simulate_traffic()

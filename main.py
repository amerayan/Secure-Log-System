import datetime
import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

logs = []

def add_log(event, description):
    timestamp = str(datetime.datetime.now())

    if len(logs) == 0:
        previous_hash = "0"
    else:
        previous_hash = logs[-1]["current_hash"]

    data = timestamp + event + description + previous_hash
    current_hash = generate_hash(data)

    log = {
        "timestamp": timestamp,
        "event": event,
        "description": description,
        "previous_hash": previous_hash,
        "current_hash": current_hash
    }

    logs.append(log)

def show_logs():
    for i, log in enumerate(logs):
        print(f"\nLog {i}")
        for key, value in log.items():
            print(f"{key}: {value}")

# Test
add_log("LOGIN", "User logged in")
add_log("FILE", "Opened file")

show_logs()
def verify_logs():
    for i in range(1, len(logs)):
        current = logs[i]
        previous = logs[i - 1]

        # Check chain integrity
        if current["previous_hash"] != previous["current_hash"]:
            print(f"Tampering detected at log {i} (chain broken)")
            return False

        # Recalculate hash
        data = current["timestamp"] + current["event"] + current["description"] + current["previous_hash"]
        recalculated_hash = generate_hash(data)

        if current["current_hash"] != recalculated_hash:
            print(f"Tampering detected at log {i} (data modified)")
            return False

    print("All logs are secure ✅")
    return True
print("\nVerifying logs...")
verify_logs()
# Tampering simulation
logs[1]["description"] = "HACKED DATA"

print("\nAfter tampering:")
verify_logs()
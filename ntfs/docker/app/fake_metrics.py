import random
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Define a route to return fake metrics in JSON format
@app.route('/windows_metrics', methods=['GET'])
def get_os_windows_metrics():
    # Define a list of drives
    drives = ["C:", "D:", "E:"]

    # Generate random fake metrics
    cpu_usage = round(random.uniform(0, 100), 1)
    memory_usage = round(random.uniform(0, 100), 1)
    
    # Generate random disk usage data for each drive
    disk_usage = []
    for drive in drives:
        usage = round(random.uniform(20, 80), 1)
        disk_usage.append({
            "Drive": drive,
            "Usage": usage
        })

    # Create a JSON response
    metrics_data = {
        "CPU_usage": cpu_usage,
        "Memory_usage": memory_usage,
        "Disks": disk_usage
    }

    return jsonify(metrics_data)

@app.route('/linux_metrics', methods=['GET'])
def get_os_linux_metrics():
    # Define a list of drives
    drives = ["/", "/home", "/var"]

    # Generate random fake metrics
    cpu_usage = round(random.uniform(0, 100), 1)
    memory_usage = round(random.uniform(0, 100), 1)
    swap_usage = round(random.uniform(50, 100), 1)
    
    # Generate random disk usage data for each drive
    disk_usage = []
    for drive in drives:
        usage = round(random.uniform(20, 80), 1)
        inode = round(random.uniform(1, 50), 1)
        disk_usage.append({
            "Drive": drive,
            "Usage": usage,
            "inode": inode
        })

    # Create a JSON response
    metrics_data = {
        "CPU_usage": cpu_usage,
        "Memory_usage": memory_usage,
        "Swap_usage": swap_usage,
        "Disks": disk_usage
    }

    return jsonify(metrics_data)


# Define a route for fake IIS metrics
@app.route('/iis_metrics', methods=['GET'])
def get_fake_iis_metrics():
    # Generate random IIS-related metrics
    requests_per_second = round(random.uniform(0, 100), 2)
    active_connections = random.randint(0, 500)
    
    # Create a JSON response for IIS metrics
    iis_metrics_data = {
        "Requests_per_second": requests_per_second,
        "Active_connections": active_connections
    }

    return jsonify(iis_metrics_data)

# Define a route for fake IIS metrics
@app.route('/nginx_metrics', methods=['GET'])
def get_fake_nginx_metrics():

    # Create a JSON response for IIS metrics
    metrics_data = {
            "accepted": random.randint(0, 500),
            "active": random.randint(0, 500),
            "dropped": random.randint(0, 200),
            "handled": random.randint(0, 500),
            "reading": random.randint(0, 150),
            "writing": random.randint(0, 150),
            "resquests": random.randint(0, 500),
            "total": random.randint(0, 500),
            "version":1.0,
            "status":200
        }

    return jsonify(metrics_data)

# Define a route for fake Oracle Database metrics
@app.route('/oracle_metrics', methods=['GET'])
def get_fake_oracle_metrics():
    # Generate random Oracle Database-related metrics
    query_response_time = round(random.uniform(10, 1000), 2)
    active_sessions = random.randint(0, 100)

    # Generate random tablespace usage data
    tablespace_usage = []
    for tablespace in ["USERS", "DATA", "INDEX", "SYSDASTA"]:
        usage = round(random.uniform(0, 100), 2)
        tablespace_usage.append({
            "table" : tablespace,
            "usage" : usage
        })
  
    # Create a JSON response for Oracle Database metrics
    oracle_metrics_data = {
        "Query_response_time_ms": query_response_time,
        "Active_sessions": active_sessions,
        "Tablespace_usage_percent": tablespace_usage
    }

    return jsonify(oracle_metrics_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

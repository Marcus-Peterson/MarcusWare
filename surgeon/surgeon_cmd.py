import os
import psutil
import subprocess
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health_check.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """Runs a system command and logs the output."""
    try:
        logging.info(f"Running command: {command}")
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        logging.info(result.stdout)
        if result.stderr:
            logging.error(result.stderr)
    except Exception as e:
        logging.error(f"Error running command '{command}': {e}")

def check_cpu_usage(threshold=80):
    """Checks if CPU usage is above the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")

def check_memory_usage(threshold=500):  # threshold in MB
    """Checks if available memory is below the threshold."""
    available_memory = psutil.virtual_memory().available / (1024 * 1024)  # Convert to MB
    if available_memory < threshold:
        logging.warning(f"Low available memory: {available_memory:.2f} MB")
    else:
        logging.info(f"Available memory is sufficient: {available_memory:.2f} MB")

def check_disk_usage(threshold=20):  # threshold in percentage
    """Checks if disk usage is above the threshold."""
    total, used, free = shutil.disk_usage("C:\\")
    free_percent = (free / total) * 100
    if free_percent < threshold:
        logging.warning(f"Low disk space: {free_percent:.2f}% free")
    else:
        logging.info(f"Disk space is sufficient: {free_percent:.2f}% free")

def check_smart_status():
    """Checks the SMART status of disk drives."""
    command = "wmic diskdrive get model,status"
    run_command(command)

def check_network_configuration():
    """Checks the network configuration."""
    command = "ipconfig /all"
    run_command(command)

def check_system_info():
    """Retrieves detailed system information."""
    command = "systeminfo"
    run_command(command)

def check_power_efficiency():
    """Generates a power efficiency report."""
    command = "powercfg /energy"
    run_command(command)

def run_dism_checks():
    """Runs DISM health checks."""
    commands = [
        "DISM /Online /Cleanup-Image /CheckHealth",
        "DISM /Online /Cleanup-Image /ScanHealth",
        "DISM /Online /Cleanup-Image /RestoreHealth"
    ]
    for cmd in commands:
        run_command(cmd)

def run_memory_diagnostics():
    """Schedules Windows Memory Diagnostic tool to run on next reboot."""
    command = "mdsched.exe"
    run_command(command)

def check_event_logs():
    """Retrieves the last 10 entries from the System event log."""
    command = "wevtutil qe System /c:10 /f:text"
    run_command(command)

def run_driver_verifier():
    """Runs Driver Verifier to identify problematic drivers."""
    command = "verifier /standard /all"
    run_command(command)

def reset_network_settings():
    """Resets network settings to fix connectivity issues."""
    command = "netsh winsock reset"
    run_command(command)

def main():
    logging.info("Starting system health check")

    # Run System File Checker
    run_command("sfc /scannow")

    # Run DISM checks
    run_dism_checks()

    # Run Check Disk
    run_command("chkdsk C: /f")

    # Check system resources
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()

    # Additional checks
    check_smart_status()
    check_network_configuration()
    check_system_info()
    check_power_efficiency()
    run_memory_diagnostics()
    check_event_logs()
    run_driver_verifier()
    reset_network_settings()

    logging.info("System health check completed")

if __name__ == "__main__":
    main()

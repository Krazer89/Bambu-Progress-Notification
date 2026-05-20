# =============================================================================
# CONFIGURATION TEMPLATE
# =============================================================================
# Copy this file to config.py and fill in your values:
#   cp config.example.py config.py
#
# This config file is compatible with both Bambu Progress Notification and FilamentTracker.
# You can copy config.py between the two projects — each will use what it
# needs and ignore settings for the other.

# =============================================================================
# Bambu MQTT Connection Mode - Cloud or LAN
# =============================================================================
# Set to True to connect to printer directly on LAN (developer/local mode)
# Set to False to connect to Bambu Cloud (default)
BAMBU_USE_LAN_MODE = False

# =============================================================================
# Bambu Cloud MQTT Configuration (required if BAMBU_USE_LAN_MODE = False)
# =============================================================================
# Server: "us.mqtt.bambulab.com" for most users, "cn.mqtt.bambulab.com" for China
BAMBU_MQTT_SERVER = "us.mqtt.bambulab.com"
BAMBU_MQTT_PORT = 8883

# Your Bambu Lab account user ID (numeric)
# How to find: Run python3 get_credentials.py
BAMBU_USER_ID = "YOUR_USER_ID_HERE"

# Your Bambu Lab access token
BAMBU_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN_HERE"

# Your printer's serial number
# How to find: Bambu Handy app -> Printer settings, or printed on the printer
BAMBU_PRINTER_SERIAL = "YOUR_PRINTER_SERIAL_HERE"

# =============================================================================
# Bambu LAN MQTT Configuration (required if BAMBU_USE_LAN_MODE = True)
# =============================================================================
# Printer's local IP address on your network
BAMBU_PRINTER_IP = "YOUR_PRINTER_IP_HERE"  # e.g., "192.168.1.100"

# LAN access code (aka dev_access_code from Device object)
# How to find: Check your printer's local network settings or API documentation
BAMBU_LAN_ACCESS_CODE = "YOUR_LAN_ACCESS_CODE_HERE"

# Skip TLS certificate verification (for self-signed certificates)
# Set to True for LAN mode (printer uses self-signed cert)
# Set to False for Cloud mode (uses valid Bambu certificate)
BAMBU_TLS_SKIP_VERIFY = False  # Default: skip verification for LAN safety

# =============================================================================
# Filament Tracker Settings
# =============================================================================
# These are used by the FilamentTracker service.
# If running Bambu Progress Notification only, you can leave these as defaults.

FILAMENT_TRACKER_PORT = 5000
FILAMENT_TRACKER_HOST = "0.0.0.0"  # Listen on all interfaces

# Optional API key to protect write endpoints (PATCH/DELETE/POST).
# Leave empty to allow unrestricted access (original behavior).
# Can also be set via FILAMENT_TRACKER_API_KEY environment variable.
FILAMENT_TRACKER_API_KEY = ""

# Alert when a spool drops below this weight (grams). Set to 0 to disable.
FILAMENT_LOW_ALERT_GRAMS = 150

# Send FCM push notification when filament is low (requires notifications)
FILAMENT_LOW_ALERT_FCM = False

# =============================================================================
# Notification Service Settings (FCM / Firebase)
# =============================================================================
# These are used by the Bambu Progress Notification service.
# If running FilamentTracker only, you can leave these as defaults.

# Path to your Firebase service account JSON file
FIREBASE_CREDENTIALS_FILE = "firebase-service-account.json"

# Your Android device's FCM token(s)
# How to get: Open the Bambu Progress Notification Android app -> tap "Copy FCM Token"
FCM_DEVICE_TOKENS = [
    "YOUR_FCM_TOKEN_HERE",
]

# =============================================================================
# iOS Live Activity (APNs) Configuration — OPTIONAL
# =============================================================================
# Leave these empty if you don't have an iOS device.

APNS_KEY_FILE = ""          # e.g., "AuthKey_XXXXXXXXXX.p8"
APNS_TEAM_ID = ""           # e.g., "ABCDE12345"
APNS_KEY_ID = ""            # e.g., "XXXXXXXXXX"
APNS_BUNDLE_ID = "com.elliot.bamboonowbar"
APNS_USE_SANDBOX = True
APNS_PRINTER_NAME = "Bambu Lab"

# =============================================================================
# Cross-Service Integration — OPTIONAL
# =============================================================================
# If you have both Bambu Progress Notification and FilamentTracker cloned as sibling folders:
#   YourFolder/
#     Bambu-Progress-Notification/
#     FilamentTracker/
#
# You can enable the other service here to run both on a single MQTT connection.

# Set True in Bambu Progress Notification to also run the filament tracker
ENABLE_FILAMENT_TRACKER = False

# Set True in FilamentTracker to also run the notification service
ENABLE_NOTIFICATIONS = False

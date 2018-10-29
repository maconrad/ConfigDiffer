
#Program Version
VERSION = "v1"

#General Definitions
ROUTER_TEMPLATE = "../Files/Templates/router_eigrp_templ.json"
INTERFACE_TEMPLATE = "../Files/Templates/interface_templ.json"
RADIUS_TEMPLATE = "../Files/Templates/radius_all_templ.json"
DEVICE_SENSOR_TEMPLATE = "../Files/Templates/device_sensor_templ.json"

#Templates to Verify
TEMPLATES = [
    ROUTER_TEMPLATE,
    INTERFACE_TEMPLATE,
    RADIUS_TEMPLATE,
    DEVICE_SENSOR_TEMPLATE
]

#USER Config
USER_CONFIG = "../Files/SampleCfgs/Test1_Correct.txt"
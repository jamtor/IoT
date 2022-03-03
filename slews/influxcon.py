from lib2to3.pgen2 import token
from django.conf import settings
from influxdb import InfluxDBClient



def get_influxdb_client():
    """Returns an ``InfluxDBClient`` instance."""
    client = InfluxDBClient(
    settings.INFLUXDB_HOST,
    settings.INFLUXDB_PORT,
    settings.INFLUXDB_USERNAME,
    settings.INFLUXDB_PASSWORD,
    settings.INFLUXDB_DATABASE,
    timeout=settings.INFLUXDB_TIMEOUT)
    return client

# def get_influxdb_client():
#     token = "fHB2-LGCVmxTDhpuHyQVI2KSH3Pv1yCzk3AD8YqA-EVWypG47yWRokbHxs8wc9CuJRN9mOKzsXxFPwmN8VGCkA=="
#     org = "DOST9"
#     bucket = "dost"
#     client = InfluxDBClient(url="http://192.168.1.78:8086", token=token, org=org)
#     return client



# You can generate an API token from the "API Tokens Tab" in the UI
# token = "fHB2-LGCVmxTDhpuHyQVI2KSH3Pv1yCzk3AD8YqA-EVWypG47yWRokbHxs8wc9CuJRN9mOKzsXxFPwmN8VGCkA=="
# org = "DOST9"
# bucket = "dost"

# with InfluxDBClient(url="http://192.168.1.78:8086", token=token, org=org) as client:

import os
from collections import namedtuple

# getting content root directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

OUTPUT_DIR = os.path.join(parent, "activities")
GPX_FOLDER = os.path.join(parent, "GPX_OUT")
TCX_FOLDER = os.path.join(parent, "TCX_OUT")
FIT_FOLDER = os.path.join(parent, "FIT_OUT")
PNG_FOLDER = os.path.join(parent, "PNG_OUT")
ENDOMONDO_FILE_DIR = os.path.join(parent, "Workouts")
FOLDER_DICT = {
    "gpx": GPX_FOLDER,
    "tcx": TCX_FOLDER,
    "fit": FIT_FOLDER,
}
SQL_FILE = os.path.join(parent, "run_page", "data.db")
JSON_FILE = os.path.join(parent, "src", "static", "activities.json")
SYNCED_FILE = os.path.join(parent, "imported.json")
SYNCED_ACTIVITY_FILE = os.path.join(parent, "synced_activity.json")

# TODO: Move into nike_sync NRC THINGS


BASE_TIMEZONE = "Asia/Shanghai"
UTC_TIMEZONE = "UTC"

start_point = namedtuple("start_point", "lat lon")
run_map = namedtuple("polyline", "summary_polyline")

# add more type here
# add more type here
TYPE_DICT = {
    "running": "Run",
    "RUN": "Run",
    "Run": "Run",
    "track_running": "Run",
    "trail_running": "Trail Run",
    "cycling": "Ride",
    "CYCLING": "Ride",
    "Ride": "Ride",
    "EBikeRide": "Ride",
    "E-Bike": "Ride",
    "road_biking": "Ride",
    "Road Bike": "Ride",
    "Mountain Bike": "Ride",
    "VirtualRide": "VirtualRide",
    "indoor_cycling": "Indoor Ride",
    "Indoor Bike ": "Indoor Ride",
    "walking": "Hike",
    "hiking": "Hike",
    "Walk": "Hike",
    "Hike": "Hike",
    "Swim": "Swim",
    "swimming": "Swim",
    "Pool Swim": "Swim",
    "Open Water": "Swim",
    "rowing": "Rowing",
    "RoadTrip": "RoadTrip",
    "flight": "Flight",
    "kayaking": "Kayaking",
    "Snowboard": "Snowboard",
    "resort_skiing_snowboarding_ws": "Ski",  # garmin
    "AlpineSki": "Ski",  # strava
    "Ski": "Ski",
    "Indoor_Running": "Indoor Running",
    "Strength_Training": "Strength Training",
    "Floor_Climbing": "Floor Climbing",
    "Elliptical": "Elliptical",
}

MAPPING_TYPE = [
    "Hike",
    "Ride",
    "VirtualRide",
    "Rowing",
    "Run",
    "Trail Run",
    "Swim",
    "RoadTrip",
    "Kayaking",
    "Snowboard",
    "Ski",
    "Indoor Running",
    "Strength Training",
    "Floor Climbing",
    "Elliptical",
]
STRAVA_GARMIN_TYPE_DICT = {
    "Hike": "hiking",
    "Run": "running",
    "EBikeRide": "cycling",
    "Walk": "walking",
    "Swim": "swimming",
}

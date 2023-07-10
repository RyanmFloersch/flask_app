# motion jpeg streamer server

import  cv2
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import argparse
from opecvutils import Camera
import socket as Socket
from opencvutils import __version__ as VERSION
import os
import re



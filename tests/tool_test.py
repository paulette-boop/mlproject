# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
  lat1, lon1 = 48.865070, 2.380009
  lat2, lon2 = 51.357335,-0.1904432
  distance = 332.21369695800894

  assert haversine(lon1, lat1, lon2, lat2) == distance

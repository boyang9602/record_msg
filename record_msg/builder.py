#!/usr/bin/env python

# Copyright 2022 daohu527 <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cv2
import logging
import numpy as np
import time
from google.protobuf import json_format

from record_msg import pypcd

from modules.common_msgs.sensor_msgs import sensor_image_pb2, pointcloud_pb2, imu_pb2, gnss_best_pose_pb2
from modules.common_msgs.localization_msgs import localization_pb2
from modules.common_msgs.transform_msgs import transform_pb2

from record_msg.time_conversion import Unix2Gps

class Builder(object):
  def __init__(self) -> None:
    self._sequence_num = 0

  def _build_header(self, header,
      t=None, module_name=None, version=None, frame_id=None):
    header.sequence_num = self._sequence_num
    if t:
      header.timestamp_sec = t
      # todo(zero): no need to add?
      # header.camera_timestamp = int(t * 1e9)
      # header.lidar_timestamp = int(t * 1e9)
    if module_name:
      header.module_name = module_name
    if version:
      header.version = version
    if frame_id:
      header.frame_id = frame_id


class TransformBuilder(Builder):
  def __init__(self) -> None:
    super().__init__()

  def build(self, frame_id, child_frame_id, translation, rotation, t):
    pb_transformstampeds = transform_pb2.TransformStampeds()
    pb_transformstamped = pb_transformstampeds.transforms.add()
    if t is None:
      t = time.time()

    self._build_header(pb_transformstamped.header, t=t, frame_id=frame_id)
    pb_transformstamped.child_frame_id = child_frame_id
    pb_transformstamped.transform.translation.x = translation[0]
    pb_transformstamped.transform.translation.y = translation[1]
    pb_transformstamped.transform.translation.z = translation[2]

    pb_transformstamped.transform.rotation.qw = rotation[0]
    pb_transformstamped.transform.rotation.qx = rotation[1]
    pb_transformstamped.transform.rotation.qy = rotation[2]
    pb_transformstamped.transform.rotation.qz = rotation[3]

    self._sequence_num += 1
    return pb_transformstampeds


class LocalizationBuilder(Builder):
  def __init__(self) -> None:
    super().__init__()

  def build(self, translation, rotation, heading, measurement_time, t = None):
    pb_localization = localization_pb2.LocalizationEstimate()
    if t is None:
      t = time.time()

    self._build_header(pb_localization.header, t=t, module_name='localization')
    pb_localization.pose.position.x = translation[0]
    pb_localization.pose.position.y = translation[1]
    pb_localization.pose.position.z = translation[2]

    pb_localization.pose.orientation.qw = rotation[0]
    pb_localization.pose.orientation.qx = rotation[1]
    pb_localization.pose.orientation.qy = rotation[2]
    pb_localization.pose.orientation.qz = rotation[3]

    pb_localization.pose.heading = heading

    # todo(zero): need to complete
    # pb_localization.pose.linear_velocity
    # pb_localization.pose.linear_acceleration
    # pb_localization.pose.angular_velocity

    pb_localization.measurement_time = measurement_time
    self._sequence_num += 1
    return pb_localization

class IMUBuilder(Builder):
  def __init__(self) -> None:
    super().__init__()

  def build(self, ax, ay, az, wx, wy, wz,
            measurement_time, measurement_span = None,
            measurement_time_is_unix_time = True, t = None):
    pb_imu = imu_pb2.Imu()
    if t is None:
      t = time.time()
    self._build_header(pb_imu.header, t=t)

    if measurement_time_is_unix_time:
      pb_imu.measurement_time = Unix2Gps(measurement_time)
    else:
      pb_imu.measurement_time = measurement_time

    if measurement_span is not None:
      pb_imu.measurement_span = measurement_span

    pb_imu.linear_acceleration.x = ax
    pb_imu.linear_acceleration.y = ay
    pb_imu.linear_acceleration.z = az

    pb_imu.angular_velocity.x = wx
    pb_imu.angular_velocity.y = wy
    pb_imu.angular_velocity.z = wz

    self._sequence_num += 1
    return pb_imu

class GnssBestPoseBuilder(Builder):
  def __init__(self) -> None:
    super().__init__()

  def build(self, measurement_time,
            latitude, longitude, height_msl, undulation,
            latitude_std_dev, longitude_std_dev, height_std_dev,
            sol_status, sol_type,
            num_sats_tracked, num_sats_in_solution, num_sats_l1, num_sats_multi,
            datum_id = gnss_best_pose_pb2.DatumId.WGS84,
            base_station_id = None,
            differential_age = None, solution_age = None,
            extended_solution_status = None,
            galileo_beidou_used_mask = None,
            gps_glonass_used_mask = None,
            measurement_time_is_unix_time = True,
            t = None):
    pb_gnss_best_pose = gnss_best_pose_pb2.GnssBestPose()
    if t is None:
      t = time.time()
    self._build_header(pb_gnss_best_pose.header, t=t)

    if measurement_time_is_unix_time:
      pb_gnss_best_pose.measurement_time = Unix2Gps(measurement_time)
    else:
      pb_gnss_best_pose.measurement_time = measurement_time

    pb_gnss_best_pose.latitude = latitude
    pb_gnss_best_pose.longitude = longitude
    pb_gnss_best_pose.height_msl = height_msl
    pb_gnss_best_pose.undulation = undulation
    pb_gnss_best_pose.latitude_std_dev = latitude_std_dev
    pb_gnss_best_pose.longitude_std_dev = longitude_std_dev
    pb_gnss_best_pose.height_std_dev = height_std_dev
    pb_gnss_best_pose.sol_status = sol_status
    pb_gnss_best_pose.sol_type = sol_type
    pb_gnss_best_pose.num_sats_tracked = num_sats_tracked
    pb_gnss_best_pose.num_sats_in_solution = num_sats_in_solution
    pb_gnss_best_pose.num_sats_l1 = num_sats_l1
    pb_gnss_best_pose.num_sats_multi = num_sats_multi
    pb_gnss_best_pose.datum_id = datum_id

    if base_station_id is not None:
      pb_gnss_best_pose.base_station_id = base_station_id
    if differential_age is not None:
      pb_gnss_best_pose.differential_age = differential_age
    if solution_age is not None:
      pb_gnss_best_pose.solution_age = solution_age
    if extended_solution_status is not None:
      pb_gnss_best_pose.extended_solution_status = extended_solution_status
    if galileo_beidou_used_mask:
      pb_gnss_best_pose.galileo_beidou_used_mask = galileo_beidou_used_mask
    if gps_glonass_used_mask:
      pb_gnss_best_pose.gps_glonass_used_mask = gps_glonass_used_mask

    self._sequence_num += 1
    return pb_gnss_best_pose

class ImageBuilder(Builder):
  def __init__(self) -> None:
    super().__init__()

  def _to_flag(self, encoding):
    if encoding == 'rgb8' or encoding == 'bgr8':
      return cv2.IMREAD_COLOR
    elif encoding == 'gray' or encoding == 'y':
      return cv2.IMREAD_GRAYSCALE
    else:
      print('Unsupported image encoding type: %s.' % encoding)
      return None

  def build(self, file_name, frame_id, encoding, measurement_time, t=None):
    pb_image = sensor_image_pb2.Image()
    flag = self._to_flag(encoding)
    if flag is None:
      return

    if t is None:
      t = time.time()

    self._build_header(pb_image.header, frame_id=frame_id)
    pb_image.frame_id = frame_id
    pb_image.measurement_time = measurement_time
    pb_image.encoding = encoding

    img = cv2.imread(file_name, flag)

    if flag == cv2.IMREAD_COLOR:
      pb_image.height, pb_image.width, channels = img.shape
      pb_image.step = pb_image.width * channels
    elif flag == cv2.IMREAD_GRAYSCALE:
      pb_image.height, pb_image.width = img.shape
      pb_image.step = pb_image.width
    else:
      return

    pb_image.data = img.tostring()
    self._sequence_num += 1
    return pb_image


class PointCloudBuilder(Builder):
  def __init__(self, dim=4) -> None:
    super().__init__()
    self._dim = dim

  def build(self, file_name, frame_id, measurement_time, t=None):
    pb_point_cloud = pointcloud_pb2.PointCloud()

    if t is None:
      t = time.time()

    self._build_header(pb_point_cloud.header, t=t, frame_id=frame_id)
    pb_point_cloud.frame_id = frame_id
    # pb_point_cloud.is_dense = False
    pb_point_cloud.measurement_time = measurement_time

    point_cloud = pypcd.point_cloud_from_path(file_name)

    pb_point_cloud.width = point_cloud.width
    pb_point_cloud.height = point_cloud.height

    for data in point_cloud.pc_data:
      point = pb_point_cloud.point.add()
      point.x, point.y, point.z, point.intensity, timestamp = data
      point.timestamp = int(timestamp * 1e9)

    self._sequence_num += 1
    return pb_point_cloud

  def build_nuscenes(self, file_name, frame_id, measurement_time, t=None,
                     lidar_transform=np.identity(4), intensity_scale_factor=1.0):
    pb_point_cloud = pointcloud_pb2.PointCloud()

    if t is None:
      t = time.time()

    self._build_header(pb_point_cloud.header, t=t, frame_id=frame_id)
    pb_point_cloud.frame_id = frame_id
    # pb_point_cloud.is_dense = False
    pb_point_cloud.measurement_time = measurement_time

    # Loads LIDAR data from binary numpy format.
    # Data is stored as (x, y, z, intensity, ring index).
    if file_name.endswith('.bin'):
      scan = np.fromfile(file_name, dtype=np.float32)
    elif file_name.endswith('.txt'):
      scan = np.loadtxt(file_name, dtype=np.float32)
    else:
      raise RuntimeError("Unsupported file extension.")

    points = scan.reshape((-1, self._dim))[:, :4]
    intensities = (points[:, -1] * intensity_scale_factor).astype(np.uint8)
    points = points @ lidar_transform

    pb_point_cloud.width = len(points)
    pb_point_cloud.height = 1

    # Points shape is (length, 4)
    n0, _ = np.shape(points)
    for i in range(n0):
      point = pb_point_cloud.point.add()
      point.intensity = intensities[i]
      points[i][3] = 1
      point.x, point.y, point.z, _ = points[i]
    self._sequence_num += 1
    return pb_point_cloud

import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/leejunmi/ros2_ws/install/microstrain_inertial_rqt'

from setuptools import find_packages, setup

package_name = 'lidar_intensity'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leejunmi',
    maintainer_email='jm051020@naver.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 's=lidar_intensity.lidar_intensity:main',
        'marker=lidar_intensity.create_marker:main',
        'noise_marker=lidar_intensity.create_marker_noise:main',
        ],
    },
)

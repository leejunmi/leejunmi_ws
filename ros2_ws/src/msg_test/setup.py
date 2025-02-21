from setuptools import find_packages, setup

package_name = 'msg_test'

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
    maintainer_email='leejunmi@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    
  #수정: run할때 실행시킬 이름, node 추가
    entry_points={
        'console_scripts': [ 'p=msg_test.pub:main','s=msg_test.sub:main',

        ],
    },
)

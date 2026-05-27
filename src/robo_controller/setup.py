from setuptools import find_packages, setup

package_name = 'robo_controller'

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
    maintainer='bhuwan',
    maintainer_email='bhuwanadhikari775@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        "test_node=robo_controller.first_node:main",
        "draw_circle=robo_controller.publisher:main",
        "pos_subscriber=robo_controller.sub:main",
        "crash_avoid=robo_controller.smart_turtle:main",
        "random_rotate=robo_controller.rndm_trtl:main",
        "add_server=robo_controller.server:main",
        "add_client=robo_controller.client:main",
        "colour_client=robo_controller.colour_client:main",
        "colour_server=robo_controller.colour_server:main"

        ],
    },
)

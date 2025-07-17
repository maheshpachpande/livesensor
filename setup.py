from setuptools import setup, find_packages


def get_requirements()-> list:
    
    requirements = list[str] = []
    
    return requirements


setup(
    name='sensorClassifier',
    version='0.1.0',
    description='A machine learning project for sensor data classification',
    author='Mahesh',
    author_email='pachpandemahesh300@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # 👈 Important fix!
    python_requires='>=3.9, <4.0',
    install_requires=get_requirements()
)

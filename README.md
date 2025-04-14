# Memo: using in conda.yaml

pip download --index-url https://test.pypi.org/simple/ test-app-hommat==0.0.3

downloads locally the .whl  
add the library to your conda and run your tests  

## conda.yaml

channels:
  - conda-forge

dependencies:
  - python=3.12.8                 # https://pyreadiness.org/3.10
  - pip=24.3.1                    # https://pip.pypa.io/en/stable/news
  - robocorp-truststore=0.8.0     # https://pypi.org/project/robocorp-truststore/
  - pip:
    - rpaframework==30.0.1        # https://rpaframework.org/releasenotes.html
    - robocorp==2.1.3             # https://pypi.org/project/robocorp
    - robocorp-browser==2.3.4     # https://pypi.org/project/robocorp-browser
    - ./test_app_hommat-0.0.3-py3-none-any.whl

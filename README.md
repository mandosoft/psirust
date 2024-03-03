This is a test bench for examining issues with symmetry and how they may be rectified. 

I'm using [PyO3](https://pyo3.rs/v0.20.3/) for Rust bindings and the `information` library [crate](https://docs.rs/information/latest/information/mutual/fn.mutual_information.html).

First ensure you have [Rust](https://www.rust-lang.org/tools/install) installed:
`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

Create a python virtual environment and install requirements:
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Next have maturin build the library funtion and install it into the virtual environment:
`
maturin develop
`

From there you can run `python3 symmetry_test.py` to operate the test bench script.

use pyo3::prelude::*;
use information::{prob2d, mutual_information};
use approx::assert_relative_eq;
use numpy::PyReadonlyArray1;


/// Tests the ability to access the Rust Mutual Information function
/// from the Python interpreter
///
/// An initial test yields an interesting result:
/// Even with uniformly random elements, some deviation is bound to occur
/// So the objective is to cap the deviation to within e-14
///


#[pyfunction]
fn mut_info_t(_py: Python, x: PyReadonlyArray1<usize>, y: PyReadonlyArray1<usize>) -> (f64, f64) {

    let c_x = x.as_array().to_owned();
    let c_y = y.as_array().to_owned();

    //let c_x_bins = c_x.len();
    //let c_y_bins = c_y.len();

    let p_xy = prob2d(&c_x, &c_y, 21, 21).unwrap();
    let p_yx = prob2d(&c_y, &c_x, 21, 21).unwrap();

    let i_xy = mutual_information(&p_xy);
    let i_yx = mutual_information(&p_yx);

    // Measures: I(X;Y) = I(Y;X)
    assert_relative_eq!(i_xy, i_yx, epsilon=1e-14);

    (i_xy, i_yx)
}



/// A Python module implemented in Rust.
#[pymodule]
fn psirust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(mut_info_t, m)?)?;
    Ok(())
}

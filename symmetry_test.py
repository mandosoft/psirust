#!/usr/bin/env python3
import maturin
import psicalc as pc
import psirust as pr
import numpy as np

from sklearn.metrics.cluster import normalized_mutual_info_score as sk_nmis
from psicalc.nmi import normalized_mutual_info_score as nmis

# First read in test msa
file = 'TOP2A_protein_105species REV trunc to HTIIa d.csv'
df = pc.read_csv_file_format(file)

# Now we just want the first two columns to validate with
two_cols = df.iloc[:, :2]
print(two_cols)

# Next do the usual cleansing
encoded_df = pc.encode_msa(two_cols)

# These are the columns we'll use to measure differences
c_x = encoded_df[:, 0]
c_y = encoded_df[:, 1]

# First we run the PsiCalc Version
control_rii_xy = nmis(c_x, c_y)
control_rii_yx = nmis(c_y, c_x)
control_rii = (control_rii_xy, control_rii_yx)
print("\nPsiCalc rii between two columns: ", control_rii)

# Now we run the rust version. The mutual info library complains
# if not using uint for 1d Arrays
uc_x = c_x.astype(np.uint64)
uc_y = c_x.astype(np.uint64)
rust_rii = pr.mut_info_t(uc_x, uc_y)
print("\nRust rii between two columns: ", rust_rii)

# Finally we use the most recent version of the scikit library
scikit_rii_xy = sk_nmis(c_x, c_y)
scikit_rii_yx = sk_nmis(c_y, c_x)
scikit_rii = (scikit_rii_xy, scikit_rii_yx)
print("\nPython scikit library rii between two columns: ", scikit_rii)

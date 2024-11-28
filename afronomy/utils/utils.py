import numpy as np
from daskms import xds_from_table
from africanus.rime.predict import predict_vis
from africanus.averaging.support import unique_time


def DFT():
    pass

def dask_DFT():
    pass

def corrupt_vis(msname, column, n_dir=1):
    xds = xds_from_table(msname)[0]
    model = xds[column]
    ant1 = xds["ANTENNA1"]
    ant2 = xds["ANTENNA2"]
    time = xds["TIME"]
    #time_index = np.unique(time.values, return_inverse=True)[1]
    _, time_index, _, n_time = unique_time(time.values)
    n_time = np.unique(n_time)[0]
    n_ant =  len(np.unique(ant1.values))
    # Read the measurement set and extract relevant information
    pol_name = "::".join((msname, "POLARIZATION"))
    field_name = "::".join((msname, "FIELD"))
    spwname = "::".join((msname, "SPECTRAL_WINDOW"))
    pols = xds_from_table(pol_name)[0]
    spwds = xds_from_table(spwname)[0]
    fieldds = xds_from_table(field_name)[0]
    frequency = spwds['CHAN_FREQ'].values.squeeze()
    n_chan = len(frequency)
    corr_shape = len(pols.NUM_CORR.values)
    # simulate gains (just randomly scattered around 1 for now)
    jones = np.ones((n_time, n_ant, n_chan, n_dir) +
                    (corr_shape,), dtype=np.complex128)
    # Add random perturbations
    perturbation_scale = 0.1  # Scale of random perturbations
    jones += perturbation_scale * (np.random.randn(*jones.shape) +
                               1j * np.random.randn(*jones.shape))
    #jones = np.transpose(jones, [3, 0, 1, 2, 4])
    #model = np.transpose(model, [2, 0, 1, 3])
    corrupt_vis = predict_vis(time_index,
                              ant1.values,
                              ant2.values,
                              base_vis=model.values,
                              dde1_jones=jones,
                              dde2_jones=jones)
    return corrupt_vis

def compute_res(xds, column):
    model = xds[column]
    vis = xds['DATA']
    ant1 = xds["ANTENNA1"]
    ant2 = xds["ANTENNA2"]
    compute_res = []
    return compute_res

def correct_obs(xds, column):
    vis = xds[column]
    time = xds["TIME"]
    _, time_bin_indices, _, time_bin_counts = unique_time(time)
    ant1 = xds["ANTENNA1"]
    ant2 = xds["ANTENNA2"]
    jones = xds["JONES"]
    flag = xds["FLAG"]
    corrected_vis = correct_vis(time_bin_indices, time_bin_counts,
                                ant1, ant2, jones, vis, flag)
    return corrected_vis

import h5py
import numpy as np
import sys
sys.path.append(r"C:\Users\ricca\Documents\Unimib-Code\AstroStatistics\Notebooks\Exam")
#C:\Users\Phisio97\Documents\Astrostatistics\Notebooks\Exam
from LIGO_Utils.LigoUtils import load_data, downsample_unbalanced
#from LIGO.LIGO_Utils.LIGOUTILS import load_data, downsample_balanced, downsample_unbalanced

data_path = r"C:\Users\ricca\Documents\Unimib-Code\AstroStatistics\Notebooks\Exam\LIGO\Npy\LIGO.h5"
#C:\Users\Phisio97\Downloads\LIGO.h5
y, data, keys = load_data(data_path)
y, data = downsample_unbalanced(data, y, 100000, 42)

print('Saving DS data...')
np.save(r'C:\Users\ricca\Documents\Unimib-Code\AstroStatistics\Notebooks\Exam\LIGO\LIGO_v2\Npy\y.npy', y)
np.save(r'C:\Users\ricca\Documents\Unimib-Code\AstroStatistics\Notebooks\Exam\LIGO\LIGO_v2\Npy\data.npy', data)
np.save(r'C:\Users\ricca\Documents\Unimib-Code\AstroStatistics\Notebooks\Exam\LIGO\LIGO_v2\Npy\keys.npy', keys)
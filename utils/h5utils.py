import h5py
import numpy as np
from pathlib import Path
from typing import Union


def write_data_to_h5(data: np.ndarray, filename: Union[str, Path], dtype="uint8", verbose=False):
	with h5py.File(filename if isinstance(filename, str) else str(filename), "w", libver="latest") as f:
		f.create_dataset(
			# `chunks=(1, *data.shape[1:])`: optimize for row access!
			"array",
			shape=data.shape,
			data=data,
			chunks=(1, *data.shape[1:]),
			dtype=dtype,
		)
		if verbose:
			print(f"... done writing {filename}")


def load_h5_file(file_path: Union[str, Path]):
	with h5py.File(str(file_path) if isinstance(file_path, Path) else file_path, "r") as fr:
		data = fr.get("array")
		data = np.array(data)
		return data

def aggregate_data_file(filename):
	data_file = Path(filename).with_suffix('.h5')
	aggr_filename = filename + '_aggregated'
	aggr_filename_ext = Path(aggr_filename).with_suffix('.h5')
	print(data_file, aggr_filename_ext)
	data = load_h5_file(data_file)
	parts = []
	for index in range(0, 288, 12):
		parts.append(np.average(data[index: index + 6], axis=0))
	aggr_data = np.stack(parts)
	write_data_to_h5(aggr_data, aggr_filename_ext)
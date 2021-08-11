# Utils for flamingo WPS
import yaml
import os

from operator import itemgetter


dset_assets_file = os.path.join(os.path.dirname(__file__), 
                   "assets/flamingo/datasets.yml")


def get_dset_info(process):
    resp = yaml.load(open(dset_assets_file))

    process = process.replace("/", ".").split(".")[-1]
    processes = [r["process"] for r in resp]

    if process not in processes:
        raise KeyError(f"Process not found using key: {process}")

    data = [r for r in resp if r["process"] == process][0]

    datasets = [ds for ds in data["datasets"]]

    d = {}

    d["input_datasets"] = {ds["long_name"]: ds["name"] for ds in sorted(datasets, key=itemgetter("name"), 
                                                                        reverse=True)}
    d["input_variables"] = {value: key for key, value in sorted(data["variables"].items())}

    if "frequencies" in data:
        d["input_frequencies"] = {value: key for key, value in sorted(data["frequencies"].items())}

    if "spatial_averages" in data:
        d["input_spatial_averages"] = {value: key for key, value in sorted(data["spatial_averages"].items())}


    d["time_range"] = data["time_range"]
    d["bbox"] = data["bbox"]

    d["catalogue_records"] = {ds["name"].upper() + " record": ds["catalogue_record"] \
                              for ds in sorted(datasets, key=itemgetter("name"), reverse=True)}    
    return d


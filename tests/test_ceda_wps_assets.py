#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ceda_wps_assets` package."""

from ceda_wps_assets import flamingo as flamingo_assets


def test_flamingo_assets():
    d = flamingo_assets.get_dset_info("/vagrant-share/ceda-wps/flamingo/flamingo/processes/wps_subset_cru_ts.py")

    assert list(d["input_datasets"].items())[0] == ("Climatic Research Unit (CRU) TS (time-series) dataset 4.05", "cru_ts.4.05")
    assert list(d["input_variables"].items())[0] == ("cloud cover (percentage)", "cld")

    assert d["time_range"] == "1901-01-16/2020-12-16"
    assert d["bbox"] == "-180.0, -90.0, 180.0, 90.0,epsg:4326"

    assert list(d["catalogue_records"].values())[0] == "https://catalogue.ceda.ac.uk/uuid/c26a65020a5e4b80b20018f148556681"



#!/usr/bin/python3.3 -O
"""
Created on April 22, 2014

Convolitional channels config.

Copyright (c) 2013 Samsung Electronics Co., Ltd.
"""


import os

from veles.config import root


# optional parameters

root.model = "conv"

root.update = {"accumulator": {"n_bars": 30},
               "decision": {"fail_iterations": 1000,
                            "snapshot_prefix": "channels %s" % root.model,
                            "use_dynamic_alpha": False,
                            "do_export_weights": True},
               "conv": {  # "weights_filling": "uniform"},
                   "weights_filling": "gaussian",
                   "weights_stddev": 0.0001},
               "conv_relu": {  # "weights_filling": "uniform"
                   "weights_filling": "gaussian",
                   "weights_stddev": 0.0001},
               "image_saver": {"out_dirs":
                               [os.path.join(root.common.cache_dir,
                                             "tmp %s/test" % root.model),
                                os.path.join(root.common.cache_dir,
                                             "tmp %s/validation" %
                                             root.model),
                                os.path.join(root.common.cache_dir,
                                             "tmp %s/train" % root.model)]},
               "loader": {"cache_fnme": os.path.join(root.common.cache_dir,
                                                     "channels_%s.pickle"
                                                     % root.model),
                          "grayscale": False,
                          "minibatch_size": 81,
                          "n_threads": 32,
                          "channels_dir":
                          "/data/veles/VD/channels/russian_small/train",
                          "rect": (264, 129),
                          "validation_ratio": 0.15},
               "weights_plotter": {"limit": 64},
               "channels": {"export": False,
                            "find_negative": 0,
                            "global_alpha": 0.005,
                            "global_lambda": 0.004,
                            "layers":
                            [{"type": "conv", "n_kernels": 32,
                              "kx": 5, "ky": 5, "padding": (2, 2, 2, 2)},
                             {"type": "max_pooling",
                              "kx": 3, "ky": 3, "sliding": (2, 2)},
                             {"type": "conv", "n_kernels": 32,
                              "kx": 5, "ky": 5, "padding": (2, 2, 2, 2)},
                             {"type": "avg_pooling",
                              "kx": 3, "ky": 3, "sliding": (2, 2)},
                             {"type": "conv", "n_kernels": 64,
                              "kx": 5, "ky": 5, "padding": (2, 2, 2, 2)},
                             {"type": "avg_pooling",
                              "kx": 3, "ky": 3, "sliding": (2, 2)},
                             {"type": "softmax", "layers": 11}],
                            "snapshot": ""}}

from typing import NamedTuple


GROUND_LEVEL = {
    'birmingham_block_8': 9.767633576781428,
    'birmingham_block_5': 9.035724612581797,
    'cambridge_block_4': 37.4447906884959,
    'cambridge_block_32': 37.43283726180316,
    'cambridge_block_2': 37.619963888870764,
    'birmingham_block_10': 8.163523742999931,
    'birmingham_block_4': 12.510308110043573,
    'cambridge_block_12': 41.64058599525279,
    'cambridge_block_14': 43.83640200944717,
    'birmingham_block_9': 9.839007739084987,
    'cambridge_block_25': 40.61091891460477,
    'cambridge_block_9': 38.49224945510375,
    'cambridge_block_17': 35.684234558137426,
    'cambridge_block_27': 40.6977502452132,
    'cambridge_block_8': 41.62273423227555,
    'cambridge_block_28': 31.608505851194376,
    'birmingham_block_3': 13.178169088193988,
    'birmingham_block_6': 8.342005752216762,
    'birmingham_block_1': 10.02721669169363,
    'cambridge_block_18': 39.98595895231467,
    'cambridge_block_26': 42.35843426980253,
    'cambridge_block_33': 38.33041905329609,
    'cambridge_block_10': 34.02419401450328,
    'cambridge_block_21': 36.74889242048286,
    'birmingham_block_0': 16.048856444156698,
    'cambridge_block_22': 34.080272548771816,
    'cambridge_block_16': 36.817109712105065,
    'birmingham_block_12': 4.4762829987220245,
    'birmingham_block_13': 7.38571378212217,
    'birmingham_block_11': 7.368852686277198,
    'birmingham_block_7': 9.069972432079426,
    'cambridge_block_19': 41.064048426704154,
    'cambridge_block_13': 43.69745461677479,
    'cambridge_block_7': 39.464565007249114,
    'cambridge_block_20': 41.84850877729182,
    'cambridge_block_6': 35.84253359519473,
    'cambridge_block_15': 37.940351251848824,
    'cambridge_block_3': 37.80057158222191,
    'birmingham_block_2': 7.0204973115052995,
    'cambridge_block_23': 34.436207572934606
}

class Bounds(NamedTuple):
    x_min: float
    y_min: float
    x_max: float
    y_max: float

MAP_BOUNDS = {
    "birmingham_block_8": Bounds(799.95, 399.91874999999993, 1200.0500000000002, 800.01875),
    "birmingham_block_5": Bounds(399.95, 799.9187499999999, 800.05, 1200.01875),
    "cambridge_block_4": Bounds(113.3875, 1599.96875, 400.0875, 1802.26875),
    "cambridge_block_32": Bounds(1999.95, 1059.1499999999999, 2068.85, 1200.05),
    "cambridge_block_2": Bounds(-0.05, 799.9499999999999, 400.05, 1200.05),
    "birmingham_block_10": Bounds(799.95, 1199.9125, 1200.0500000000002, 1285.1125),
    "birmingham_block_4": Bounds(399.95, 399.91874999999993, 800.05, 800.01875),
    "cambridge_block_12": Bounds(799.95, 22.349999999999966, 1200.0500000000002, 400.05),
    "cambridge_block_14": Bounds(799.95, 799.9499999999999, 1200.0500000000002, 1200.05),
    "birmingham_block_9": Bounds(799.95, 799.9187499999999, 1200.0500000000002, 1200.01875),
    "cambridge_block_25": Bounds(1599.95, 512.4499999999999, 1817.3500000000001, 800.05),
    "cambridge_block_9": Bounds(399.95, 1199.9499999999998, 800.05, 1600.05),
    "cambridge_block_17": Bounds(799.95, 1999.9562500000002, 1200.0500000000002, 2136.95625),
    "cambridge_block_27": Bounds(1599.95, 1199.9499999999998, 2000.0500000000002, 1600.05),
    "cambridge_block_8": Bounds(399.95, 799.9499999999999, 800.05, 1200.05),
    "cambridge_block_28": Bounds(1599.95, 1599.9499999999998, 2000.0500000000002, 1918.05),
    "birmingham_block_3": Bounds(399.95, -0.08125000000001137, 800.05, 400.01875),
    "birmingham_block_6": Bounds(414.0125, 1199.8999999999999, 800.0125, 1306.8),
    "birmingham_block_1": Bounds(15.2, 399.91874999999993, 400.0, 800.01875),
    "cambridge_block_18": Bounds(1199.95, 146.35, 1490.0500000000002, 400.05),
    "cambridge_block_26": Bounds(1599.95, 799.9499999999999, 2000.0500000000002, 1200.05),
    "cambridge_block_33": Bounds(1999.95, 1199.9499999999998, 2152.95, 1600.05),
    "cambridge_block_10": Bounds(399.95, 1599.9499999999998, 800.05, 2013.55),
    "cambridge_block_21": Bounds(1199.95, 1199.9499999999998, 1600.0500000000002, 1600.05),
    "birmingham_block_0": Bounds(256.66875, 55.91874999999999, 400.06875, 400.01875),
    "cambridge_block_22": Bounds(1199.95, 1599.9499999999998, 1600.0500000000002, 2000.05),
    "cambridge_block_16": Bounds(799.95, 1599.9499999999998, 1200.0500000000002, 2000.05),
    "birmingham_block_12": Bounds(1199.95, 799.9187499999999, 1273.25, 1200.01875),
    "birmingham_block_13": Bounds(1199.95, 1199.90625, 1273.75, 1261.70625),
    "birmingham_block_11": Bounds(1199.95, 620.4187499999999, 1265.55, 800.01875),
    "birmingham_block_7": Bounds(799.95, 226.61875, 1119.65, 400.01875),
    "cambridge_block_19": Bounds(1199.95, 399.94999999999993, 1600.0500000000002, 800.05),
    "cambridge_block_13": Bounds(799.95, 399.94999999999993, 1200.0500000000002, 800.05),
    "cambridge_block_7": Bounds(399.95, 399.94999999999993, 800.05, 800.05),
    "cambridge_block_20": Bounds(1199.95, 799.9499999999999, 1600.0500000000002, 1200.05),
    "cambridge_block_6": Bounds(399.95, -0.05000000000001137, 800.05, 400.05),
    "cambridge_block_15": Bounds(799.95, 1199.9499999999998, 1200.0500000000002, 1600.05),
    "cambridge_block_3": Bounds(10.95, 1199.9499999999998, 400.05, 1600.05),
    "birmingham_block_2": Bounds(-0.05, 799.9499999999999, 400.05, 1099.55),
    "cambridge_block_23": Bounds(1199.95, 1999.9906250000001, 1456.3500000000001, 2107.690625),
}

TARGET_COLUMNS = {
    "success": "C",
    "justified_absence": "D",
    "unjustified_absence": "E",
    "reports": "F",
    "non_attendance": "G",
    "ratio": "H",
}

GROUPS = {
    "ESO1A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 6)
        },) * 3,
        "target_row": 2,
    },
    "ESO1B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 13)
        },) * 3,
        "target_row": 3,
    },
    "ESO1C": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 21)
        },) * 3,
        "target_row": 4,
    },
    "ESO1D": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 29)
        },) * 3,
        "target_row": 5,
    },
    "ESO2A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 6)
        },) * 3,
        "target_row": 6,
    },
    "ESO2B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 13)
        },) * 3,
        "target_row": 7,
    },
    "ESO2C": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 21)
        },) * 3,
        "target_row": 8,
    },
    "ESO2Z": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet5",
            "success": (26, 6)
        },) * 3,
        "target_row": 9,
    },
    "ESO3A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet3",
            "success": (34, 6)
        },) * 3,
        "target_row": 10,
    },
    "ESO3B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet3",
            "success": (34, 13)
        },) * 3,
        "target_row": 11,
    },
    "ESO3Z": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet6",
            "success": (26, 6)
        },) * 3,
        "target_row": 12,
    },
    "ESO4A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet4",
            "success": (38, 6)
        },) * 3,
        "target_row": 13,
    },
    "ESO4B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet4",
            "success": (38, 13)
        },) * 3,
        "target_row": 14,
    },
    "1FPB": {
        "source": ({
            "file_suffix": "_FPB",
            "sheet": "Sheet1",
            "success": (21, 6)
        },) * 2 + ({
            "file_suffix": "_1FPB",
            "sheet": "InformeRendimientoEscolar",
            "success": (21, 6)
        },),
        "target_row": 15,
    },
    "2FPB": {
        "source": ({
            "file_suffix": "_FPB",
            "sheet": "Sheet2",
            "success": (21, 6)
        },) * 2 + ({
            "file_suffix": "_2FPB",
            "sheet": "InformeRendimientoEscolar",
            "success": (21, 6)
        },),
        "target_row": 16,
    },
    "1CIE": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet1",
            "success": (29, 6)
        },) * 3,
        "target_row": 17,
    },
    "1SOC": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet2",
            "success": (29, 6)
        },) * 3,
        "target_row": 18,
    },
    "2CIE": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet3",
            "success": (30, 6)
        },) * 3,
        "target_row": 19,
    },
    "2SOC": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet4",
            "success": (31, 6)
        },) * 3,
        "target_row": 20,
    },
    "1TEL": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet1",
            "success": (22, 6)
        },) * 3,
        "target_row": 21,
    },
    "1ELE": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet2",
            "success": (21, 6)
        },) * 3,
        "target_row": 22,
    },
    "1CAR": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet3",
            "success": (21, 6)
        },) * 3,
        "target_row": 23,
    },
    "2TEL": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet1",
            "success": (23, 6)
        },) * 3,
        "target_row": 24,
    },
    "2ELE": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet2",
            "success": (24, 6)
        },) * 3,
        "target_row": 25,
    },
    "2CAR": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet3",
            "success": (22, 6)
        },) * 3,
        "target_row": 26,
    },
    "1ARI": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet1",
            "success": (24, 6)
        },) * 3,
        "target_row": 27,
    },
    "1ALO": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet2",
            "success": (24, 6)
        },) * 3,
        "target_row": 28,
    },
    "1GIT": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet3",
            "success": (24, 6)
        },) * 3,
        "target_row": 29,
    },
    "1ASR": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet4",
            "success": (23, 6)
        },) * 3,
        "target_row": 30,
    },
    "1DAW": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet5",
            "success": (23, 6)
        },) * 3,
        "target_row": 31,
    },
    "2ARI": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet1",
            "success": (23, 6)
        },) * 3,
        "target_row": 32,
    },
    "2ALO": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet2",
            "success": (23, 6)
        },) * 3,
        "target_row": 33,
    },
    "2GIT": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet3",
            "success": (23, 6)
        },) * 3,
        "target_row": 34,
    },
    "2ASR": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet4",
            "success": (24, 6)
        },) * 3,
        "target_row": 35,
    },
    "2DAW": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet5",
            "success": (23, 6)
        },) * 3,
        "target_row": 36,
    },
    "1DAM": {
        "source": (None, None, {
            "file_suffix": "_12DAM",
            "sheet": "Sheet1",
            "success": (20, 6)
        }),
        "target_row": 37,
    },
    "2DAM": {
        "source": (None, None, {
            "file_suffix": "_12DAM",
            "sheet": "Sheet2",
            "success": (21, 6)
        }),
        "target_row": 38,
    },
    "3DAM": {
        "source": (None, None, {
            "file_suffix": "_3DAM",
            "sheet": "InformeRendimientoEscolar",
            "success": (22, 6)
        }),
        "target_row": 39,
    }
}

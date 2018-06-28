GROUPS = {
    "ESO1A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 6)
        },) * 3,
        "target": {
            "success": "C2",
            "ratio": "G2",
            "reports": "E2",
            "non_attendance": "F2",
            "absence": "D2"
        }
    },
    "ESO1B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 13)
        },) * 3,
        "target": {
            "success": "C3",
            "ratio": "G3",
            "reports": "E3",
            "non_attendance": "F3",
            "absence": "D3"
        }
    },
    "ESO1C": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 21)
        },) * 3,
        "target": {
            "success": "C4",
            "ratio": "G4",
            "reports": "E4",
            "non_attendance": "F4",
            "absence": "D4"
        }
    },
    "ESO1D": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet1",
            "success": (29, 29)
        },) * 3,
        "target": {
            "success": "C5",
            "ratio": "G5",
            "reports": "E5",
            "non_attendance": "F5",
            "absence": "D5"
        }
    },
    "ESO2A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 6)
        },) * 3,
        "target": {
            "success": "C6",
            "ratio": "G6",
            "reports": "E6",
            "non_attendance": "F6",
            "absence": "D6"
        }
    },
    "ESO2B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 13)
        },) * 3,
        "target": {
            "success": "C7",
            "ratio": "G7",
            "reports": "E7",
            "non_attendance": "F7",
            "absence": "D7"
        }
    },
    "ESO2C": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet2",
            "success": (29, 21)
        },) * 3,
        "target": {
            "success": "C8",
            "ratio": "G8",
            "reports": "E8",
            "non_attendance": "F8",
            "absence": "D8"
        }
    },
    "ESO2Z": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet5",
            "success": (26, 6)
        },) * 3,
        "target": {
            "success": "C9",
            "ratio": "G9",
            "reports": "E9",
            "non_attendance": "F9",
            "absence": "D9"
        }
    },
    "ESO3A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet3",
            "success": (34, 6)
        },) * 3,
        "target": {
            "success": "C10",
            "ratio": "G10",
            "reports": "E10",
            "non_attendance": "F10",
            "absence": "D10"
        }
    },
    "ESO3B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet3",
            "success": (34, 13)
        },) * 3,
        "target": {
            "success": "C11",
            "ratio": "G11",
            "reports": "E11",
            "non_attendance": "F11",
            "absence": "D11"
        }
    },
    "ESO3Z": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet6",
            "success": (26, 6)
        },) * 3,
        "target": {
            "success": "C12",
            "ratio": "G12",
            "reports": "E12",
            "non_attendance": "F12",
            "absence": "D12"
        }
    },
    "ESO4A": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet4",
            "success": (38, 6)
        },) * 3,
        "target": {
            "success": "C13",
            "ratio": "G13",
            "reports": "E13",
            "non_attendance": "F13",
            "absence": "D13"
        }
    },
    "ESO4B": {
        "source": ({
            "file_suffix": "_ESO",
            "sheet": "Sheet4",
            "success": (38, 13)
        },) * 3,
        "target": {
            "success": "C14",
            "ratio": "G14",
            "reports": "E14",
            "non_attendance": "F14",
            "absence": "D14"
        }
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
        "target": {
            "success": "C15",
            "ratio": "G15",
            "reports": "E15",
            "non_attendance": "F15",
            "absence": "D15"
        }
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
        "target": {
            "success": "C16",
            "ratio": "G16",
            "reports": "E16",
            "non_attendance": "F16",
            "absence": "D16"
        }
    },
    "1CIE": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet1",
            "success": (29, 6)
        },) * 3,
        "target": {
            "success": "C17",
            "ratio": "G17",
            "reports": "E17",
            "non_attendance": "F17",
            "absence": "D17"
        }
    },
    "1SOC": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet2",
            "success": (29, 6)
        },) * 3,
        "target": {
            "success": "C18",
            "ratio": "G18",
            "reports": "E18",
            "non_attendance": "F18",
            "absence": "D18"
        }
    },
    "2CIE": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet3",
            "success": (30, 6)
        },) * 3,
        "target": {
            "success": "C19",
            "ratio": "G19",
            "reports": "E19",
            "non_attendance": "F19",
            "absence": "D19"
        }
    },
    "2SOC": {
        "source": ({
            "file_suffix": "_BACH",
            "sheet": "Sheet4",
            "success": (31, 6)
        },) * 3,
        "target": {
            "success": "C20",
            "ratio": "G20",
            "reports": "E20",
            "non_attendance": "F20",
            "absence": "D20"
        }
    },
    "1TEL": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet1",
            "success": (22, 6)
        },) * 3,
        "target": {
            "success": "C21",
            "ratio": "G21",
            "reports": "E21",
            "non_attendance": "F21",
            "absence": "D21"
        }
    },
    "1ELE": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet2",
            "success": (21, 6)
        },) * 3,
        "target": {
            "success": "C22",
            "ratio": "G22",
            "reports": "E22",
            "non_attendance": "F22",
            "absence": "D22"
        }
    },
    "1CAR": {
        "source": ({
            "file_suffix": "_1CFGM",
            "sheet": "Sheet3",
            "success": (21, 6)
        },) * 3,
        "target": {
            "success": "C23",
            "ratio": "G23",
            "reports": "E23",
            "non_attendance": "F23",
            "absence": "D23"
        }
    },
    "2TEL": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet1",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C24",
            "ratio": "G24",
            "reports": "E24",
            "non_attendance": "F24",
            "absence": "D24"
        }
    },
    "2ELE": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet2",
            "success": (24, 6)
        },) * 3,
        "target": {
            "success": "C25",
            "ratio": "G25",
            "reports": "E25",
            "non_attendance": "F25",
            "absence": "D25"
        }
    },
    "2CAR": {
        "source": ({
            "file_suffix": "_2CFGM",
            "sheet": "Sheet3",
            "success": (22, 6)
        },) * 3,
        "target": {
            "success": "C26",
            "ratio": "G26",
            "reports": "E26",
            "non_attendance": "F26",
            "absence": "D26"
        }
    },
    "1ARI": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet1",
            "success": (24, 6)
        },) * 3,
        "target": {
            "success": "C27",
            "ratio": "G27",
            "reports": "E27",
            "non_attendance": "F27",
            "absence": "D27"
        }
    },
    "1ALO": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet2",
            "success": (24, 6)
        },) * 3,
        "target": {
            "success": "C28",
            "ratio": "G28",
            "reports": "E28",
            "non_attendance": "F28",
            "absence": "D28"
        }
    },
    "1GIT": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet3",
            "success": (24, 6)
        },) * 3,
        "target": {
            "success": "C29",
            "ratio": "G29",
            "reports": "E29",
            "non_attendance": "F29",
            "absence": "D29"
        }
    },
    "1ASR": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet4",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C30",
            "ratio": "G30",
            "reports": "E30",
            "non_attendance": "F30",
            "absence": "D30"
        }
    },
    "1DAW": {
        "source": ({
            "file_suffix": "_1CFGS",
            "sheet": "Sheet5",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C31",
            "ratio": "G31",
            "reports": "E31",
            "non_attendance": "F31",
            "absence": "D31"
        }
    },
    "2ARI": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet1",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C32",
            "ratio": "G32",
            "reports": "E32",
            "non_attendance": "F32",
            "absence": "D32"
        }
    },
    "2ALO": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet2",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C33",
            "ratio": "G33",
            "reports": "E33",
            "non_attendance": "F33",
            "absence": "D33"
        }
    },
    "2GIT": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet3",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C34",
            "ratio": "G34",
            "reports": "E34",
            "non_attendance": "F34",
            "absence": "D34"
        }
    },
    "2ASR": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet4",
            "success": (24, 6)
        },) * 3,
        "target": {
            "success": "C35",
            "ratio": "G35",
            "reports": "E35",
            "non_attendance": "F35",
            "absence": "D35"
        }
    },
    "2DAW": {
        "source": ({
            "file_suffix": "_2CFGS",
            "sheet": "Sheet5",
            "success": (23, 6)
        },) * 3,
        "target": {
            "success": "C36",
            "ratio": "G36",
            "reports": "E36",
            "non_attendance": "F36",
            "absence": "D36"
        }
    },
    "1DAM": {
        "source": (None, None, {
            "file_suffix": "_12DAM",
            "sheet": "Sheet1",
            "success": (20, 6)
        }),
        "target": {
            "success": "C37",
            "ratio": "G37",
            "reports": "E37",
            "non_attendance": "F37",
            "absence": "D37"
        }
    },
    "2DAM": {
        "source": (None, None, {
            "file_suffix": "_12DAM",
            "sheet": "Sheet2",
            "success": (21, 6)
        }),
        "target": {
            "success": "C38",
            "ratio": "G38",
            "reports": "E38",
            "non_attendance": "F38",
            "absence": "D38"
        }
    },
    "3DAM": {
        "source": (None, None, {
            "file_suffix": "_3DAM",
            "sheet": "InformeRendimientoEscolar",
            "success": (22, 6)
        }),
        "target": {
            "success": "C39",
            "ratio": "G39",
            "reports": "E39",
            "non_attendance": "F39",
            "absence": "D39"
        }
    }
}

import config


def get_target_cell(group, key):
    return config.TARGET_COLUMNS[key] + str(config.GROUPS[group]["target_row"])

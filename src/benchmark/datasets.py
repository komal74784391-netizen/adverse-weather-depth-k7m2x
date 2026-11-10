import os

WEATHER_SPLITS = ('clear', 'rain', 'fog', 'snow', 'low_sun')


def list_split(root, split):
    if split not in WEATHER_SPLITS:
        raise ValueError(f'unknown split: {split}')
    folder = os.path.join(root, split)
    return sorted(os.listdir(folder))

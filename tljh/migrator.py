"""Migration utilities for upgrading tljh"""

import os
from datetime import date
import logging
import shutil

from tljh.config import (
    CONFIG_DIR,
    CONFIG_FILE,
    INSTALL_PREFIX,
)


logger = logging.getLogger("tljh")


def migrate_file(old_path, new_path):
    """Migrate one file from an old location to a new one

    avoids collisions if the new file exists
    """
    if not os.path.exists(old_path):
        return
    if os.path.exists(new_path):
        # new config file already created! still move the config,
        # but avoid collision
        timestamp = date.today().isoformat()
        dest = dest_base = "{}.old.{}".format(new_path, timestamp)
        i = 0
        while os.path.exists(dest):
            # avoid collisions
            dest = dest_base + ".{}".format(i)
            i += 1
        logger.warning("Found file in both old ({}) and new ({}).".format(old_path, new_path))
        logger.warning(
            "Moving {} to {} to avoid clobbering.  Its contents will be ignored.".format(old_path, dest)
        )
    else:
        dest = new_path
    shutil.move(old_path, dest)


def migrate_directory(old_dir, new_dir):
    """Migrate a directory to a new location"""
    if not os.path.exists(old_dir):
        return
    if os.path.exists(new_dir):
        # both dirs exist
        for f in os.listdir(old_dir):
            src = os.path.join(old_dir, f)
            dest = os.path.join(new_dir, f)
            if os.path.isdir(src):
                migrate_directory(src, dest)
            else:
                migrate_file(src, dest)
    else:
        logger.warning("Moving directory to new location {} -> {}".format(old_dir, new_dir))
        shutil.move(old_dir, new_dir)


def migrate_config_files():
    """Migrate config files to their new locations"""
    # handle old TLJH_DIR/config.yaml location
    migrate_file(os.path.join(INSTALL_PREFIX, "config.yaml"), CONFIG_FILE)
    migrate_directory(
        os.path.join(INSTALL_PREFIX, "jupyterhub_config.d"),
        os.path.join(CONFIG_DIR, "jupyterhub_config.d"),
    )

import logging
import os
import re
import sys
import warnings

ENVIRON = os.environ
logger = logging.getLogger(__name__)


def read_env(env_file=None, base_dir=None, **overrides):
    if env_file is None:
        frame = sys._getframe()
        env_file = os.path.join(
            os.path.dirname(base_dir or frame.f_back.f_code.co_filename), ".env" if base_dir else "../.env"
        )
        if not os.path.exists(env_file):
            warnings.warn(
                "%s doesn't exist - if you're not configuring your "
                "environment separately, create one." % env_file
            )
            return

    try:
        with open(env_file) if isinstance(env_file, str) else env_file as f:
            content = f.read()
    except OSError:
        warnings.warn(
            "Error reading %s - if you're not configuring your " "environment separately, check this." % env_file
        )
        return

    logger.debug("Read environment variables from: {}".format(env_file))

    for line in content.splitlines():
        m1 = re.match(r"\A(?:export )?([A-Za-z_0-9]+)=(.*)\Z", line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r"\\(.)", r"\1", m3.group(1))
            ENVIRON.setdefault(key, str(val))

    # set defaults
    for key, value in overrides.items():
        ENVIRON.setdefault(key, value)

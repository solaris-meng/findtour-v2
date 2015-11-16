
import logging
import logging.handlers

# Non Rotating
formatter = logging.Formatter("[%(asctime)s] %(levelname)-5s [%(name)s] [%(filename)s:%(lineno)d:%(funcName)s] %(message)s")
log_file = "/tmp/findtour_index"
log_fh = logging.FileHandler(log_file)
log_fh.setFormatter(formatter)

flog = logging.getLogger("findtour_index");
flog.setLevel(logging.INFO)
flog.addHandler(log_fh)

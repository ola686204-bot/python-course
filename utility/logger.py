"""Central operation logging for the CLI utility toolkit."""

from datetime import datetime

from file_handler import append_text, clear_file, read_text


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
LINE_END = "\n"
LOG_SEPARATOR = " - "


def get_timestamp():
    """Create the current formatted timestamp.

    Returns:
        str: Current date and time.
    """
    return datetime.now().strftime(TIMESTAMP_FORMAT)


def log_operation(message, log_path):
    """Append a timestamped operation to the log.

    Args:
        message (str): Operation description.
        log_path (str): Log file path.

    Returns:
        bool: True when logging succeeds.
    """
    entry = get_timestamp() + LOG_SEPARATOR + message + LINE_END
    return append_text(log_path, entry)


def view_logs(log_path):
    """Read all operation log entries.

    Args:
        log_path (str): Log file path.

    Returns:
        str: Log contents or an error message.
    """
    success, content = read_text(log_path)
    if not success:
        return "No log entries available."
    return content or "No log entries available."


def clear_logs(log_path):
    """Remove all entries from the operation log.

    Args:
        log_path (str): Log file path.

    Returns:
        bool: True when the log is cleared.
    """
    return clear_file(log_path)


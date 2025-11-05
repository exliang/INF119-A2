import argparse

def parse_command_line(argv):
    """
    Parses the command line arguments using the argparse module.

    Args:
        argv (list): A list of command line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Process a list of integers and optionally sum them.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Added for better help output
    )
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='A list of integers to process.')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='If provided, sum the integers. Otherwise, find the maximum (default).')

    args = parser.parse_args(argv)
    return args

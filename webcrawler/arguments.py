import argparse


def argparse_setup() -> argparse.Namespace:
    """Setup and return argparse."""
    parser = argparse.ArgumentParser(description="Web crawler test")

    parser.add_argument("-p", "--path", help="paths to datachunk file", type=str, nargs="*", action="extend", dest="paths")

    return validate_arguments(parser)


def validate_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """Validate arguments"""
    args = parser.parse_args()

    if not args.paths:
        parser.error("Provide paths to datachunks to crawl")

    return args

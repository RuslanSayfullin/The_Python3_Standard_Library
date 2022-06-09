# Changes from asyncio_executor_thread.py
if __name__ == '__main__':
    # Configure logging to show the ID of the process
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='PID %(process)5s %(name)18s: %(message)s',
        stream=sys.stderr,
    )
    # Create a limited process pool.
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=3,)


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(run_blocking_tasks(executor)
)
finally:
    event_loop.close()
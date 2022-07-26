import time
import psutil


def calculate_bandwidth():
    # get current bytes
    last_received, last_sent, last_total = get_receive_sent_total_bytes()

    while True:
        # get current bytes again
        bytes_received, bytes_sent, bytes_total = get_receive_sent_total_bytes()

        # calculate difference between them
        new_received = bytes_received - last_received
        new_sent = bytes_sent - last_sent
        new_total = bytes_total - last_total

        mb_new_received = convert_byte_to_mb(new_received)
        mb_new_sent = convert_byte_to_mb(new_sent)
        mb_new_total = convert_byte_to_mb(new_total)

        # show the info to user
        print(f'{mb_new_received:.2f} MB Received {mb_new_sent:.2f} MB Sent {mb_new_total:.2f} MB Total')

        # reinitialize current bytes
        last_received = bytes_received
        last_sent = bytes_sent
        last_total = bytes_total

        # wail 1 second
        time.sleep(1)


def get_receive_sent_total_bytes():
    received = psutil.net_io_counters().bytes_recv
    sent = psutil.net_io_counters().bytes_sent
    total = received + sent
    return received, sent, total


def convert_byte_to_mb(byte):
    return byte / 1024 / 1024


if __name__ == '__main__':
    calculate_bandwidth()

import pytest
import socket
import requests
import smtplib
from ping3 import ping
from ftplib import FTP

@pytest.fixture(scope="module")
def timeout():
    # Define a common timeout value for all network operations
    return 5

@pytest.mark.parametrize("url", [
    "http://www.google.com",
    "https://www.google.com",
    "http://www.github.com",
    "https://www.github.com",
    "http://www.microsoft.com",
    "https://www.microsoft.com"
])
def test_http_https_requests(url, timeout):
    """
    Test that HTTP and HTTPS requests to various external sites fail.
    Purpose: Ensure the container cannot access any web resources (HTTP/HTTPS).
    HTTP and HTTPS are the protocols used to browse the web. Blocking these ensures no web access.
    """
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(url, timeout=timeout)

@pytest.mark.parametrize("hostname", [
    "www.google.com",
    "www.github.com",
    "www.microsoft.com"
])
def test_dns_resolution(hostname):
    """
    Test that DNS resolution for various domain names fails.
    Purpose: Verify the container cannot resolve domain names to IP addresses.
    DNS (Domain Name System) translates human-readable domain names to IP addresses.
    Blocking DNS ensures the container cannot find the addresses of any web services.
    """
    with pytest.raises(socket.gaierror):
        socket.gethostbyname(hostname)

@pytest.mark.parametrize("address", [
    ("8.8.8.8", 80),
    ("8.8.4.4", 80),
    ("1.1.1.1", 80)
])
def test_socket_connection(timeout, address):
    """
    Test that socket connections to various external IPs fail.
    Purpose: Ensure the container cannot establish TCP connections.
    Sockets are used to open connections to other computers. Blocking this prevents data exchange.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        with pytest.raises((socket.timeout, OSError)):
            s.connect(address)

@pytest.mark.parametrize("ftp_server", [
    "ftp.debian.org",
    "ftp.gnu.org"
])
def test_ftp_connection(timeout, ftp_server):
    """
    Test that FTP connections to various external servers fail.
    Purpose: Verify the container cannot connect to FTP servers.
    FTP (File Transfer Protocol) is used to transfer files between computers. Blocking this prevents file transfers.
    """
    with pytest.raises(socket.gaierror):
        with FTP() as ftp:
            ftp.connect(ftp_server, timeout=timeout)

@pytest.mark.parametrize("icmp_target", [
    "8.8.8.8",
    "1.1.1.1"
])
def test_icmp_ping(timeout, icmp_target):
    """
    Test that ICMP ping requests to an external server fail.
    Purpose: Ensure the container cannot send ping requests (ICMP).
    Ping uses ICMP (Internet Control Message Protocol) to check if a server is reachable.
    Blocking ping prevents the container from testing connectivity to other servers.
    """
    try:
        response = ping(icmp_target, timeout=timeout)
        assert response is None
    except OSError as e:
        assert "Network is unreachable" in str(e), f"Unexpected error occurred: {e}"

@pytest.mark.parametrize("smtp_server", [
    "smtp.gmail.com",
    "smtp.mail.yahoo.com",
    "smtp.office365.com"
])
def test_smtp_connection(timeout, smtp_server):
    """
    Test that SMTP connections to various email servers fail.
    Purpose: Ensure the container cannot send emails (SMTP protocol).
    SMTP (Simple Mail Transfer Protocol) is used to send emails. Blocking this prevents the container from sending emails.
    """
    with pytest.raises((socket.timeout, OSError)):
        with smtplib.SMTP(smtp_server, 587, timeout=timeout) as server:
            server.noop()

@pytest.mark.parametrize("url, data", [
    ("http://www.google.com", {'key': 'value'}),
    ("https://www.google.com", {'key': 'value'})
])
def test_http_https_upload(url, data, timeout):
    """
    Test that HTTP/HTTPS POST requests to external sites fail.
    Purpose: Verify the container cannot upload data via HTTP/HTTPS.
    HTTP/HTTPS POST requests are used to send data to web servers. Blocking this prevents data uploads.
    """
    with pytest.raises(requests.exceptions.RequestException):
        requests.post(url, data=data, timeout=timeout)

@pytest.mark.parametrize("url", [
    "http://www.google.com/robots.txt",
    "https://www.google.com/robots.txt"
])
def test_http_https_download(url, timeout):
    """
    Test that HTTP/HTTPS GET requests to download data from external sites fail.
    Purpose: Ensure the container cannot download data via HTTP/HTTPS.
    HTTP/HTTPS GET requests are used to retrieve data from web servers. Blocking this prevents data downloads.
    """
    with pytest.raises(requests.exceptions.RequestException):
        requests.get(url, timeout=timeout)

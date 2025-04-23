import re
import dns.resolver
import smtplib
import socket
import argparse

# Regular expression for validating an Email
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email_format(email):
    return re.match(regex, email) is not None

def is_valid_domain(domain):
    disposable_domains = ["mailinator.com", "trashmail.com", "tempmail.com"]
    if domain in disposable_domains:
        return False
    try:
        dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        return False

def check_mx_records(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        return mx_record
    except Exception:
        return None

def check_mailbox(email):
    domain = email.split('@')[1]
    mx_record = check_mx_records(email)
    if mx_record:
        try:
            server = smtplib.SMTP(timeout=10)
            server.set_debuglevel(0)
            server.connect(mx_record)
            server.helo(socket.gethostname())
            server.mail('me@mydomain.com')
            code, _ = server.rcpt(email)
            server.quit()
            return code == 250
        except Exception:
            return False
    return False

def check_email(email):
    if not is_valid_email_format(email):
        return "Invalid email format"
    domain = email.split('@')[1]
    if not is_valid_domain(domain):
        return "Invalid or disposable domain"
    if check_mailbox(email):
        return "Valid email address"
    else:
        return "Email address does not exist or cannot be verified"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate an email address.")
    parser.add_argument("email", help="The email address to validate.")
    args = parser.parse_args()

    print(check_email(args.email))

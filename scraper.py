import argparse
import requests
import re


def main(args):
    r = requests.get(args.url)
    urls = re.findall(r'href="(http\S+)"', r.text)
    print('\n--- URLs ---\n')
    for url in set(urls):
        print(url)

    phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', r.text)
    print('\n--- Phone Numbers ---\n')
    for num in set(phone_numbers):
        print(num)

    email_addresses = re.findall(r'\S+@\S+\.S+', r.text)
    print('\n--- Email Adresses ---\n')
    for email in set(email_addresses):
        print(email)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Scrape a website for any URLs, email addresses,
        and phone numbers it contains.""")
    parser.add_argument('url', metavar='URL', type=str, help='a URL to scrape')

    args = parser.parse_args()

    main(args)
